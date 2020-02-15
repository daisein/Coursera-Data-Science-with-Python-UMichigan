"""
# Assignment 4 - Hypothesis Testing

Definitions:
* A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
* A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
* A _recession bottom_ is the quarter within a recession which had the lowest GDP.
* A _university town_ is a city which has a high percentage of university students compared to the total population of the city.

**Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)

The following data files are available for this assignment:
* From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
* From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
* From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```. For this assignment, only look at GDP data from the first quarter of 2000 onward.
"""

import pandas as pd
import numpy as np
import math
from scipy.stats import ttest_ind


# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '''

    # load university_towns.txt
    university_towns_dict = {}

    with open('university_towns.txt') as file:
        for line in file:
            # print(line[:-1])
            if '[edit]' in line:
                university_towns = []
                # print(line[:line.index('[')])
                university_towns_dict[line[:line.index('[')]] = university_towns
            elif '[edit]' not in line and '(' in line:
                university_towns.append(line[:(line.index('(') - 1)])
            # university_towns.append(line)
    # print(university_towns_dict)

    state = []
    RegionName = []
    for key, value in university_towns_dict.items():
        for idx in range(len(value)):
            # print(key, value[idx])
            state.append(key)
            RegionName.append(value[idx])

    df_dict = {'State': state, 'RegionName': RegionName}
    university_towns = pd.DataFrame(df_dict)
    # print(university_towns)

    # swap columns
    cols = university_towns.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    university_towns = university_towns[cols]

    return university_towns
# get_list_of_university_towns()

def get_recessions():
    """
    get the whole duration of recessions
    :return: a tuple (recession start, recession end)
    """

    # format the DataFrame
    gdp_info = pd.read_excel('gdplev.xls', skiprows=7, skipfooter=0)
    gdp_info = gdp_info.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 7'])
    gdp_info = gdp_info.rename(columns={"Unnamed: 4": "Quarter", "Unnamed: 5": "GDP(current dollars)", "Unnamed: 6": "GDP(2009 dollars)"} )

    # get possible starts
    recession_starts = []
    for idx in range(len(gdp_info) - 2):
        if gdp_info.iloc[idx]['GDP(2009 dollars)'] > gdp_info.iloc[idx+1]['GDP(current dollars)'] > gdp_info.iloc[idx+2]['GDP(current dollars)']:
            recession_starts.append((idx+1, gdp_info.iloc[idx+1]['Quarter']))

    pop_list = []
    for jdx in range(len(recession_starts) - 1):
        if recession_starts[jdx][0] + 1 == recession_starts[jdx+1][0]:
            pop_list.append(jdx+1)

    final_recession_starts = []
    for kdx in range(len(recession_starts) - 1):
        if kdx not in pop_list:
            final_recession_starts.append(recession_starts[kdx][1])

    # get possbile ends
    recession_ends = []
    for idx in range(len(gdp_info) - 2):
        if gdp_info.iloc[idx]['GDP(2009 dollars)'] < gdp_info.iloc[idx+1]['GDP(current dollars)'] < gdp_info.iloc[idx+2]['GDP(current dollars)']:
            recession_ends.append((idx+2, gdp_info.iloc[idx+2]['Quarter']))

    pop_list = []
    for jdx in range(len(recession_ends) - 1):
        if recession_ends[jdx][0] + 1 == recession_ends[jdx+1][0]:
            pop_list.append(jdx+1)

    final_recession_ends = []
    for kdx in range(len(recession_ends) - 1):
        if kdx not in pop_list:
            final_recession_ends.append(recession_ends[kdx][1])
    # print(final_recession_starts, final_recession_ends)

    # Get the period
    min_dist = float('inf')
    for rec_start in final_recession_starts:
        for rec_end in final_recession_ends:
            dist = int(rec_end[:4]) - int(rec_start[:4])
            if dist < min_dist:
                min_dist = dist
                recession = (rec_start, rec_end)
    # print(recession)

    return(recession)
# get_recessions()

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    return(get_recessions()[0])
# get_recession_start()

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''

    return(get_recessions()[1])
# get_recession_end()

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''

    # Format the DataFrame
    gdp_info = pd.read_excel('gdplev.xls', skiprows=7, skipfooter=0)
    gdp_info = gdp_info.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 7'])
    gdp_info = gdp_info.rename(columns={"Unnamed: 4": "Quarter", "Unnamed: 5": "GDP(current dollars)", "Unnamed: 6": "GDP(2009 dollars)"} )
    gdp_info = gdp_info.set_index('Quarter')

    # Get lowest GDP
    min_gdp = float('inf')
    recession_bottom = None
    for idx in range(gdp_info.index.get_loc(get_recessions()[0]), gdp_info.index.get_loc(get_recessions()[1])):
        # print(gdp_info.iloc[idx]['GDP(current dollars)'])
        if gdp_info.iloc[idx]['GDP(current dollars)'] < min_gdp:
            min_gdp = gdp_info.iloc[idx]['GDP(current dollars)']
            recession_bottom = gdp_info.index[idx]
    # print(recession_bottom)

    return recession_bottom
# get_recession_bottom()

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    # restructure dataframe
    housing_data = pd.read_csv("City_Zhvi_AllHomes.csv")
    drop_start = housing_data.columns.get_loc('1996-04')
    drop_end = housing_data.columns.get_loc('2000-01')
    drop_list = ['RegionID', 'Metro', 'CountyName', 'SizeRank']
    for jdx in range(drop_start, drop_end):
        drop_list.append(housing_data.columns[jdx])
    housing_data = housing_data.drop(drop_list, axis=1)
    housing_data['State'] = [states[key] for key in housing_data['State']]
    housing_data = housing_data.set_index(['State', 'RegionName'])
    # print(housing_data)

    # Add quarters columns
    quarters_length = int(len(housing_data.columns) / 3)
    for idx in range(1, quarters_length + 1):
        housing_data[str(idx)] = housing_data[ [housing_data.columns[((idx * 3) - 3)], housing_data.columns[((idx * 3) - 2)], housing_data.columns[((idx * 3) - 1)]] ].mean(axis=1)
    housing_data[str(quarters_length + 1)] = housing_data[ [housing_data.columns[(((quarters_length + 1) * 3) - 3)], housing_data.columns[(((quarters_length + 1) * 3) - 2)], ] ].mean(axis=1)
    # print(housing_data)

    # Drop irrelevant months, rename quarters
    drop_start = housing_data.columns.get_loc('2000-01')
    drop_end = housing_data.columns.get_loc('1')
    drop_list = []
    for jdx in range(drop_start, drop_end):
        drop_list.append(housing_data.columns[jdx])
    housing_data = housing_data.drop(drop_list, axis=1)
    # print(len(housing_data.columns))
    quarter_columns = []
    for idx in range(0, len(housing_data.columns)):
        quarter_string = ''
        quarter_list = [1, 2, 3, 4]
        start_year = 2000 + math.floor(idx/4)
        quarter_string = str(start_year)+'q'+str(quarter_list[(idx%4)])
        quarter_columns.append(quarter_string)
    # print(quarter_columns)
    housing_data.columns = quarter_columns
    # print(housing_data.head(10))

    return(housing_data)
# convert_housing_data_to_quarters()

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    # prep work, trim down dataframes, get ready for merge
    recession_start = get_recession_start()
    recession_bottom = get_recession_bottom()
    housing_data = convert_housing_data_to_quarters()
    start_idx = housing_data.columns.get_loc(recession_start)
    bottom_idx = housing_data.columns.get_loc(recession_bottom)
    reccession_df = housing_data[ [housing_data.columns[start_idx], housing_data.columns[bottom_idx] ]]
    reccession_df = reccession_df.reset_index()
    unitowns_df = get_list_of_university_towns()
    unitowns_df['UniTown'] = True

    # separate uni towns from non-uni towns
    # print(reccession_df, unitowns_df)
    merge_one = (pd.merge(reccession_df, unitowns_df, how='outer', left_on=['State', 'RegionName'], right_on=['State', 'RegionName']))
    merge_one["UniTown"].fillna(False, inplace = True)
    merge_one = merge_one.dropna()
    # print(merge_one)

    uni_towns = merge_one[merge_one['UniTown'] == True]
    uni_towns = uni_towns.set_index(['State', 'RegionName'])
    uni_towns = uni_towns.drop(columns=['UniTown'])
    uni_towns['Ratio'] = uni_towns[recession_bottom] - uni_towns[recession_start]

    non_uni_towns = merge_one[merge_one['UniTown'] == False]
    non_uni_towns = non_uni_towns.set_index(['State', 'RegionName'])
    non_uni_towns = non_uni_towns.drop(columns=['UniTown'])
    non_uni_towns['Ratio'] = non_uni_towns[recession_bottom] - non_uni_towns[recession_start]

    # print(uni_towns)
    # print(non_uni_towns)

    # get test results
    t,p = ttest_ind(uni_towns['Ratio'], non_uni_towns['Ratio'])
    different = True if p<0.01 else False
    better = "university town" if uni_towns['Ratio'].mean() > non_uni_towns['Ratio'].mean() else "non-university town"

    return (different, p, better)
run_ttest()
