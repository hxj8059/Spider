# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import re

data_out = []


class ZolSpider(scrapy.Spider):
    name = 'zol'

    def start_requests(self):
        index_list = get_index_list()
        for index in index_list:
            index = str(index)
            url = "https://detail.zol.com.cn/1146/%s/param.shtml" % (index)
            yield scrapy.Request(url=url, callback=self.parse)

        # with open(r"zol_phone\phone_details_indent_new_1.json", "w", encoding='utf-8') as datafile:
        #     json.dump(data_out, datafile, ensure_ascii=False, indent=2)

    def parse(self, response):
        contents = response.css("div.detailed-parameters table")
        one_phone = {}
        # 找回手机index
        link = response.url
        find_index = re.compile(r"\d/(\d*?)/")
        index = re.findall(find_index, link)[0]
        one_phone["id"] = index
        for table in contents:
            table_contents = table.css("tr")
            # skip the first one
            for row in table_contents[1:]:
                # 行标题为链接
                if row.css("th span::text").get() is None:
                    one_phone[row.css("th a::text").get()] = row.css("td span::text").getall()
                    # {row.css("th a::text").get(): row.css("td span::text").get()}
                # 行内容为链接
                elif row.css("td span::text").get() is None or row.css("td span::text").get() == "，" \
                        or "高清" in row.css("td span::text").get() or "普通" in row.css("td span::text").get():
                    one_phone[row.css("th span::text").get()] = row.css("td a::text").getall()
                    # {row.css("th span::text").get(): row.css("td a::text").get().replace(">", "")}
                # 正常
                else:
                    one_phone[row.css("th span::text").get()] = row.css("td span::text").getall()
                    # {row.css("th span::text").get(): row.css("td span::text").get()}
        return one_phone


def get_index_list():
    input_file = pd.read_excel(r"zol_phone\11111.xlsx", sheet_name='Sheet3')
    index_values = input_file["index_zol"].values
    index_list = index_values.tolist()
    print(index_list)
    return index_list
