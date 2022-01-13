# Name: covidvisualizer.py
# Reads cleaned data from "Our World in Data" about COVID-19, and provides different ways to visualize the data

import pandas as pd
import matplotlib.pyplot as plt


# Data files
COVID_19 = 'covid-data.csv'
CODES = 'iso-codes.csv'


# Reads iso-codes.csv and creates a dictionary of all iso codes and their associated countries
def create_iso_dict():
    dataframe = pd.read_csv(CODES)
    countries_list = []
    iso_list = []
    iso_dict = {}

    for country in dataframe['location'].values:
        if country not in countries_list:
            countries_list.append(country)

    for code in dataframe['iso_code'].values:
        if code not in iso_list:
            iso_list.append(code)

    for code in range(len(iso_list)):
        key = countries_list[code]
        iso_dict[key] = iso_list[code]

    return iso_dict


""" General Tools """


# Function that takes a string of a country name, and outputs its iso code
def find_iso_code(country_string):

    country_dictionary = create_iso_dict()
    print(country_dictionary[country_string])


# Displays a summary of the information provided by a given datafile. Takes a solo file input,
# a file input + the string 'headers', and a file input + the name of column as a string.
def show_available_info(datafile, data_type=None):
    dataframe = pd.read_csv(datafile)

    if data_type is None:
        print(dataframe)
        return

    if data_type == 'headers':
        print(dataframe.columns.values)
        return

    print(dataframe[data_type].values)


""" COVID Visualizers """


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
    virus_data = pd.read_csv(datafile)
    subsample = virus_data.head(sample_size)
    subsample.set_index('iso_code', inplace=True)

    subsample.plot(kind='bar', y=stat)

    y_axis_label = stat.title().replace("_", " ")
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    plt.show()


""" Test Code """

# find_iso_code('Algeria')

# show_available_info(COVID_19, 'headers')

# comp_infec_between_countries(COVID_19, 'total_cases', 'DZA', 'ARM')

# infec_stat_all_countries(COVID_19, 50, 'total_cases_per_million')


