import pandas as pd

census_df = pd.read_csv('census.csv')
print(census_df.head())

def q5():
    df = census_df[census_df['SUMLEV'] == 50]
    print(df)

    count_dict = {}
    for index, row in df.iterrows():
        if row['STNAME'] not in count_dict:
            count_dict[row['STNAME']] = 1
        else:
            count_dict[row['STNAME']] += 1


    inverse = [(value, key) for key, value in count_dict.items()]
    print(max(inverse)[1])
    print(inverse)
    # print(count_dict)

# q1()


def q6():
    df = census_df[census_df['SUMLEV'] == 50]
    # print(df)
    # df = df.set_index(['STNAME', 'CENSUS2010POP'])
    # print(df.head())
    population_dict = {}
    df = df.sort_values(by=['CENSUS2010POP'], ascending = False)
    for index, row in df.iterrows():
        if row['STNAME'] not in population_dict:
            population_dict[row['STNAME']] = [row['CENSUS2010POP'], 1]
        else:
            if population_dict[row['STNAME']][1] <= 2:
                population_dict[row['STNAME']][0] += row['CENSUS2010POP']
                population_dict[row['STNAME']][1] += 1

    print(population_dict)

    largest_populations = []
    for key, value in population_dict.items():
        largest_populations.append(value[0])

    # print(largest_populations.sort(reverse = True))
    print(largest_populations)


    # population_dict = {}
    #
    # local_count = 3
    #
    #
    # # for index, row in df.iterrows():
        # if row['STNAME'] in population_dict:
        #     population_dict[row['STNAME']] = row['CENSUS2010POP']
        #     local_count = 3
    # #     else:
    # #         population_dict[row['STNAME']] += row['CENSUS2010POP']
    # #         local_count -= 1
    # #
    # #     # largest_populations.append(row['CENSUS2010POP'])
    # #     largest_populations.append(row['STNAME'])
    #
    # print(largest_populations[:3])
    # return largest_populations[:3]

q6()


def q7():
    df = census_df[census_df['SUMLEV'] == 50]
    print(df)

    largest_change = 0
    for index, row in df.iterrows():
        county_populations = [row['POPESTIMATE2010'], row['POPESTIMATE2011'],row['POPESTIMATE2012'],row['POPESTIMATE2013'],row['POPESTIMATE2014'],row['POPESTIMATE2015']]
        current_change = max(county_populations) - min(county_populations)
        if current_change > largest_change:
            largest_change = current_change
            target_county = row['CTYNAME']

    print(largest_change, target_county)


        # print(row['STNAME'], row['CENSUS2010POP'])
        # largest_populations.append(row['CENSUS2010POP'])


def q8():
    df = census_df[census_df['SUMLEV'] == 50]
    target_counties = df.where(df['REGION'] < 3)
    target_counties = target_counties.dropna()

    county_names = []
    state_names = []
    indexes = []
    for index, row in target_counties.iterrows():
        if row['POPESTIMATE2015'] > row['POPESTIMATE2014'] and "Washington" in row['CTYNAME']:
            county_names.append(row['CTYNAME'])
            state_names.append(row['STNAME'])
            indexes.append(index)

            print(row['CTYNAME'], row['STNAME'], index)

    print(indexes)

    data_tuples = list(zip(state_names, county_names))
    ser = pd.DataFrame(data_tuples, columns=['STNAME','CTYNAME'], index = indexes)

    print(ser)
    return ser


    # print(target_counties)

# q8()
