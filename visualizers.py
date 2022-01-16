"""
GENERAL INFORMATION

Name: visualizers.py

Description: Contains multiple functions that read cleaned, global data about a single infection (in this case COVID-19)
or data about multiple pandemics and epidemics, and provides different ways to visualize the data graphically.

NB: The single-infection visualizers can read any csv file formatted with 'iso_codes' in the first column.
The example file, 'covid-data.csv', is formatted in this manner.

The multiple-infection visualizers can read any csv file formatted with 'infection' and 'continent' in the first two
columns. The example file, 'panepi-data.csv', is formatted in this manner.

Testing: Example function calls are provided at the bottom to test code functionality.

"""


import pandas as pd
import matplotlib.pyplot as plt
import datatoolslib as dtl  # See "Test Code" at the bottom for usage


""" Single-Infection Visualizers (Country-Based) """


# Compares a piece of statistical data about one infection between up to three different locations
def comp_infec_between_countries(dataframe, stat, iso_code1, iso_code2=None, iso_code3=None):

    # Store dataframe
    infec_data = dataframe

    # Copy dataframe to avoid permanent manipulations
    data_copy = infec_data.copy()

    # Set the index to 'iso_code' to make user query easier, and to make the codes display on the graph
    data_copy.set_index('iso_code', inplace=True)

    # If only one iso code has been entered, slice the dataframe by that code
    if iso_code3 is iso_code2 is None:
        country_comp = data_copy.loc[[iso_code1]]

    # If two iso codes have been entered, slice the dataframe by those codes
    elif iso_code3 is None:
        country_comp = data_copy.loc[[iso_code1, iso_code2]]

    # If three iso codes have been entered, slice the dataframe by those codes
    else:
        country_comp = data_copy.loc[[iso_code1, iso_code2, iso_code3]]

    # Plot the collection of country data with the y-axis being the user's chosen statistic
    plt.ion()
    country_comp.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    # Show the graph
    plt.show()
    plt.pause(30)


# Compares a piece of statistical data about one infection across all countries. Allows the user to view a subset of
# the first few countries
def infec_stat_all_countries(dataframe, sample_size, stat, top=False, bottom=False):

    # Store dataframe
    infec_data = dataframe

    # Copy dataframe to avoid permanent manipulations
    data_copy = infec_data.copy()

    # Decide whether to sort the data by highest stats, lowest stats, or alphabetically
    if top is True:
        data_copy.sort_values(by=[stat], inplace=True, ascending=False)
    elif bottom is True:
        data_copy.sort_values(by=[stat], inplace=True)

    # Display only a sample of the data, if requested
    if sample_size is not None:
        # Take the first few rows of data
        subsample = data_copy.head(sample_size)

        # Set the index to 'iso_code' to make the codes display on the graph
        subsample.set_index('iso_code', inplace=True)

        # Plot the graph with the y-axis being the user's chosen statistic
        plt.ion()
        subsample.plot(kind='bar', y=stat)

    else:
        data_copy.set_index('iso_code', inplace=True)

        # Plot the graph with the y-axis being the user's chosen statistic
        plt.ion()
        data_copy.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Country', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " by Country")

    # Show the graph
    plt.show()
    plt.pause(30)


""" Multiple-Infection Visualizers (Continent-Based) """


# Compares a piece of statistical data between two different infections in a given continent
def comp_infec_in_continent(dataframe, continent, infection1, infection2, stat):

    # Store dataframe
    panepi_data = dataframe

    # Copy dataframe to avoid permanent data manipulation
    data_copy = panepi_data.copy()

    # Store all data related to the chosen continent
    continent_group = data_copy[data_copy.continent == continent]

    # Set the index to 'infection' to make querying the chosen infections easier
    continent_group.set_index('infection', inplace=True)

    # Store all data related to the two chosen infections for the chosen continent
    infection_comp = continent_group.loc[[infection1, infection2]]

    # Plot the data with the y-axis being the chosen statistic
    plt.ion()
    infection_comp.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Infection', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " of " + infection1 + " and " + infection2 + " in " + continent)

    # Show the graph
    plt.show()
    plt.pause(30)


# Compares a piece of statistical data about a given virus in two different continents
def comp_infec_between_continents(dataframe, infection, continent1, continent2, stat):

    # Store dataframe
    panepi_data = dataframe

    # Copy dataframe to avoid permanent data manipulation
    data_copy = panepi_data.copy()

    # Store all data related to the chosen infection
    infection_group = data_copy[data_copy.infection == infection]

    # Set the index to 'continent' to make querying the chosen continents easier
    infection_group.set_index('continent', inplace=True)

    # Store all data related to the two chosen continents for the chosen infection
    continent_comp = infection_group.loc[[continent1, continent2]]

    # Plot the data with the y-axis being the chosen statistic
    plt.ion()
    continent_comp.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Location', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " of " + infection + " in " + continent1 + " and " + continent2)

    # Show the graph
    plt.show()
    plt.pause(30)


# Compares a given stat about two different infections in two different continents
def multi_comp(dataframe, infec1, infec2, continent1, continent2, stat):

    # Store dataframe
    panepi_data = dataframe

    # Copy dataframe to avoid permanent data manipulation
    data_copy = panepi_data.copy()

    # Set the index to 'infection' to make querying the chosen infections easier
    data_copy.set_index('infection', inplace=True)

    # Store all data related to the two chosen infections
    infection_data = data_copy.loc[[infec1, infec2]]

    # Store all data concerning both infections for each continent
    cont1_data = infection_data[infection_data.continent == continent1]
    cont2_data = infection_data[infection_data.continent == continent2]

    # Store the integer value of the chosen statistic for each continent, for each infection. Adjust for NaN values.
    cont1_infec1 = nan_checker(cont1_data, infec1, stat, continent1)
    cont1_infec2 = nan_checker(cont1_data, infec2, stat, continent1)
    cont2_infec1 = nan_checker(cont2_data, infec1, stat, continent2)
    cont2_infec2 = nan_checker(cont2_data, infec2, stat, continent2)

    # Create a dictionary such that its dataframe will have the following columns: the chosen infections, the chosen
    # infection stats for continent 1, and the chosen infection stats for continent two
    final_infec_comp_data = {'infection': [infec1, infec2], continent1: [cont1_infec1, cont1_infec2],
                             continent2: [cont2_infec1, cont2_infec2]}

    # Create a new dataframe from the dictionary
    infec_comp_df = pd.DataFrame(data=final_infec_comp_data)

    # Plot a double-bar graph with the infections on the x-axis, and the two continents' data on the y-axis
    plt.ion()
    infec_comp_df.plot(x='infection', y=[continent1, continent2], kind='bar')

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Infection', fontsize=11)
    plt.ylabel(y_axis_label, fontsize=11)
    plt.title(y_axis_label + " of " + infec1 + " and " + infec2 + " in " + continent1 + " and " + continent2,
              fontsize=11)

    # Show the graph
    plt.show()
    plt.pause(30)


""" Assistive Functions (Not for direct user interaction) """


# Checks for a NaN value in a slice of data and adjusts before graphing. For multi_comp.
def nan_checker(data, infec, stat, continent):

    # Slice data from dataframe
    datapoint = (data.loc[[infec]])[stat].values

    # Check if the value is NaN and replace with 0
    if pd.isna(datapoint):
        print("NOTE: No data for this value: " + continent + ", " + infec)
        return 0
    else:
        return int(datapoint)  # Return an int of the value if not NaN


""" Test Code: Single-Infection Visualizers """

# Data files
# covid_df = pd.read_csv('datafiles/covid-data.csv')

# Test 1: Testing the functionality of datatoolslib functions outside the library. Prints 'USA' to the console.
# dtl.find_iso_code('United States')

# Test 2A: Displays a bar graph of total COVID-19 cases per million in the United States and Canada.
# comp_infec_between_countries(covid_df, 'total_deaths', 'USA', 'CAN')
# Test 2B: Can also be used to compare non-infection statistics between countries.
# comp_infec_between_countries(covid_df, 'gdp_per_capita', 'USA', 'CAN')

# Test 3: Displays a bar graph of total COVID-19 cases per million in the first 20 countries with the lowest numbers
# infec_stat_all_countries(covid_df, 20, 'total_cases_per_million', bottom=True)


""" Test Code: Multiple-Infection Visualizers """

# Data files
# infec_df = pd.read_csv('datafiles/panepi-data.csv')

# Test 1: Testing the functionality of datatoolslib functions outside the library. Prints all continent names from
# 'panepi-data.csv' to the console as a list
# data = dtl.available_info(infec_df, 'continent')
# print(data)


# Test 2: Displays a bar graph of total estimated deaths from COVID19 and the Bubonic Plague in Europe.
# comp_infec_in_continent(infec_df, 'Europe', 'COVID19', 'SPANISH FLU', 'est_total_deaths')


# Test 3: Displays a bar graph of deaths per million from COVID19 in Africa and North America.
# comp_infec_between_continents(infec_df, 'COVID19', 'Africa', 'North America', 'deaths_per_million')


# Test 4: Displays a double-bar graph of estimated total deaths from COVID19 and the Bubonic Plague
# in Africa and Europe.
# multi_comp(infec_df, 'COVID19', 'HIV', 'Africa', 'North America', 'est_total_deaths')

