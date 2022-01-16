# Name: data_cleaning.py
# Description: A module that contains all the one-off scripts created to clean and parse data

import pandas as pd
import csv

"""

 Scripts to create 'covid-data.csv' from the raw OWID data

"""


# Function slices the last data point of each country in the dataframe and stores the information in a list
def prune_data():

    dataframe = pd.read_csv("sourcedata/owid-covid-data.csv")

    # Keeps track of when the country id switches
    prev_country = dataframe.iloc[0, 0]

    country_list = []

    # Iterate over all the rows in the dataframe, and pull the last captured datapoint for each country
    for i in range(len(dataframe)-1):

        # Pulls the country id from the current index
        current_country = dataframe.iloc[i, 0]

        # If the program has reached a new country id, store the information from the final
        # instance of the previous country
        if current_country != prev_country:

            # Replace the old country id with the new one
            prev_country = current_country

            country_list.append(dataframe.iloc[i-1, :])

    return country_list


# Function takes the list of data objects and writes a new csv file with the desired categories
def create_csv(data_list):
    with open('covid-data.csv', 'w', ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['iso_code', 'continent', 'location', 'date', 'total_cases', 'total_deaths',
                         'total_cases_per_million', 'reproduction_rate', 'population', 'population_density',
                         'gdp_per_capita', 'life_expectancy'])
        for data in data_list:
            writer.writerow([data.iso_code, data.continent, data.location, data.date, data.total_cases,
                             data.total_deaths, data.total_cases_per_million, data.reproduction_rate,
                             data.population, data.population_density, data.gdp_per_capita, data.life_expectancy])


"""

 Script to create 'iso-codes.csv'

"""


# Create a csv file containing iso codes and their respective countries, using the info in 'covid-data.csv'
def create_iso_codes_file():

    # Create a dataframe using the data in the file
    dataframe = pd.read_csv('covid_data.csv')

    # A list of all the countries
    countries_list = []

    # A list of all the iso codes
    iso_list = []

    # Iterate over all the items in the "location" column and store all new values in the countries list
    for country in dataframe['location'].values:
        if country not in countries_list:
            countries_list.append(country)

    # Iterate over all the items in the "iso_code" column and store all new values in the iso_list
    for code in dataframe['iso_code'].values:
        if code not in iso_list:
            iso_list.append(code)

    # Open and write a csv file containing iso codes in the first column, and locations (i.e. countries) in the second
    with open('iso-codes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['location', 'iso_code'])

        for code in range(len(iso_list)):
            writer.writerow([countries_list[code], iso_list[code]])


"""

 Scripts to add 'deaths_per_million' column to 'panepi-data.csv'

"""


# Calculate deaths per million using total death and population data in a csv file, and create a new csv file
# with the additional deaths per million column
def add_dpm():

    # Create a dataframe
    df = pd.read_csv('datafiles/panepi-data.csv')

    # Calculate deaths per million, and create a new deaths per million column
    df['deaths_per_million'] = df['est_total_deaths'] / (df['population']/1000000)

    # Create a new csv file using the updated dataframe
    with open('panepi-data.csv', 'w') as csvfile:

        # Create a writer object
        writer = csv.writer(csvfile)

        # Write the first row of data (column headers) into the csv file
        writer.writerow(list(df.columns))

        # Iterate over the length of the dataframe (number of rows), writing each row of data into the csv file one
        # at a time
        for i in range(len(df)):
            # Slice the dataframe by index and store that row's data
            row = df.iloc[i]

            # Write the row data
            writer.writerow([row.infection, row.continent, row.duration_in_years, row.est_total_deaths, row.population, row.deaths_per_million])

