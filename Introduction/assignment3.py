import pandas as pd
import numpy as np

def answer_one():
    """
    week3 assignment q1
    """
    # load the excel file
    df = pd.read_excel('Energy Indicators.xls', skiprows=17, skipfooter=38)
    # print(df)

    # drop the unuseful columns
    energy = (df[df.columns[2:6]])

    # rename columns
    energy = energy.rename(columns={'Unnamed: 2': "Country", 'Petajoules': "Energy Supply", 'Gigajoules': "Energy Supply per Capita", "%": "% Renewable"})
    # print(energy)


    # multiply petajoules values
    energy['Energy Supply'] = energy['Energy Supply'].mul(1000000)
    # print(energy)

    # replace '...'
    energy_columns = ['Energy Supply', 'Energy Supply per Capita']
    replace_index = []

    for column in energy_columns:
        replace_targets = energy[column].str.startswith("...")
        for index, value in replace_targets.iteritems():
            # print(index, value)
            if value == True:
                replace_index.append((column, index))
    # print(replace_index)

    for tuple in replace_index:
        energy.replace(energy[tuple[0]][tuple[1]], np.nan, inplace=True)


    # Rename the following list of countries (for use in later questions):
    energy.replace({"Republic of Korea": "South Korea", "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"}, regex=True, inplace=True)

    # There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,

    energy['Country'].replace('\d', '', regex=True, inplace=True)
    energy['Country'].replace('\s*\([^)]+\)', '', regex=True, inplace=True)


    # Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP = GDP.rename(columns={'Country Name': "Country"})
    # GDP = GDP.drop(columns=['1960',
    #    '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969',
    #    '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978',
    #    '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
    #    '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996',
    #    '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005'])
    # # print(GDP)

    GDP = GDP.drop(['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005'], axis = 1)

    # Make sure to skip the header, and rename the following list of countries:
    GDP.replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"}, regex=True, inplace=True)

    # print(GDP.columns)





    # Finally, load the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this **ScimEn**.

    ScimEn = (pd.read_excel('scimagojr-3.xlsx')).head(15)
    # print(ScimEn)

    # Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

    # print()
    merge_one = (pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country'))
    final_merge = pd.merge(merge_one, GDP, how='inner', left_on='Country', right_on='Country')
    final_merge = final_merge.set_index('Country')

    final_merge = final_merge.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    # print(final_merge)

    # # answer two
    # ScimEn2 = pd.read_excel('scimagojr-3.xlsx')
    # outer = pd.merge(ScimEn2, pd.merge(GDP, energy, how='outer', on='Country'), how='outer', on='Country')
    # inner = pd.merge(ScimEn2, pd.merge(GDP, energy, how='inner', on='Country'), how='inner', on='Country')
    # answer_two = len(outer) - len(inner)
    # print(answer_two) #156

    # print(energy.head(20))
    return(final_merge)

# answer_one()



def answer_three():
    """
    week3 assignment q3
    """
    Top15 = answer_one()
    # print(Top15)
    target_columns = []
    for year in range(2006, 2016):
        target_columns.append(str(year))
    # print(target_columns)
    Top15['Average'] = Top15[target_columns].mean(axis=1)
    # avgGDP = avgGDP.sort_values(inplace=True, ascending=False)
    # print(avgGDP.sort_values(by = '0',inplace=True, ascending=False))
    avgGDP = Top15.sort_values(by ='Average', ascending=False)

    # print(avgGDP['Average'])
    return(avgGDP['Average'])

# answer_three()


def answer_four():
    """
    By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
    """
    Top15 = answer_one()
    rank_six = answer_three().index[5]
    gdp_diff = Top15.loc[rank_six]['2015'] - Top15.loc[rank_six]['2006']
    # print(gdp_diff)
    return gdp_diff

# answer_four()


def answer_five():
    """
    What is the mean `Energy Supply per Capita`?
    """
    Top15 = answer_one()
    # rank_six = answer_three().index[5]
    target_columns = []
    for year in range(2006, 2016):
        target_columns.append(str(year))
    # espc_mean = Top15.loc[rank_six][target_columns].mean()

    total = 0
    for column in target_columns:
        espc_mean = Top15[column].mean()
        total += espc_mean

    target_mean = total/10

    return target_mean

answer_five()

def answer_six():
    """
    What country has the maximum % Renewable and what is the percentage?
    This function should return a tuple with the name of the country and the percentage.
    """
    Top15 = answer_one()
    # print(Top15.columns)
    max_renew = Top15.sort_values(by ='% Renewable', ascending=False)
    target_tuple = (max_renew.index[0], Top15.loc[max_renew.index[0]]['% Renewable'])
    # print(target_tuple)
    return target_tuple
# answer_six()

def answer_seven():
    """
    Create a new column that is the ratio of Self-Citations to Total Citations.
    What is the maximum value for this new column, and what country has the highest ratio?
    *This function should return a tuple with the name of the country and the ratio.*
    """
    Top15 = answer_one()
    # print(Top15.columns)
    Top15['Self-citations Ratio'] = Top15['Self-citations'] / Top15['Citations']
    # print(Top15['Self-citations Ratio'])
    target_df = Top15.sort_values(by ='Self-citations Ratio', ascending=False)
    target_tuple = (target_df.index[0], Top15.loc[target_df.index[0]]['Self-citations Ratio'])
    # print(target_tuple)

    return target_tuple
# answer_seven()

def answer_eight():
    """
    Create a column that estimates the population using Energy Supply and Energy Supply per capita.
    What is the third most populous country according to this estimate?

    *This function should return a single string value.*
    """

    Top15 = answer_one()
    Top15['Est. Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    # print(Top15['Self-citations Ratio'])
    target_df = Top15.sort_values(by ='Est. Population', ascending=False)
    # print(target_df)
    target_tuple = (target_df.index[2], Top15.loc[target_df.index[2]]['Est. Population'])
    print(target_tuple[0])

    return target_tuple[0]
answer_eight()

def answer_nine():
    """
    Create a column that estimates the number of citable documents per person.

    What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).

    *This function should return a single number.*

    *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*
    """
    Top15 = answer_one()
    print(Top15.columns)
    Top15['Est. Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable per capita'] = Top15['Citable documents'] / Top15['Est. Population']
    target_num = Top15['Energy Supply per Capita'].corr(Top15['Citable per capita'])
    print(target_num)

    return target_num
# answer_nine()

def plot9():
    """
    *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*
    """
    import matplotlib.pyplot as plt
    # %matplotlib inline

    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    plt.show()
# plot9()

def answer_ten():
    """
    Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

    *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*
    """

    Top15 = answer_one()
    target_df = Top15.sort_values(by ='% Renewable', ascending=False)
    target_tuple = (target_df.index[8], Top15.loc[target_df.index[8]]['% Renewable'])
    print(target_tuple)
    Top15['HighRenew'] = 0
    for idx in range(15):
        if Top15.loc[Top15.index[idx]]['% Renewable'] > target_tuple[1]:
            # Top15.loc[Top15.index[idx]]['HighRenew'] = 1
            Top15.at[Top15.index[idx], 'HighRenew'] = 1
    print(Top15['HighRenew'])

    return(Top15['HighRenew'])
# answer_ten()


# def answer_eleven():
#     """
#     Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
#
#     *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*
#     """
#     Top15 = answer_one()
#     Top15['Est. Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
#
#     ContinentDict  = {'China':'Asia',
#                       'United States':'North America',
#                       'Japan':'Asia',
#                       'United Kingdom':'Europe',
#                       'Russian Federation':'Europe',
#                       'Canada':'North America',
#                       'Germany':'Europe',
#                       'India':'Asia',
#                       'France':'Europe',
#                       'South Korea':'Asia',
#                       'Italy':'Europe',
#                       'Spain':'Europe',
#                       'Iran':'Asia',
#                       'Australia':'Australia',
#                       'Brazil':'South America'}
#
#     # make a reverse_dict
#     reverse_dict = {}
#     for key, value in ContinentDict.items():
#         print(key, value)
#         if value not in reverse_dict:
#             reverse_dict[value] = [key]
#         else:
#             reverse_dict[value].append(key)
#     print(reverse_dict)
#
#     # make an empty dataframe
#     indexes = ['Asia', 'Australia', 'Europe', 'North America', 'South America']
#     columns = ['size', 'sum', 'mean', 'std']
#     target_df = pd.DataFrame(index = indexes, columns = columns)
#     print(target_df)
#
#     # calculate size
#     size_list = []
#     for continent in indexes:
#         size_list.append(float(len(reverse_dict[continent])))
#     print(size_list)
#
#     # calculate sum of population
#     sum_list = []
#     for continent in indexes:
#         continent_sum = 0
#         for country in reverse_dict[continent]:
#             continent_sum += Top15.loc[country]['Est. Population']
#         sum_list.append(float(int(continent_sum)))
#     print(sum_list)
#
#     # calc mean
#     mean_list = []
#     for idx in range(len(size_list)):
#         continent_mean = int(float(sum_list[idx]) / float(size_list[idx]))
#         mean_list.append(float(continent_mean))
#     print(mean_list)
#
#     # calc std

    # return "ANSWER"

# answer_eleven()


def answer_eleven():
    """
    Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.

    *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*
    """
    Top15 = answer_one().reset_index()
    print(Top15)
    Top15['Est. Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    ContinentDict  = {'China':'Asia',
                      'United States':'North America',
                      'Japan':'Asia',
                      'United Kingdom':'Europe',
                      'Russian Federation':'Europe',
                      'Canada':'North America',
                      'Germany':'Europe',
                      'India':'Asia',
                      'France':'Europe',
                      'South Korea':'Asia',
                      'Italy':'Europe',
                      'Spain':'Europe',
                      'Iran':'Asia',
                      'Australia':'Australia',
                      'Brazil':'South America'}
    # indexes = ['Asia', 'Australia', 'Europe', 'North America', 'South America']
    columns = ['size', 'sum', 'mean', 'std']

    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]

    df = Top15.set_index('Continent').groupby(level = 0)['Est. Population'].agg({'size':np.size, 'sum':np.sum, 'mean':np.mean, 'std':np.std})

    # print(df)
    return df[columns]
# answer_eleven()

def answer_twelve():
    """
    Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?

    *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*
    """
    Top15 = answer_one().reset_index()
    ContinentDict  = {'China':'Asia',
                      'United States':'North America',
                      'Japan':'Asia',
                      'United Kingdom':'Europe',
                      'Russian Federation':'Europe',
                      'Canada':'North America',
                      'Germany':'Europe',
                      'India':'Asia',
                      'France':'Europe',
                      'South Korea':'Asia',
                      'Italy':'Europe',
                      'Spain':'Europe',
                      'Iran':'Asia',
                      'Australia':'Australia',
                      'Brazil':'South America'}
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Top15['Cut by five']= pd.cut(Top15['% Renewable'], 5)
    target_series = Top15.groupby(['Continent','Cut by five']).size()
    # print(target_series)
    return target_series

# answer_twelve()


def answer_thirteen():
    """
    Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.

    e.g. 317615384.61538464 -> 317,615,384.61538464

    *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*
    """
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['PopEst'].apply(lambda x: '{:,}'.format(x))
    print(Top15['PopEst'])

    return Top15['PopEst']
# answer_thirteen()


def plot_optional():
    import matplotlib.pyplot as plt
    # %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'],
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")
