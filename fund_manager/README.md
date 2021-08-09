# 天天基金基金经理信息&基金信息爬取和处理

## scrapy
`fund_managers.py`  - 基金经理和基金经理id

`manager_info.py` - 基金经理历史信息和简介

`funds.py` - 基金经理管理的基金和概览

`fund_position` - 基金经理持仓信息、规模等信息

## clean

`cv_clean.py` - 学历和相关持证信息

`clean_position.py` - 匹配持仓股票代码和数据库内的股票代码来获取行业信息

`join.py` - join持仓table和行业信息table

`intro_line.py` - 处理基金经理简介信息以便[训练的nlp-ner模型](https://github.com/hxj8059/NER_Albert) 处理

`parse_intro.py` - 模型输出结果到csv文件