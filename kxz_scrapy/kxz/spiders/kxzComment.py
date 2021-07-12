# -*- coding: utf-8 -*-
import scrapy
import json
import time
from kxz import items
import csv


# scrapy crawl kxzcomment -O comment.csv
# Step2 根据获取的product_id_list爬取评论数据
class KXZSpider(scrapy.Spider):
    def __init__(self):
        # sorttype=6: 按时间排序
        # sorttype=5: 默认排序
        # productPageComments 该页面所有商品评论
        # skuproductPageComments 只看该商品评论
        self.format_url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98&productId={0}&score=0&sortType=6&page={1}&pageSize=10&isShadowSku=0&fold=1"
        self.current_product = ''
        self.max_page = 0
        self.item = items.CommentItem()
        self.product_i = 0
        self.page_i = 0
    name = 'kxzcomment'

    def start_requests(self):
        product_list = get_product_list('indexlist.csv')
        # product_list = ['53659143385', '64329880873', '10025849091308']
        for product_i in range(len(product_list)):
            self.current_product = product_list[product_i]
            url = self.format_url.format(product_list[product_i], "0")
            yield scrapy.Request(url=url, callback=self.parse_max_page)

    # 获取最大页数和第一页评论
    def parse_max_page(self, response):
        print('startMAX')
        try:
            json_text = response.text
            start_loc = json_text.find("{")
            json_data = json_text[start_loc:-2]
            print(json_data)
            json_data = json.loads(json_data)
            self.max_page = json_data['maxPage']
            print("最大页数%s" % self.max_page)
            for page_i in range(self.max_page):
                url = self.format_url.format(self.current_product, page_i)
                print("URL:", url)
                yield response.follow(url=url, callback=self.parse, dont_filter=True)
        except Exception as e:
            print("Error occurred: waiting 300s to retry", e)
            self.product_i -= 1
            time.sleep(300)

    # 获取评论数据
    def parse(self, response):
        print('startMAIN')
        try:
            json_text = response.text
            start_loc = json_text.find("{")
            json_data = json_text[start_loc:-2]
            print(json_data)
            json_data = json.loads(json_data)
            pageLen = len(json_data['comments'])
            print('total', pageLen)
            for i in range(0, pageLen):
                self.item['user_id'] = json_data['comments'][i]['id']
                self.item['comment'] = json_data['comments'][i]['content']
                self.item['buy_date'] = json_data['comments'][i]['referenceTime']
                self.item['com_date'] = json_data['comments'][i]['creationTime']
                self.item['product_name'] = json_data['comments'][i]['referenceName']
                self.item['star'] = json_data['comments'][i]['score']
                yield self.item
        except Exception as e:
            print("Error occurred: waiting 300s to retry", e)
            self.page_i -= 1
            time.sleep(300)


def get_product_list(list_path):
    product_list = []
    with open(list_path, encoding='utf-8') as st:
        reader = csv.reader(st)
        for row in reader:
            product_list.append(row[0])
    return product_list







