import pandas as pd

df = pd.read_csv('fund_position1.csv', encoding='utf-8', converters={'fund_code': str})
print(df['stock_code'])
stock = df['stock_code']
code_list = []
# index = []
for code in stock:
    country = code[:2]
    index = code[2:]
    ts_code = ''
    if str(country) == 'us':
        ts_code = str(index) + ' US EQUITY'
    elif str(country) == 'hk':
        ts_code = str(index).lstrip('0') + ' ' + 'HK' + ' EQUITY'
    elif str(country).isalpha():
        ts_code = str(index) + ' ' + 'CH' + ' EQUITY'
    else:
        ts_code = code
    print(ts_code)
    code_list.append(ts_code)

df['ticker'] = code_list

df.to_csv('fund_position_cleaned.csv', index=False)

