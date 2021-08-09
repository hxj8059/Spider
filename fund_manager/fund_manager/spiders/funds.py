import scrapy
import json
import pandas as pd
import re


class ManagerInfo(scrapy.Spider):
    name = 'funds'

    def start_requests(self):
        start_url = "http://fund.eastmoney.com/manager/{}.html"
        id_list = read_manager_id()
        for name_id in id_list:
            url = start_url.format(name_id)
            yield scrapy.Request(url=url, meta={'name_id': name_id}, callback=self.parse)

    def parse(self, response, **kwargs):
        item = {}
        fund_table = response.css('body div.content_out div:nth-child(2) table tbody')
        find_year = re.compile(r'(^\d*?)年')
        find_day = re.compile(r'(\d*?)天')
        name_id = response.meta['name_id']
        # name
        name = response.css('#name_1::text').get()
        response = response.css('div.jlinfo')
        # company
        company = response.css('div.left.clearfix.w438 div.right.jd a::text').get()
        # duration
        duration = response.css('div.left.clearfix.w438 div.right.jd::text').getall()
        if len(duration) > 1:
            duration = duration[1]
            day = re.findall(find_day, duration)
            year = re.findall(find_year, duration)
        else:
            duration = None
            day = None
            year = None
        # intro
        intro = response.css('div.right.ms p::text').getall()
        if len(intro) > 1:
            intro = intro[1].replace('\r\n', '').rstrip()
        else:
            intro = None
        # scale
        scale = response.css('div.left.clearfix.w438 div.right.jd div div.gmleft.gmlefts span.numtext span.redText::text').get()
        # best return
        best_return = response.css('div.left.clearfix.w438 div.right.jd div div.gmleft span.numtext span.redText::text').getall()
        if len(best_return) > 1:
            best_return = best_return[1].strip('%')
        else:
            best_return = None
        print(name)
        print(company)
        print(duration)
        print(intro)
        print(scale)
        print(best_return)
        # 每一只基金
        for fund in fund_table.css('tr'):
            # 每一列
            info_list = []
            key_list = ['fund_code', 'fund_name', 'fund_type', 'last_3m', '3m_rank', 'last_6m', '6m_rank', 'last_1y',
                        '1y_rank', 'last_2y', '2y_rank', 'this_year', 'this_year_rank']
            for col in fund.css('td'):
                if len(col.css('a::text')) != 0:
                    output = col.css('a::text').get()
                elif len(col.css('::text')) >= 3:
                    rank_list = col.css('::text').getall()
                    # 前%名
                    if rank_list[0] == '-' or rank_list[2] == '-':
                        output = '-'
                    else:
                        output = int(rank_list[0])/int(rank_list[2])
                        output = round(output, 3)
                elif len(col.css('::text')) == 1:
                    output = col.css('::text').get()
                else:
                    output = None
                info_list.append(output)
            print(info_list)
            for i in range(len(key_list)):
                item[key_list[i]] = info_list[i]
            item['name'] = name
            item['name_id'] = name_id
            yield item


def read_manager_id():
    path = 'managers_id.csv'
    data = pd.read_csv(path)
    return data["name_id"]

# body > div:nth-child(8) > div.content_out > div:nth-child(2) > table > tbody