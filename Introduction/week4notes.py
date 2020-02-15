import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt

# Distributions in Pandas

def distribution_pandas():
    """
    # Distributions in Pandas
    """
    print(np.random.binomial(1, 0.5)) #(number of coins, chance of 0)
    print(np.random.binomial(1000, 0.5)/1000)

    print()
    chance_of_tornado = 0.01/100
    print(np.random.binomial(100000, chance_of_tornado))

    print()
    chance_of_tornado = 0.01

    tornado_events = np.random.binomial(1, chance_of_tornado, 1000000) #n, p, size

    two_days_in_a_row = 0
    for j in range(1,len(tornado_events)-1):
        if tornado_events[j]==1 and tornado_events[j-1]==1:
            two_days_in_a_row+=1

    print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))

    print()
    print(np.random.uniform(0, 1))

    print()
    print(np.random.normal(0.75))

    print()
    distribution = np.random.normal(0.75,size=1000)
    print(distribution)

    print()
    print(np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution)))

    print()
    print(np.std(distribution))

    print()
    print()
    print('import scipy.stats as stats')
    print()
    print()
    print(stats.kurtosis(distribution))

    print()
    print(stats.skew(distribution))

    print()
    chi_squared_df2 = np.random.chisquare(2, size=10000)
    print(chi_squared_df2)
    print(stats.skew(chi_squared_df2))

    print()
    chi_squared_df5 = np.random.chisquare(5, size=10000)
    print(chi_squared_df5)
    print(stats.skew(chi_squared_df5))


    # plot
    output = plt.hist([chi_squared_df2,chi_squared_df5], bins=50, histtype='step',
                  label=['2 degrees of freedom','5 degrees of freedom'])
    plt.legend(loc='upper right')
    plt.show()


# distribution_pandas()


# Hypothesis Testing

def hypothesis_testing():
    """
    Hypothesis testing
    """
    df = pd.read_csv('grades.csv')
    print(df.head())
    print(len(df))
    early = df[df['assignment1_submission'] <= '2015-12-31']
    late = df[df['assignment1_submission'] > '2015-12-31']
    print(early.mean())
    print(late.mean())

    print()
    print(stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade']))
    # pvalue: compare that to the threashold

    print()
    print(stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade']))

    print()
    print(stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade']))
hypothesis_testing()
