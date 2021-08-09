import pandas as pd

position_df = pd.read_csv('fund_position_cleaned.csv', encoding='utf-8' ,converters={'fund_code': str})
print(position_df.info)
industry_df = pd.read_csv('stock_list.csv', encoding='utf-8')

output_df = pd.merge(position_df, industry_df, 'left', left_on='ticker', right_on='ticker', left_index=False, right_index=False)
print(output_df)
fund_df = pd.read_csv('fund_info.csv', encoding='utf-8', converters={'fund_code': str, 'name_id': str})

# 'last_3m': float, '3m_rank': float,'last_6m': float,'6m_rank': float,'last_1y': float, '1y_rank': float,'last_2y': float, '2y_rank': float,'this_year': float,'this_year_rank': float
output_df = pd.merge(output_df, fund_df, 'left', left_on='fund_code', right_on='fund_code', left_index=False, right_index=False)
manager_df = pd.read_csv('fund_manager.csv', encoding='utf-8', converters={'name_id': str})
output_df = pd.merge(output_df, manager_df, 'left', left_on='name_id', right_on='name_id', left_index=False, right_index=False)
print(output_df.dtypes)
output_df.to_csv('test_merge.csv', index=False)

# base_df = pd.read_csv('share_fund_info.csv', encoding='utf-8')
# right1_df = pd.read_csv
