# Name: datatoolslib.py
# Description: A small library of functions that can be called to get quick info about each dataset, and any information
# needed to run the visualization functions.

import pandas as pd


""" For covid_visualizer.py """


# Reads iso-codes.csv and creates a dictionary of all iso codes and their associated countries
def create_iso_dict():
    dataframe = pd.read_csv('iso-codes.csv')
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


# Function that takes a string of a country name, and outputs its iso code
def find_iso_code(country_string):
    country_dictionary = create_iso_dict()
    print(country_dictionary[country_string])


""" For All Modules """


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


""" Test Code """

# Data files
COVID_19 = 'covid-data.csv'

# find_iso_code('Algeria')

# show_available_info(COVID_19, 'headers')
