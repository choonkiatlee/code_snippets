import pandas as pd

usfundamentals = pd.read_csv('test.csv')
s_and_p_500 = pd.read_csv('s_and_p_500_companies_list.csv')

s_and_p_500_name_index = s_and_p_500.set_index('Name')

name_latest_inner_join = s_and_p_500_name_index.join(usfundamentals.set_index('name_latest'),how='inner')

print(name_latest_inner_join.head())
print("{0} items inner joined by name_latest".format(len(name_latest_inner_join)))

names_previous_inner_join = s_and_p_500_name_index.join(usfundamentals.set_index('names_previous'),how='inner')

print(names_previous_inner_join.head())
print("{0} items inner joined by names_previous".format(len(names_previous_inner_join)))

concated_join_dfs = pd.concat([name_latest_inner_join,names_previous_inner_join],sort=False)

other_dfs = s_and_p_500_name_index.loc[~s_and_p_500_name_index.index.isin(concated_join_dfs.index)]
other_dfs.to_csv('other.csv')