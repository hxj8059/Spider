from scrapy import Selector
import re
import pandas as pd
import csv

output = []
body = open('../breo.html', encoding="utf-8").read()
# 使用scrapy自身的Selector解析文本
selector = Selector(text=body)
find_link = re.compile('href="https://item.jd.com/(.*?).html"')


# 获得所有a标签中的链接
a_list = selector.css("ul.gl-warp li div div.p-img a").getall()
print(a_list)
for one in a_list:
    id_list = re.findall(find_link, one)
    # print(re.findall(find_link, one))
    for shitou_id in id_list:
        print(shitou_id)
        output.append(shitou_id)

print(output)
df = pd.DataFrame(output)
df.to_csv('breo.csv')
#J_goodsList > ul > li:nth-child(2) > div > div.p-name.p-name-type-3 > a
#J_goodsList > ul > li:nth-child(1) > div > div.p-img > a
//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img