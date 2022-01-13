import pandas as pd
import csv

FILE = 'covid-data.csv'

df = pd.read_csv(FILE)


"""
df['new_column'] = df['est_total_deaths'] / (df['population']/1000000)

print(df)

"""
