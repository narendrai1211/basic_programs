import time

import sklearn
import pandas as pd
df_bankrupt = pd.read_excel('~/Downloads/data1.xlsx', sheet_name='A_bankrupt')
df_non_bankrupt = pd.read_excel('~/Downloads/data1.xlsx', sheet_name='B_non_bankrupt')
print(df_bankrupt.columns)


def get_matching_codes():
    s = df_bankrupt.groupby(['Primary UK SIC (2007) code'])['Total Assets\nth GBP Year - 1'].apply(list)
    bankrupt_group_by = s.to_frame()
    print(bankrupt_group_by.shape)
    list_ids = bankrupt_group_by.index.to_list()
    list_ids.sort()
    print(len(list_ids))
    df_matched_codes = df_non_bankrupt[df_non_bankrupt['Primary UK SIC (2007) code'].isin(list_ids)]
    return df_matched_codes


def ten_percent_up_down():
    # df_bankrupt['percent_mark'] = (df_bankrupt['Total Assets\nth GBP Year - 1'] > df_non_bankrupt['Total Assets\nth GBP Year - 1'].quantile(0.10)).astype(int)
    # print(df_bankrupt['percent_mark'].value_counts())

    list_cmp_values = []
    # list_ten_down = []

    for i, row in df_bankrupt.iterrows():
        ten_percent_of_row = row['Total Assets\nth GBP Year - 1'] * 0.1
        up_value = row['Total Assets\nth GBP Year - 1'] + ten_percent_of_row
        # print()
        down_value = row['Total Assets\nth GBP Year - 1'] - ten_percent_of_row
        list_cmp_values.append([row['Total Assets\nth GBP Year - 1'], up_value, down_value])
    df_bankrupt['compare_values_list'] = list_cmp_values

    return df_bankrupt, matched_code_df

import ast

id_col_name = 'Primary UK SIC (2007) code'
asset_col_name = 'Total Assets\nth GBP Year - 1'

def compare_and_contrast():
    matched_code_df = get_matching_codes()
    # df_bankrupt_with_cmp_values, matched_code_df = ten_percent_up_down()
    # df_bankrupt_with_cmp_values[id_col_name]
    # print(df_bankrupt_with_cmp_values.columns)
    # df_bankrupt_sorted_by_id = df_bankrupt_with_cmp_values.sort_values(by=['Primary UK SIC (2007) code'])
    # matched_code_df_sorted_by_id = matched_code_df.sort_values(by=['Primary UK SIC (2007) code'])
    # print(df_bankrupt_sorted_by_id['Primary UK SIC (2007) code'], matched_code_df_sorted_by_id['Primary UK SIC (2007) code'])
    list_values = []

    for i_val, row_bankrupt in df_bankrupt.iterrows():
        print('Comparing for', row_bankrupt[id_col_name])
        time.sleep(5)
        ten_percent_of_row = row_bankrupt['Total Assets\nth GBP Year - 1'] * 0.1
        up_value = row_bankrupt['Total Assets\nth GBP Year - 1'] + ten_percent_of_row
        down_value = row_bankrupt['Total Assets\nth GBP Year - 1'] - ten_percent_of_row
        list_values.append([row_bankrupt[id_col_name], up_value, down_value])
 
        for i, row in matched_code_df.iterrows():
            print(row['Company name'], int(row[id_col_name]))
            temp_df = matched_code_df[matched_code_df[id_col_name] == int(row_bankrupt[id_col_name])]
            print(temp_df)

            # temp_df['difference'] = temp_df[asset_col_name] - [i for i in list_values]
            print(temp_df)


compare_and_contrast()


# df_bankrupt_with_cmp_values.to_csv('output_bankrupt_values.csv', index=False)


