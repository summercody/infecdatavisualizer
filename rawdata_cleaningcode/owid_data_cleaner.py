# Name: owid_data_cleaner.py
# Single-use program to modify the COVID-19 data provided by "Our World in Data", and export a re-formatted csv file.

import pandas as pd
import csv

# Read the csv data and create a dataframe
covid_data = pd.read_csv("owid-covid-data.csv")

# Keeps track of the number of rows to create a range that can be iterated over
LOCATION_LIST_LEN = covid_data['iso_code'].count()


# Function slices the last data point of each country in the dataframe and stores the information in a list
def prune_data(dataframe):

    # Keeps track of when the country id switches
    prev_country = dataframe.iloc[0, 0]

    country_list = []

    # Iterate over all the rows in the dataframe, and pull the last captured datapoint for each country
    for i in range(LOCATION_LIST_LEN - 1):

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
    with open('../covid-data.csv', 'w', ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['iso_code', 'continent', 'location', 'date', 'total_cases', 'total_deaths',
                         'total_cases_per_million', 'reproduction_rate', 'population', 'population_density',
                         'gdp_per_capita', 'life_expectancy'])
        for data in data_list:
            writer.writerow([data.iso_code, data.continent, data.location, data.date, data.total_cases,
                             data.total_deaths, data.total_cases_per_million, data.reproduction_rate,
                             data.population, data.population_density, data.gdp_per_capita, data.life_expectancy])


# Store the list of sliced data objects
pruned_data = prune_data(covid_data)

# Write the new csv file
create_csv(pruned_data)
