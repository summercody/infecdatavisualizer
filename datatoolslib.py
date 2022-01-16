"""
GENERAL INFORMATION

Name: datatoolslib.py

Description: A small library of functions that can be called to get quick info about the datasets each visualizer
is referencing.

Testing: Example function calls are provided at the bottom to test code functionality.

"""


import pandas as pd


""" For Single-Infection Visualizers """


# Reads iso-codes.csv and creates a dictionary of all iso codes and their associated countries
def create_iso_dict():

    # Create a dataframe from a file with iso codes and their countries
    iso_info = pd.read_csv('datafiles/iso-codes.csv')

    # Create a dictionary using the locations as keys
    iso_dict = iso_info.set_index('location')['iso_code'].to_dict()

    # Return the dictionary
    return iso_dict


# Takes a string of a country name, and outputs its iso code
def find_iso_code(country_string):

    # Create the dictionary and store it in a variable
    country_dictionary = create_iso_dict()

    if country_string not in country_dictionary.keys():
        print("\nOops! That's not a country in the iso lookup.")
        return

    # Run a search in the dictionary using the string as a key, and print the result to the console
    print("\n" + country_dictionary[country_string])


""" For All Modules """


# Displays a summary of the information provided by a given datafile. Takes a solo file input,
# a file input + the string 'headers', or a file input + the name of a column as a string
def available_info(dataframe, data_type=None):

    # If the user has only input a filename, print the entire dataframe and return the function
    if data_type is None:
        return dataframe

    # If the user has requested only the column names from the dataframe, print the column values as a list and return
    if data_type == 'headers':
        return dataframe.columns.values

    # If the user has input a filename and a column name as a string, print the column's values as a list
    data = dataframe[data_type]
    data_values = data.values

    if type(data_values[0]) is str:
        no_dup = data.drop_duplicates()
        return no_dup.values

    return data_values


""" Test Code """

# Data files
# COVID_19 = 'datafiles/covid-data.csv'

# Test 1: Prints 'DZA' to the console
# find_iso_code('Algeria')

# Test 2: Prints all the available continents from 'covid-data.csv' as a list
# covid_df = pd.read_csv(COVID_19)
# continent_info = available_info(covid_df, 'continent')
# print(continent_info)
