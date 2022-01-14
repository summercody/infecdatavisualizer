"""
GENERAL INFORMATION

Name: panepi_visualizer.py

Description: A collection of functions the user can call to read a csv file containing data about different epidemics
and pandemics, and visualize the data graphically.

NB: Each function can visualize data from other csv files as long as 'infection' and 'continent' are listed as
the first two columns. The example file, panepi-data.csv, is formatted in this manner.

Testing: Example function calls are provided at the bottom to test code functionality.

"""


import pandas as pd
import matplotlib.pyplot as plt
import datatoolslib as dtl  # See "Test Code" at the bottom for usage


# Compares a piece of statistical data between two different infections in a given continent
def comp_infec_in_continent(datafile, continent, infection1, infection2, stat):

    # Create a dataframe
    panepi_data = pd.read_csv(datafile)

    # Copy dataframe to avoid permanent data manipulation
    data_copy = panepi_data.copy()

    # Store all data related to the chosen continent
    continent_group = data_copy[data_copy.continent == continent]

    # Set the index to 'infection' to make querying the chosen infections easier
    continent_group.set_index('infection', inplace=True)

    # Store all data related to the two chosen infections for the chosen continent
    infection_comp = continent_group.loc[[infection1, infection2]]

    # Plot the data with the y-axis being the chosen statistic
    infection_comp.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Infection', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " of " + infection1 + " and " + infection2 + " in " + continent)

    # Show the graph
    plt.show()


# Compares a piece of statistical data about a given virus in two different continents
def comp_infec_between_continents(datafile, infection, continent1, continent2, stat):

    # Create a dataframe
    panepi_data = pd.read_csv(datafile)

    # Copy dataframe to avoid permanent data manipulation
    data_copy = panepi_data.copy()

    # Store all data related to the chosen infection
    infection_group = data_copy[data_copy.infection == infection]

    # Set the index to 'continent' to make querying the chosen continents easier
    infection_group.set_index('continent', inplace=True)

    # Store all data related to the two chosen continents for the chosen infection
    continent_comp = infection_group.loc[[continent1, continent2]]

    # Plot the data with the y-axis being the chosen statistic
    continent_comp.plot(kind='bar', y=stat)

    # Store the y-axis label as the chosen statistic
    y_axis_label = stat.title().replace("_", " ")

    # Label the x and y-axes, and title the graph
    plt.xlabel('Location', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " of " + infection + " in " + continent1 + " and " + continent2)

    # Show the graph
    plt.show()


# Compares a given stat about two different infections in two different continents
def multi_comp(datafile, infec1, infec2, continent1, continent2, stat):

    # Create a dataframe
    panepi_data = pd.read_csv(datafile)

    # Copy dataframe to avoid permanent data manipulation
    data_copy = panepi_data.copy()

    # Set the index to 'infection' to make querying the chosen infections easier
    data_copy.set_index('infection', inplace=True)

    # Store all data related to the two chosen infections
    infection_data = data_copy.loc[[infec1, infec2]]

    # Store all data concerning both infections for each continent
    cont1_data = infection_data[infection_data.continent == continent1]
    cont2_data = infection_data[infection_data.continent == continent2]

    # Store the integer value of the chosen statistic for each continent, for each infection
    cont1_infec1 = int((cont1_data.loc[[infec1]])[stat].values)
    cont1_infec2 = int((cont1_data.loc[[infec2]])[stat].values)
    cont2_infec1 = int((cont2_data.loc[[infec1]])[stat].values)
    cont2_infec2 = int((cont2_data.loc[[infec2]])[stat].values)

    # Create a dictionary such that its dataframe will have the following columns: the chosen infections, the chosen
    # infection stats for continent 1, and the chosen infection stats for continent two
    final_infec_comp_data = {'infection': [infec1, infec2], continent1: [cont1_infec1, cont1_infec2],
                             continent2: [cont2_infec1, cont2_infec2]}

    # Create a new dataframe from the dictionary
    infec_comp_df = pd.DataFrame(data=final_infec_comp_data)

    # Plot a double-bar graph with the infections on the x-axis, and the two continents' data on the y-axis
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


""" Test Code """

# Data files
ALL_INFECTIONS = 'panepi-data.csv'


# Test 1: Testing the functionality of datatoolslib functions outside the library. Prints all continent names from
# 'panepi-data.csv' to the console as a list
# dtl.show_available_info(ALL_INFECTIONS, 'continent')


# Test 2: Displays a bar graph of total estimated deaths from COVID19 and the Bubonic Plague in Europe.
# comp_infec_in_continent(ALL_INFECTIONS, 'Europe', 'COVID19', 'BBP', 'est_total_deaths')


# Test 3: Displays a bar graph of deaths per million from COVID19 in Africa and North America.
# comp_infec_between_continents(ALL_INFECTIONS, 'COVID19', 'Africa', 'North America', 'deaths_per_million')


# Test 4: Displays a double-bar graph of estimated total deaths from COVID19 and the Bubonic Plague
# in Africa and Europe.
# multi_comp(ALL_INFECTIONS, 'COVID19', 'BBP', 'Africa', 'Europe', 'est_total_deaths')





