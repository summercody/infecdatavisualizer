# One-off program to add a "deaths_per_million" column to panepi-data.csv

import pandas as pd
import csv

FILE = 'panepi-data.csv'

df = pd.read_csv(FILE)

df['deaths_per_million'] = df['est_total_deaths'] / (df['population']/1000000)


with open('panepi-data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(list(df.columns))

    for i in range(len(df)):
        x = df.iloc[i]
        writer.writerow([x.infection, x.continent, x.duration_in_years, x.est_total_deaths, x.population, x.deaths_per_million])




