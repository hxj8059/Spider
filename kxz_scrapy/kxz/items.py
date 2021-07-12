# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KxzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()


class CommentItem(scrapy.Item):
    user_id = scrapy.Field()
    comment = scrapy.Field()
    buy_date = scrapy.Field()
    star = scrapy.Field()
    com_date = scrapy.Field()
    product_name = scrapy.Field()
