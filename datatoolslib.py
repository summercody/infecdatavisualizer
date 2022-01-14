"""
GENERAL INFORMATION

Name: datatoolslib.py

Description: A small library of functions that can be called to get quick info about the datasets each visualizer
is referencing.

NB: The file 'iso-codes.csv' must be in the same directory as datatoolslib.py in order for "create_iso_dict" and
"find_iso_code" to run.

Testing: Example function calls are provided at the bottom to test code functionality.

"""


import pandas as pd


""" For covid_visualizer.py """


# Reads iso-codes.csv and creates a dictionary of all iso codes and their associated countries
def create_iso_dict():

    # Create a dataframe using a csv file containing iso codes and their countries
    iso_info = pd.read_csv('iso-codes.csv')

    countries_list = []  # List of countries
    iso_list = []  # List of iso codes
    iso_dict = {}  # A dictionary that will contain iso code information with country names as keys

    # Iterate over the countries in the dataframe and store them in the country list
    for country in iso_info['location'].values:
        if country not in countries_list:
            countries_list.append(country)

    # Iterate over the iso codes in the dataframe and store them in the iso list
    for code in iso_info['iso_code'].values:
        if code not in iso_list:
            iso_list.append(code)

    # Iterate over the iso_list and countries_list indices, find their corresponding values, and store them as
    # values and keys in the iso dictionary
    for code in range(len(iso_list)):
        key = countries_list[code]
        iso_dict[key] = iso_list[code]

    # Return the dictionary
    return iso_dict


# Takes a string of a country name, and outputs its iso code
def find_iso_code(country_string):

    # Create the dictionary and store it in a variable
    country_dictionary = create_iso_dict()

    # Run a search in the dictionary using the string as a key, and print the result to the console
    print(country_dictionary[country_string])


""" For All Modules """


# Displays a summary of the information provided by a given datafile. Takes a solo file input,
# a file input + the string 'headers', or a file input + the name of a column as a string
def show_available_info(datafile, data_type=None):

    # Create a dataframe
    dataframe = pd.read_csv(datafile)

    # If the user has only input a filename, print the entire dataframe and return the function
    if data_type is None:
        print(dataframe)
        return

    # If the user has requested only the column names from the dataframe, print the column values as a list and return
    if data_type == 'headers':
        print(dataframe.columns.values)
        return

    # If the user has input a filename and a column name as a string, print the column's values as a list
    print(dataframe[data_type].values)


""" Test Code """

# Data files
COVID_19 = 'covid-data.csv'

# Test 1: Prints 'DZA' to the console
# find_iso_code('Algeria')

# Test 2: Prints all column names from 'covid-data.csv' as a list
# show_available_info(COVID_19, 'headers')
