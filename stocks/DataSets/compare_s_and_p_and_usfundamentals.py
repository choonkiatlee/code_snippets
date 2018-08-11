import pandas as pd
import numpy as np
import re


usfundamentals = pd.read_csv('test.csv')
s_and_p_500 = pd.read_csv('s_and_p_500_companies_list.csv')

punctuation_list = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'        
        
regex_list = [
    r'/[a-z]+/',  # match 2 letter state codes: eg; /DE/, /PA/, /MA/...
    r'/[a-z]{2}', #used to match because some of the headings in the usfundamentals dataset is screwed
    re.escape('\\de\\'),
    '[{0}]'.format(re.escape(punctuation_list)),
    r'company',
    r'inc',
    r'co(?![a-z])',
    r'corporation',
    r'corp(?![a-z]) [a-c]',
    r'corp(?![a-z])',
    r'class [a-c]',
    r'com(?![a-z])',
    r'plc',
    r'the',
    r'limited',
    r'international',
    r'intl',
    r'company',
    r'holdings',
    r'ltd',
    r'companies',
    r'cos(?![a-z])',
    r'group',
    r'industries',
    r'nv',           #hack
    r'of washington' # hack
]
        
regex = re.compile('|'.join(regex_list))


# set to all lowercase and remove punctuation and things like inc, company, co 
def convert_string(input_string):
        
    try:
        input_string = input_string.lower()        
        return regex.sub('',input_string).strip().replace(' ','')
    except: 
        # not a valid string
        return input_string


s_and_p_500['simplified_name'] = s_and_p_500['Name'].apply(convert_string)
usfundamentals['simplified_name_latest'] = usfundamentals['name_latest'].apply(convert_string)
usfundamentals['simplified_names_previous'] = usfundamentals['names_previous'].apply(convert_string)

s_and_p_500_name_index = s_and_p_500.set_index('simplified_name')

name_latest_inner_join = s_and_p_500_name_index.join(usfundamentals.set_index('simplified_name_latest'),how='inner')
print("{0} items inner joined by name".format(len(name_latest_inner_join)))

names_previous_inner_join = s_and_p_500_name_index.join(usfundamentals.set_index('simplified_names_previous'),how='inner')
print("{0} items inner joined by names_previous".format(len(names_previous_inner_join)))

concated_join_dfs = pd.concat([name_latest_inner_join,names_previous_inner_join])

# These are companies that we could not match yet, mostly because they have flipped names
other_dfs = s_and_p_500_name_index.loc[~s_and_p_500_name_index.index.isin(concated_join_dfs.index)]
other_dfs.to_csv('other.csv')


manual_exclusion_list = [
        1300524,
        1073146,
        4515,
        1125259,
        20171,
        1141982,
        1551182,
        1678531,
        1578318,
        905428,
        1048268,
        1174746,
        53669,
        64670,
        1594420,
        77360,
        820096,
        1045609,
        53669,
        1056239,

        # slightly more unsure exclusions        
        8050613,
        850693,
        1054374,
        1649338,
        1668428,
        1308161,
        1647339

        
        ]

#Select out companies in the manual exclusion list
concated_join_dfs = concated_join_dfs.loc[~concated_join_dfs.company_id.isin(manual_exclusion_list)]

# Keep only duplicated columns. This will keep all A stocks
concated_join_dfs = concated_join_dfs[~concated_join_dfs.duplicated(subset = 'name_latest', keep='last')]

# These are duplicated columns, likely due to overly matchy regexes. Need to check manually!
#to_test = concated_join_dfs[concated_join_dfs.index.duplicated(keep=False)]

# Write out the final results:
concated_join_dfs.to_csv('combined.csv')
print('total of {0} items joined after slightly dubious cleaning'.format(len(concated_join_dfs)))

































