import pandas as pd
import numpy as np

# Merging Dataframes

def merge_dataframes():
    df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                       {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                       {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                      index=['Store 1', 'Store 1', 'Store 2'])

    print(df)

    print()
    df['Date'] = ['December 1', 'January 1', 'mid-May']
    print(df)

    print()
    df['Delivered'] = True
    print(df)

    print()
    df['Feedback'] = ['Positive', None, 'Negative']
    print(df)

    print()
    adf = df.reset_index()
    adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
    print(adf)

    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])

    staff_df = staff_df.set_index('Name')

    print()
    print(staff_df.head())

    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                               {'Name': 'Mike', 'School': 'Law'},
                               {'Name': 'Sally', 'School': 'Engineering'}])
    student_df = student_df.set_index('Name')


    print()
    print(student_df.head())

    print()
    print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))

    print()
    print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))

    print()
    print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))

    print()
    print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

    print()
    staff_df = staff_df.reset_index()
    student_df = student_df.reset_index()
    print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))


    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])

    print()
    print(staff_df)

    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

    print()
    print(student_df)

    print()
    print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))

    staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                             {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                             {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
    print()
    print(staff_df)

    student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                               {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                               {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])


    print()
    print(student_df)

    print()
    print(pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name']))

# merge_dataframes()


# Idiomatic Pandas: Making Code Pandorable

def idomatic_pandas():
    df = pd.read_csv('census.csv')
    print(df)

    print()
    print((df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})))

    print()
    df = df[df['SUMLEV']==50]
    df.set_index(['STNAME','CTYNAME'], inplace=True)
    df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
    print(df)

    def min_max(row):
        data = row[['POPESTIMATE2010',
                    'POPESTIMATE2011',
                    'POPESTIMATE2012',
                    'POPESTIMATE2013',
                    'POPESTIMATE2014',
                    'POPESTIMATE2015']]
        return pd.Series({'min': np.min(data), 'max': np.max(data)})
    print(df.apply(min_max, axis=1))

    rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
    print(df.apply(lambda x: np.max(x[rows]), axis=1))

# idomatic_pandas()

# Group by

def group_by():
    df = pd.read_csv('census.csv')
    df = df[df['SUMLEV']==50]
    print(df)
    # %%timeit -n 10
    # for state in df['STNAME'].unique():
    #     avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    #     # print('Counties in state ' + state + ' have an average population of ' + str(avg))


    # %%timeit -n 10
    print()
    for group, frame in df.groupby('STNAME'):
        avg = np.average(frame['CENSUS2010POP'])
        # print('Counties in state ' + group + ' have an average population of ' + str(avg))

    print()
    for group, frame in df.groupby('STNAME'):
        print(frame)

    print()
    print(df.head())

    print()
    df = df.set_index('STNAME')

    def fun(item):
        if item[0]<'M':
            return 0
        if item[0]<'Q':
            return 1
        return 2

    for group, frame in df.groupby(fun):
        print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

    print()
    df = pd.read_csv('census.csv')
    df = df[df['SUMLEV']==50]

    df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

    print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
    print(type(df.groupby(level=0)['POPESTIMATE2010']))

    # (df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum}))
    #
    # (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    # .agg({'avg': np.average, 'sum': np.sum}))
    #
    # (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    # .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))

# group_by()


def scales():
    df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
    df.rename(columns={0: 'Grades'}, inplace=True)
    print(df)

    print()
    # print(df['Grades'].astype('category').head())

    grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
    grades.head()

    # df = pd.read_csv('census.csv')
    # df = df[df['SUMLEV']==50]
    # df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
    # pd.cut(df['avg'],10)
    #

# scales()


def pivot_tables():
    #http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64
    df = pd.read_csv('cars.csv')
    print(df.head())

    print()
    print(df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean))

    print()
    print(df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True))

    print()
    print(df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.max], margins=True))

# pivot_tables()

# Date Functionality in Pandas

def date_functionality():
    print(pd.Timestamp('9/1/2016 10:05AM'))

    print(pd.Period('1/2016'))
    print(pd.Period('3/5/2016'))

    t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
    print(t1)

    print(type(t1.index))

    print()
    t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
    print(t2)

    print(type(t2.index))

    d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
    ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
    print(ts3)

    print()
    ts3.index = pd.to_datetime(ts3.index)
    print(ts3)

    print()
    print(pd.to_datetime('4.7.12', dayfirst=True))

    print()
    print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))

    print()
    print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))

    print()
    print(pd.Timestamp('10/14/2019')-pd.Timestamp('today'))

    ### Working with Dates in a Dataframe

    print()
    dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
    print(dates)

    print()
    df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
    print(df)

    print()
    # print(df.index.weekday_name)

    print()
    print(df.diff())

    print()
    print(df.resample('M').mean())

    print()
    print(df['2017'])

    print()
    print(df['2016-12'])

    print()
    print(df['2016-12':])

    print()
    print(df.asfreq('W', method='ffill'))

    import matplotlib.pyplot as plt
    # %matplotlib inline

    df.plot()
    plt.show()

date_functionality()
