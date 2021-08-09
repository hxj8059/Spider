import scrapy
import json
import pandas as pd
import re


class ManagerInfo(scrapy.Spider):
    name = 'manager_info'

    def start_requests(self):
        start_url = "http://fund.eastmoney.com/manager/{}.html"
        id_list = read_manager_id()
        for name_id in id_list:
            url = start_url.format(name_id)
            yield scrapy.Request(url=url, meta={'name_id': name_id}, callback=self.parse)

    def parse(self, response, **kwargs):
        item = {}
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
        item['name'] = name
        item['name_id'] = name_id
        item['company'] = company
        item['duration'] = duration
        item['duration-year'] = year
        item['duration-day'] = day
        item['intro'] = intro
        item['scale(100million)'] = scale
        item['best_return(%)'] = best_return
        yield item


def read_manager_id():
    path = 'managers_id.csv'
    data = pd.read_csv(path)
    return data["fund_code"]
