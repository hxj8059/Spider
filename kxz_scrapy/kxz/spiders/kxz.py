# -*- coding: utf-8 -*-
import scrapy
from kxz import items
import re

# 先在settings.py中添加cookie
# scrapy crawl kxz -O indexlist.csv
# Step1 获取product_id
index_dic = {}


class KXZSpider(scrapy.Spider):
    name = 'kxz'

    def start_requests(self):
        # 45
        for index in range(1, 45):
            index = str(index)
            url = "https://search.jd.com/search?keyword=%E5%BC%80%E5%B0%8F%E7%81%B6&qrst=1&wq=%E5%BC%80%E5%B0%8F%E7%81%B6&stock=1&ev=exbrand_%E7%BB%9F%E4%B8%80%EF%BC%88President%EF%BC%89%5E&pvid=de2236fef3a84fd1a756c205b7e948cf&page={0}&s=1261&click=0"
            url = url.format(index)
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        contents = response.css("ul.gl-warp li div div.p-img a").getall()
        find_id = re.compile(r'href="//item.jd.com/(\d*?).html')
        info = items.KxzItem()
        for content in contents:
            sku_id = re.findall(find_id, content)[0]
            print(sku_id)
            info["index"] = sku_id
            yield info