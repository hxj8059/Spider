import scrapy
import json
import pandas as pd
import re


class FundPosition(scrapy.Spider):
    name = 'fund_position'

    def start_requests(self):
        start_url = "http://fund.eastmoney.com/{}.html"
        id_list = read_fund_id()
        for fund_code in id_list:
            url = start_url.format(fund_code)
            yield scrapy.Request(url=url, meta={'fund_code': fund_code}, callback=self.parse)

    def parse(self, response, **kwargs):
        fund_code = response.meta['fund_code']
        fund_scale = response.css('div div.fundInfoItem div.infoOfFund table tr:nth-child(1) td:nth-child(2)::text').get()
        fund_scale = re.findall(r'：(.*?)亿元', fund_scale)
        print(response.css('div div.fundInfoItem div.infoOfFund table tr:nth-child(1) td:nth-child(2)::text').get())
        # #body > div:nth-child(11) > div > div > div.fundDetail-main > div.fundInfoItem > div.infoOfFund > table > tbody > tr:nth-child(1) > td:nth-child(2)
        table = response.css('#position_shares tr')
        if len(table) > 2:
            for data in table[1:]:
                stock_code = data.css('td.alignLeft a::attr(href)').get()
                stock_code = re.findall(r'.com/(.*?).html', stock_code)
                if len(stock_code) > 0:
                    stock_code = stock_code[0].replace('/', '')
                stock_name = data.css('a::text').getall()
                if len(stock_name) > 0:
                    stock_name = stock_name[0]
                stock_per = data.css('td::text').getall()
                if len(stock_per) > 2:
                    stock_per = stock_per[2].strip('%')
                yield {'fund_code': fund_code,
                       'fund_scale': fund_scale,
                       'stock_name': stock_name,
                       'stock_per': stock_per,
                       'stock_code': stock_code}


def read_fund_id():
    path = 'share_fund_info.csv'
    data = pd.read_csv(path, converters={u'fund_code': str})
    return data["fund_code"]
