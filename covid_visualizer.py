# Name: covid_visualizer.py
# Reads cleaned COVID-19 data from "Our World in Data", and provides different ways to visualize the data graphically.

# NB: Each function can visualize country-based data about other infections, as long as the csv file is formatted
# with iso codes in the first column. The example file, covid-data.csv, is formatted in this manner.

import pandas as pd
import matplotlib.pyplot as plt
import datatoolslib as dtl  # See "Test Code" at the bottom for usage


# Compares a piece of statistical data about COVID between up to three different locations
def comp_infec_between_countries(datafile, stat, iso_code1, iso_code2=None, iso_code3=None):
    infec_data = pd.read_csv(datafile)

    data_copy = infec_data.copy()

    data_copy.set_index('iso_code', inplace=True)

    if iso_code3 is iso_code2 is None:
        country_comp = data_copy.loc[[iso_code1]]
    elif iso_code3 is None:
        country_comp = data_copy.loc[[iso_code1, iso_code2]]
    else:
        country_comp = data_copy.loc[[iso_code1, iso_code2, iso_code3]]

    country_comp.plot(kind='bar', y=stat)
    y_axis_label = stat.title().replace("_", " ")
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    plt.show()


# Compares a piece of statistical data about COVID across all countries. Allows the user to view a subset of
# countries
def infec_stat_all_countries(datafile, sample_size, stat):
    infec_data = pd.read_csv(datafile)
    subsample = infec_data.head(sample_size)
    subsample.set_index('iso_code', inplace=True)

    subsample.plot(kind='bar', y=stat)

    y_axis_label = stat.title().replace("_", " ")
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    plt.show()


""" Test Code """

# Data files
COVID_19 = 'covid-data.csv'

# Test 1: Testing the functionality of datatoolslib functions outside of the library. Prints 'DZA' to the console.
# dtl.find_iso_code('United States')

# Test 2: Displays a bar graph of total COVID-19 cases per million in the United States and Canada.
# comp_infec_between_countries(COVID_19, 'total_cases_per_million', 'USA', 'CAN')

# Test 3: Displays a bar graph of total COVID-19 cases per million in the first 50 countries listed in the CSV file
# infec_stat_all_countries(COVID_19, 50, 'total_cases_per_million')


