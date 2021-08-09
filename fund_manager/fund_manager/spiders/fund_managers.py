import scrapy
import json
import pandas as pd
import copy
import re


class FundManagerSpider(scrapy.Spider):
    name = 'fund_managers'

    def start_requests(self):
        start_url = "http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pn=50&pi={}&sc=abbname&st=asc"
        for i in range(1, 55):
            url = start_url.format(str(i))
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        print(response)
        json_data = response.text
        start = json_data.find("{")
        json_data = json_data[start:]
        json_data = json_data.replace("data", '"data"').replace("record", '"record"').replace("pages", '"pages"').replace("curpage", '"curpage"')
        json_data = json.loads(json_data)
        data_list = json_data['data']
        item = {}
        for data in data_list:
            item["name_id"] = data[0]
            item["name"] = data[1]
            item["company"] = data[3]
            item["scale(100million)"] = data[10].strip("亿元")
            item["best_return(%)"] = data[11].strip('%')
            yield item


