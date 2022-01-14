"""
GENERAL INFORMATION

Name: covid_visualizer.py

Description: Reads cleaned COVID-19 data from "Our World in Data", and provides different ways to visualize the data
graphically.

NB: Each function can visualize country-based data about other infections, as long as the csv file is formatted
with iso codes in the first column. The example file, 'covid-data.csv', is formatted in this manner.

Testing: Example function calls are provided at the bottom to test code functionality.

"""


import pandas as pd
import matplotlib.pyplot as plt
import datatoolslib as dtl  # See "Test Code" at the bottom for usage


# Compares a piece of statistical data about COVID between up to three different locations
def comp_infec_between_countries(datafile, stat, iso_code1, iso_code2=None, iso_code3=None):

    # Create a dataframe
    infec_data = pd.read_csv(datafile)

    # Copy dataframe to avoid permanent manipulations
    data_copy = infec_data.copy()

    # Set the index to 'iso_code' to make user query easier, and to make the codes display on the graph
    data_copy.set_index('iso_code', inplace=True)

    # If only one iso code has been entered, slice the dataframe by that code
    if iso_code3 is iso_code2 is None:
        country_comp = data_copy.loc[[iso_code1]]

    # If two iso codes have been entered, slice the dataframe by those codes
    elif iso_code3 is None:
        country_comp = data_copy.loc[[iso_code1, iso_code2]]

    # If three iso codes have been entered, slice the dataframe by those codes
    else:
        country_comp = data_copy.loc[[iso_code1, iso_code2, iso_code3]]

    # Plot the collection of country data with the y-axis being the user's chosen statistic
    country_comp.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    # Show the graph
    plt.show()


# Compares a piece of statistical data about COVID across all countries. Allows the user to view a subset of
# the first few countries
def infec_stat_all_countries(datafile, sample_size, stat):

    # Create a dataframe
    infec_data = pd.read_csv(datafile)

    # Take the first few rows of data
    subsample = infec_data.head(sample_size)

    # Set the index to 'iso_code' to make the codes display on the graph
    subsample.set_index('iso_code', inplace=True)

    # Plot the graph with the y-axis being the user's chosen statistic
    subsample.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    # Show the graph
    plt.show()


""" Test Code """

# Data files
COVID_19 = 'covid-data.csv'

# Test 1: Testing the functionality of datatoolslib functions outside the library. Prints 'USA' to the console.
# dtl.find_iso_code('United States')

# Test 2: Displays a bar graph of total COVID-19 cases per million in the United States and Canada.
# comp_infec_between_countries(COVID_19, 'total_cases_per_million', 'USA', 'CAN')

# Test 3: Displays a bar graph of total COVID-19 cases per million in the first 50 countries listed in the CSV file
# infec_stat_all_countries(COVID_19, 50, 'total_cases_per_million')


