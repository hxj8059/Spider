import pandas as pd


with open('degree.csv', encoding='utf-8') as src:
    df = pd.read_csv(src)
    with open('newtest.txt','w', encoding='utf-8') as test:
        for line in df['intro']:
            for each in str(line)[:100]:
                if each == ',':
                    each = '，'
                if each != ' ' and each != '\n':
                    test.writelines(each+" O" + '\n')
            test.write('\n')
