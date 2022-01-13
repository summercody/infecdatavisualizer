import pandas as pd
import csv

COVID_19 = 'covid-data.csv'


def create_iso_codes_file():
    dataframe = pd.read_csv(COVID_19)
    countries_list = []
    iso_list = []

    for country in dataframe['location'].values:
        if country not in countries_list:
            countries_list.append(country)

    for code in dataframe['iso_code'].values:
        if code not in iso_list:
            iso_list.append(code)

    with open('iso-codes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['iso_code', 'location'])

        for code in range(len(iso_list)):
            writer.writerow([iso_list[code], countries_list[code]])