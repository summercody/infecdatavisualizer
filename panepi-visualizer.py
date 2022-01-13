# Name: penepi-visualizer.py

import pandas as pd
import matplotlib.pyplot as plt


# Data files

ALL_INFECTIONS = 'panepi-data.csv'

""" General Tools """


# Displays a summary of the information provided by a given datafile. Takes a solo file input,
# a file input + the string 'headers', and a file input + the name of column as a string.
def show_available_info(datafile, data_type=None):
    dataframe = pd.read_csv(datafile)

    if data_type is None:
        print(dataframe)
        return

    if data_type == 'headers':
        print(dataframe.columns.values)
        return

    print(dataframe[data_type].values)


""" Multiple-Infection Visualizers """


# Compares a piece of statistical data between two different infections in a given continent. Reads files
# in the Pandemic and Epidemic (panepi) format -- see panepi-data.csv
def comp_infec_in_continent(datafile, continent, infection1, infection2, stat):
    panepi_data = pd.read_csv(datafile)

    data_copy = panepi_data.copy()

    continent_group = data_copy[data_copy.continent == continent]

    continent_group.set_index('infection', inplace=True)
    infection_comp = continent_group.loc[[infection1, infection2]]

    infection_comp.plot(kind='bar', y=stat)
    y_axis_label = stat.title().replace("_", " ")
    plt.xlabel('Infection', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " of " + infection1 + " and " + infection2 + " in " + continent)
    plt.show()


# Compares a piece of statistical data about a given virus in two different continents. Reads files
# in the Pandemic and Epidemic (panepi) format -- see panepi-data.csv
def comp_infec_between_continents(datafile, infection, continent1, continent2, stat):
    panepi_data = pd.read_csv(datafile)

    data_copy = panepi_data.copy()

    infection_group = data_copy[data_copy.infection == infection]

    infection_group.set_index('continent', inplace=True)
    continent_comp = infection_group.loc[[continent1, continent2]]

    continent_comp.plot(kind='bar', y=stat)
    y_axis_label = stat.title().replace("_", " ")
    plt.xlabel('Location', fontsize=14)
    plt.ylabel(y_axis_label, fontsize=14)
    plt.title(y_axis_label + " of " + infection + " in " + continent1 + " and " + continent2)
    plt.show()
    pass


# Compares a given stat about two different infections in two different continents. Reads files
# in the Pandemic and Epidemic (panepi) format -- see panepi-data.csv
def multi_comp(datafile, infec1, infec2, continent1, continent2, stat):

    panepi_data = pd.read_csv(datafile)
    data_copy = panepi_data.copy()

    data_copy.set_index('infection', inplace=True)
    infection_data = data_copy.loc[[infec1, infec2]]

    cont1_data = infection_data[infection_data.continent == continent1]
    cont2_data = infection_data[infection_data.continent == continent2]

    cont1_infec1 = int((cont1_data.loc[[infec1]])[stat].values)
    cont1_infec2 = int((cont1_data.loc[[infec2]])[stat].values)
    cont2_infec1 = int((cont2_data.loc[[infec1]])[stat].values)
    cont2_infec2 = int((cont2_data.loc[[infec2]])[stat].values)

    final_infec_comp_data = {'infection': [infec1, infec2], continent1: [cont1_infec1, cont1_infec2],
                             continent2: [cont2_infec1, cont2_infec2]}

    infec_comp_df = pd.DataFrame(data=final_infec_comp_data)

    infec_comp_df.plot(x='infection', y=[continent1, continent2], kind='bar')

    y_axis_label = stat.title().replace("_", " ")
    plt.xlabel('Infection', fontsize=11)
    plt.ylabel(y_axis_label, fontsize=11)
    plt.title(y_axis_label + " of " + infec1 + " and " + infec2 + " in " + continent1 + " and " + continent2,
              fontsize=11)

    plt.show()


""" Test Code """

# show_available_info(ALL_INFECTIONS, 'continent')

# comp_infec_in_continent(ALL_INFECTIONS, 'Europe', 'COVID19', 'BBP', 'est_total_deaths')

# comp_infec_between_continents(ALL_INFECTIONS, 'BBP', 'Africa', 'World', 'est_total_deaths')

# multi_comp(ALL_INFECTIONS, 'COVID19', 'BBP', 'Africa', 'Europe', 'est_total_deaths')





