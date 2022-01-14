# Name: iso_codes_doc_creator.py
# Description: A one-off program to create a csv file containing iso codes and their respective countries, using the
# info in 'covid-data.csv'

import pandas as pd
import csv

COVID_19 = 'covid-data.csv'


def create_iso_codes_file():

    # Create a dataframe using the data in the file
    dataframe = pd.read_csv(COVID_19)

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
        writer.writerow(['iso_code', 'location'])

        for code in range(len(iso_list)):
            writer.writerow([iso_list[code], countries_list[code]])