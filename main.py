# Name: main.py
# Description: A script to access and run all the infection data visualizers

import visualizers as vs
import datatoolslib as dtl
import pandas as pd


# Sub functions

# Stores dataframe of desired csv file and displays the available visualizations for the type of data
def data_selector():

    available_visualizations = None

    datafile = input("\nPlease input the name or path of the csv file you wish to pull data from: ")
    dataframe = pd.read_csv(datafile)

    headers = dataframe.columns.values

    # If data is about one infection, or multiple infections
    if headers[0] == 'iso_code':
        available_visualizations = {'v1': "Compare up to three user-selected countries [v1]",
                                    'v2': "Compare between all countries [v2]"}
    elif headers[0] == 'infection':
        available_visualizations = {'v3': "Compare two infections in one location [v3]",
                                    'v4': "Compare one infection in two locations [v4]",
                                    'v5': "Compare two infections in two locations [v5]"}

    return dataframe, available_visualizations


# Loop that lets the user lookup multiple iso codes
def run_iso_assist():
    searching = True

    while searching:
        country = input("\nPlease enter the name of the country you wish to lookup (e.g. Algeria), "
                        "or type 'done' to end the search: ")

        if country == 'done':
            return

        dtl.find_iso_code(country)


# Requests a statistic from the user and provides options for viewing the dataframe
def get_stat(dataframe):
    stat = None

    while stat is None:

        stat = input("\nPlease enter the statistic you would like to use for comparison, or: "
                     "\n\nType 'data' to view a summary of all data in your file"
                     "\nType 'options' to view all available statistics in your file"
                     "\nType 'value check' to see all available data for a particular statistic"
                     "\n\nEnter choice: ")

        # Print a summary of the entire dataframe
        if stat == 'data':
            data = dtl.available_info(dataframe)
            print("")
            print(data)
            stat = None

        # Print a list of the columns as stat options
        if stat == 'options':
            data = dtl.available_info(dataframe, 'headers')
            print("")
            print(data)
            stat = None

        # View values in a specified column
        if stat == 'value check':
            check = input("\nPlease enter the name of the statistic you'd like see values for: ")
            data = dtl.available_info(dataframe, check)
            print("")
            print(data)
            stat = None

        # Check whether stat is a viable value
        if stat is not None and stat != 'options' and stat != 'data':
            if stat not in list(dataframe.columns):
                print("\nOops! This data is not available in your file.\n")
                stat = None
            else:
                return stat


# Provides two different ways to lookup dataframe info, for different types of datasets
def value_search(dataframe, value_name, query_type, lookup_func):

    value = None

    # Allows user to enter a specific keyword and search or its value in a list / dict using a specified function (e.g.
    # run_iso_assist)
    if query_type == 'keyword search':

        value = input("\nPlease input a " + value_name + " or type 'lookup' to find a " + value_name + ": ")
        if value == 'q':
            quit()
        if value == "lookup":
            lookup_func()
            value = None

    # Uses available_info in the datatools library to help user query a dataframe's contents by column
    if query_type == 'option display':

        value = input("\nPlease input a " + value_name + ", or type 'view' to see your options: ")
        if value == 'q':
            quit()

        if value == 'view':
            available_categories = dtl.available_info(dataframe, 'headers')

            print("")
            print(available_categories)

            more_info = input("\nPlease enter one of the above categories to view its contents: ")

            data = dtl.available_info(dataframe, more_info)

            print("")
            print(data)

            value = None

    return value


# Runs processes to help user input and/or find a desired value
def get_value(dataframe, value_name, query_type=None, lookup_func=None, value_checker=None):

    value = None

    while value is None:
        if query_type is not None:  # the dataframe and/or value can be queried, user is notified of this option
            value = value_search(dataframe, value_name, query_type, lookup_func)
        else:
            value = input("\nPlease input a " + value_name + ": ")

        if value == 'q':
            quit()

        # If the value might be viable, and a function is available to check the value for validity
        if value is not None and value != "lookup" and value != 'q' and value_checker is not None:

            value_options = value_checker()

            if type(value_options) == dict:
                if value not in list(value_options.values()):
                    print("\nOops! That's not a valid " + value_name + ".")
                    value = None

            elif type(value_options) == list:
                if value not in value_options:
                    print("\nOops! That's not a valid " + value_name + ".")
                    value = None

    return value


# Visualizers

# Guides user through inputting values for comp_infec_between_countries, and runs the function
def run_vone(dataframe):

    iso_code2 = None
    iso_code3 = None

    iso_code1 = get_value(dataframe, 'iso code', query_type='keyword search', lookup_func=run_iso_assist,
                          value_checker=dtl.create_iso_dict)

    add_country = input("\nWould you like to add another country? [y/n]: ")

    if add_country == 'y':
        iso_code2 = get_value(dataframe, 'iso code', query_type='keyword search', lookup_func=run_iso_assist,
                              value_checker=dtl.create_iso_dict)

        add_country = input("\nWould you like to add a final country? [y/n]: ")

        if add_country == 'y':
            iso_code3 = get_value(dataframe, 'iso code', query_type='keyword search', lookup_func=run_iso_assist,
                                  value_checker=dtl.create_iso_dict)

    stat = get_stat(dataframe)

    vs.comp_infec_between_countries(dataframe, stat, iso_code1, iso_code2, iso_code3)


# Guides user through inputting values for infec_stat_all_countries, and runs the function
def run_vtwo(dataframe):

    # Value presets, in case user chooses not to use one
    top = False
    bottom = False
    sample_size = None
    stat = get_stat(dataframe)

    order = input("\nWould you like to sort the data by highest stats, lowest stats, or pull data alphabetically? "
                  "[high/low/alpha]: ")

    while order != 'high' and order != 'low' and order != 'alpha':
        order = input("\nPlease enter a valid option [high/low/alpha]: ")

    if order == 'high':
        top = True
    elif order == 'low':
        bottom = True

    sample_query = input("\nWould you like to pull a sample of countries, or visualize all of them? [sample/all]:  ")

    while sample_query != 'sample' and sample_query != 'all':
        sample_query = input("\nPlease enter a valid option [sample/all]: ")

    if sample_query == 'sample':
        sample_size = int(get_value(dataframe, 'sample size'))

    vs.infec_stat_all_countries(dataframe, sample_size, stat, top, bottom)


# Guides user through inputting values for comp_infec_in_continent, and runs the function
def run_vthree(dataframe):

    continent = get_value(dataframe, 'continent', query_type='option display')
    infection1 = get_value(dataframe, 'first infection', query_type='option display')
    infection2 = get_value(dataframe, 'second infection', query_type='option display')
    stat = get_stat(dataframe)

    vs.comp_infec_in_continent(dataframe, continent, infection1, infection2, stat)


# Guides user through inputting values for comp_infec_between_continents, and runs the function
def run_vfour(dataframe):

    infection = get_value(dataframe, 'infection', query_type='option display')
    continent1 = get_value(dataframe, 'first continent', query_type='option display')
    continent2 = get_value(dataframe, 'second continent', query_type='option display')

    stat = get_stat(dataframe)

    vs.comp_infec_between_continents(dataframe, infection, continent1, continent2, stat)


# Guides user through inputting values for multi_comp, and runs the function
def run_vfive(dataframe):

    infection1 = get_value(dataframe, 'first infection', query_type='option display')
    infection2 = get_value(dataframe, 'second infection', query_type='option display')

    continent1 = get_value(dataframe, 'first continent', query_type='option display')
    continent2 = get_value(dataframe, 'second continent', query_type='option display')

    stat = get_stat(dataframe)

    vs.multi_comp(dataframe, infection1, infection2, continent1, continent2, stat)


# Reads user input and decides which function to run
def run_visualizer(chosen_visualization, dataframe):
    if chosen_visualization == 'v1':
        run_vone(dataframe)

    if chosen_visualization == 'v2':
        run_vtwo(dataframe)

    if chosen_visualization == 'v3':
        run_vthree(dataframe)

    if chosen_visualization == 'v4':
        run_vfour(dataframe)

    if chosen_visualization == 'v5':
        run_vfive(dataframe)


# Displays available visualizations for a given dataframe and asks for user's choice
def display_visualization_options(available_visualizations, dataframe):
    print("\nPlease select which type of visualization you'd like to run.\n")

    for i in available_visualizations.values():
        print(i)

    chosen_visualization = input("\nChosen visualization: ")

    while chosen_visualization not in available_visualizations.keys():
        chosen_visualization = input("\nSorry, please choose a valid option: ")

    run_visualizer(chosen_visualization, dataframe)


# Run entire program
def run_program():
    available_visualizations = None
    dataframe = None
    same_data = False

    # Allow user to stay in program to run multiple visualizations
    running = True
    while running:

        if same_data is False:  # Keep track of whether user wants to do multiple visualizations with same dataframe

            # Ask for the type of data in their file of choice
            visualizer_data = data_selector()

            dataframe = visualizer_data[0]
            available_visualizations = visualizer_data[1]

        display_visualization_options(available_visualizations, dataframe)

        visualize_more = input("\nWould you like to run another visualization? [y/n]: ")

        if visualize_more == 'n':
            return
        elif visualize_more == 'y':
            run_same_data = input("\nWould you like to visualize the same set of data, or different data? "
                                  "[same/different]: ")

            while run_same_data != 'same' and run_same_data != 'different':
                print("\nSorry, please choose one of the options [same/different]: ")

            if run_same_data == 'same':
                same_data = True

            if run_same_data == 'different':
                same_data = False


def main():

    print("\nHi, welcome to Infection Data Visualizer! \n")

    run_program()

    print("\nSuccessfully closed Infection Data Visualizer. Bye!")


if __name__ == "__main__":
    main()
