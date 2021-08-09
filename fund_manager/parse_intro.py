import pandas as pd

# 模型输出结果到csv文件

token = open('token_test.txt','r', encoding='utf-8')
label = open('label_test.txt','r',encoding='utf-8')
token_list = token.readlines()

line = -1
cnt = -1
pro = []
result = ''
for one_label in label.readlines():
    line += 1
    if one_label == '[CLS]\n':
        cnt += 1

    if 'PRO' in one_label:
        result = result + token_list[line].strip('\n')

    if one_label == '[SEP]\n':
        pro.append(result)
        result = ''

with open('degree.csv', encoding='utf-8') as fund:
    df = pd.read_csv(fund)
    print(len(df['intro']))
    df['major'] = pro
    df.to_csv('fund_manager.csv')

token.close()
label.close()
