from bs4 import BeautifulSoup
import re

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# string filter: find matching content
# t_list = bs.find_all("a")

# re
# regular expression search()
# t_list= bs.find_all(re.compile("a"))

# function search


# def name_is_exists(tag):
#     return tag.has_attr("name")
#
#
# t_list = bs.find_all(name_is_exists)

# kwargs
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href="http://news.baidu.com")
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
# t_list = bs.find_all(text=re.compile("hao123"))

# css选择器

# t_list = bs.select("title")
# t_list = bs.select(".mnav")
# t_list = bs.select("#u1")
# t_list = bs.select("a[class='bri']")
t_list = bs.select("title")


for item in bs:
    print(item)
