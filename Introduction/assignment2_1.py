import pandas as pd
import numpy as np


df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('


df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')


# print(df.sort_values(by=['Gold']))


#
# question 2
#

def q2():
    max_diff = 0

    for index, row in df.iterrows():
        # print(abs(row['Gold'] - row['Gold.1']), row['ID'], index)
        diff = abs(row['Gold'] - row['Gold.1'])
        if diff > max_diff:
            max_diff = diff
            target_country = row['ID']

    # print(target_country, max_diff)




#
# Question 3
#

def q3():
    max_stand_diff = 0

    for index, row in df.iterrows():
        # print(abs(row['Gold'] - row['Gold.1']), row['ID'], index)
        if row['Gold.2'] != 0 and row['Gold.1']!= 0 and row['Gold']!=0:
            # print(index)
            stan_diff = float(abs(row['Gold'] - row['Gold.1'])) / float(row['Gold.2'])
            if stan_diff > max_stand_diff:
                max_stand_diff = stan_diff
                target_country2 = index
                print(target_country2, max_stand_diff)

    print(target_country2, max_stand_diff)


#
# Question 4
#

print(df)

def q4():

    points_list = []
    country_names = []
    for index, row in df.iterrows():
        # print(index, row)
        points = row['Gold.2'] * 3 + row['Silver.2'] * 2 + row['Bronze.2']
        print(points)
        points_list.append(points)
        country_names.append(index)

    ser = pd.Series(points_list, index=country_names)
    return ser

    # df.insert(loc=0, column = 'Points', value=points_list)
    # return df['Points']

# print(q4())


#
# Question 5
#
