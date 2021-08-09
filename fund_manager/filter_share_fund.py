import pandas as pd

with open('fund_info.csv', 'r', encoding='utf-8') as info:
    df = pd.read_csv(info, converters={u'fund_code':str, u'name_id':str})
    print(df)
    print(df.dtypes)
    output = df[(df['fund_type'].str.contains("股票|混合型|QD"))&(~df['fund_type'].str.contains("不含|指数"))]
    print(output)
    output.to_csv('share_fund_info.csv', index=False)

