# Name: dpm_calculator.py
# Description: One-off program to add a "deaths_per_million" column to panepi-data.csv
# NB: This program was used on an old version of 'panepi-data.csv', which did not have a "deaths per million" column.
# The current 'panepi-data.csv' file was created using this program, before being moved to a different directory.

import pandas as pd
import csv

FILE = 'panepi-data.csv'


# Calculate deaths per million using total death and population data in a csv file, and create a new csv file
# with the additional deaths per million column
def add_dpm(FILENAME):

    # Create a dataframe
    df = pd.read_csv(FILENAME)

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


# Run program
add_dpm(FILE)


