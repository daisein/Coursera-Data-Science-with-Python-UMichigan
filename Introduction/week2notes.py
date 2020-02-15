
# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# The Series Data Structure
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
import numpy as np

def series_data_structure():
    animals = ['Tiger', 'Bear', 'Moose']
    print(pd.Series(animals))

    numbers = [1, 2, 3]
    print(pd.Series(numbers))

    animals = ['Tiger', 'Bear', None]
    print(pd.Series(animals))

    numbers = [1, 2, None]
    print(pd.Series(numbers))

    print(np.nan == None)

    print(np.nan == np.nan)

    print(np.isnan(np.nan))

    sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
    s = pd.Series(sports)
    print(s)
    print(s.index)

    s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
    print(s)

    sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
    s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
    print('')
    print(s)

# series_data_structure()



# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# Querying a Series
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def query_series():
    sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
    s = pd.Series(sports)
    print(s)

    print('')
    print(s.iloc[3])

    print('')
    print(s.loc['Golf'])

    print('')
    print(s[3])

    print('')
    print(s['Golf'])

    sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
    s = pd.Series(sports)

    's[0]' #This won't call s.iloc[0] as one might expect, it generates an error instead

    print('')
    s = pd.Series([100.00, 120.00, 101.00, 3.00])
    print(s)

    total = 0
    for item in s:
        total+=item
    print(total)

    print('')
    total = np.sum(s)
    print(total)

    #this creates a big series of random numbers
    print('')
    s = pd.Series(np.random.randint(0,1000,10000))
    print(s)

    print(s.head())
    # print(s)

    print('')
    print(len(s))

    # %%timeit -n 100
    summary = 0
    for item in s:
        summary+=item
    print(summary)

    print('')
    s+=2 #adds two to each item in s using broadcasting
    print(s.head())

    print('')
    # AttributeError: 'Series' object has no attribute 'set_value'

    # for label, value in s.iteritems():
        # s.set_value(label, value+2)
    print(s.head())

    # 0    537
    # 1     88
    # 2    597
    # 3    765
    # 4    890
    # dtype: int64


    print('')
    # %%timeit -n 10
    s = pd.Series(np.random.randint(0,1000,10000))
    for label, value in s.iteritems():
        s.loc[label]= value+2
    print(s)
    # 1.36 s ± 32.3 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)



    # %%timeit -n 10

    print('')
    s = pd.Series(np.random.randint(0,1000,10000))
    s+=2
    print(s)
    # The slowest run took 22.33 times longer than the fastest. This could mean that an intermediate result is being cached. 1.1 ms ± 2 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

    print('')
    s = pd.Series([1, 2, 3])
    s.loc['Animal'] = 'Bears'
    print(s)

    print('')
    original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
    cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
    all_countries = original_sports.append(cricket_loving_countries)
    print(original_sports)

    print('')
    print(cricket_loving_countries)

    print('')
    print(all_countries)

    print('')
    print(all_countries.loc['Cricket'])

# query_series()



# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# The DataFrame Data Structure
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def dataframe_data_structure():
    purchase_1 = pd.Series({'Name': 'Chris',
                            'Item Purchased': 'Dog Food',
                            'Cost': 22.50})
    purchase_2 = pd.Series({'Name': 'Kevyn',
                            'Item Purchased': 'Kitty Litter',
                            'Cost': 2.50})
    purchase_3 = pd.Series({'Name': 'Vinod',
                            'Item Purchased': 'Bird Seed',
                            'Cost': 5.00})
    df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
    print(df.head())

    print('')
    print(df.loc['Store 2'])

    print('')
    print(type(df.loc['Store 2']))

    print('')
    print(df.loc['Store 1'])

    print('')
    print(df.loc['Store 1', 'Cost'])

    print('')
    print(df.T)

    print('')
    print(df.T.loc['Cost'])

    print('')
    print(df['Cost'])

    print('')
    print(df.loc['Store 1']['Cost'])

    print('')
    print(df.loc[:,['Name', 'Cost']])

    print('')
    print(df.drop('Store 1'))

    print()
    copy_df = df.copy()
    copy_df = copy_df.drop('Store 1')
    print(copy_df)

    # copy_df.drop?
    print()
    del copy_df['Name']
    print(copy_df)

    print()
    df['Location'] = None
    print(df)

    print('')
    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Dataframe Indexing and Loading')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')
    print('')

    costs = df['Cost']
    print(costs)

    print()
    costs+=2
    print(costs)

    print()
    print(df)

    # !cat olympics.csv
    print()
    df = pd.read_csv('olympics.csv')
    print(df.head())

    print()
    df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
    print(df.head())

    print()
    print(df.columns)

    print()
    for col in df.columns:
        if col[:2]=='01':
            df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
        if col[:2]=='02':
            df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
        if col[:2]=='03':
            df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
        if col[:1]=='№':
            df.rename(columns={col:'#' + col[1:]}, inplace=True)
    # print(df.head())


    print('')
    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Querying a DataFrame')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')
    print('')

    print(df['Gold'] > 0)

    print()
    only_gold = df.where(df['Gold'] > 0)
    print(only_gold.head())

    print()
    print(only_gold['Gold'].count())

    print()
    print(df['Gold'].count())

    print()
    only_gold = only_gold.dropna()
    print(only_gold.head())

    print()
    only_gold = df[df['Gold'] > 0]
    print(only_gold.head())

    print()
    print(len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]))

    print()
    print(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)])

    print('')
    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Indexing Dataframes')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')
    print('')

    print(df.head())

    print()
    df['country'] = df.index
    df = df.set_index('Gold')
    print(df.head())

    print()
    df = df.reset_index()
    print(df.head())

    print()
    df = pd.read_csv('census.csv')
    print(df.head())

    print()
    print(df['SUMLEV'].unique())

    print()
    df=df[df['SUMLEV'] == 50]
    print(df.head())

    print()
    columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
    df = df[columns_to_keep]
    print(df.head())

    print()
    df = df.set_index(['STNAME', 'CTYNAME'])
    print(df.head())

    print()
    print(df.loc['Michigan', 'Washtenaw County'])

    print()
    print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])

    print('')
    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('# Missing values')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')
    print('')

    df = pd.read_csv('log.csv')
    print(df)

    # df.fillna?

    df = df.set_index('time')
    df = df.sort_index()
    print(df)

    print()
    df = df.reset_index()
    df = df.set_index(['time', 'user'])
    print(df)

    print()
    df = df.fillna(method='ffill')
    print(df.head())

dataframe_data_structure()
