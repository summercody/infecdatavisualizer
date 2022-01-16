# Infection Data Visualizer

This program provides different ways to visualize pandemic
and epidemic data graphically. It also provides two csv files with example data for COVID-19 through 01/09/22, and data 
about a handful of other pandemics and epidemics in history (Spanish Flu, HIV,and the Bubonic Plague).

**Technologies used:** Python, pandas, matplotlib

**IDE:** Pycharm

_-Files and Modules-_

**main.py**

Run this module to chose visualizers and input data via the console.

**visualizers.py**

This module houses five functions which allow the user to compare country-based statistics about one infection (in this case,
COVID-19) or continent-based statistics about other historical infections.

**datatoolslib.py**

This is a small library of functions that help the user get an overview of the data available in their chosen file. It 
also provides a way to look up iso codes, which is useful for working with the country-specific visualizers.

**data_cleaning.py**

This module contains all the one-off scripts written to parse data and create new csv files during the data cleaning process. 

**covid-data.csv**

This file contains country-specific and global data about COVID-19 through 01/09/22, which was
pulled from ["Our World In Data"](https://ourworldindata.org/coronavirus) and modified for size and increased usability. 

**panepi-data.csv**

This file contains basic continent-specific and global data about a handful of historical pandemics and epidemics, from
multiple sources. 

NB: As historical data of this nature is more difficult to find, there are many fields marked as "nan". The data is
best used as a means of displaying the functionality of the multi-infection visualizers, and not as a comprehensive 
source of information.

**iso-codes.csv**

This file contains a list of iso codes and their respective countries. A handful of codes are unique to "Our World in Data".
It is largely used to create an iso dictionary in 'datatoolslib.py'.

_-Directories-_

**sourcedata**

This directory houses the raw data gathered from ["Our World In Data"](https://ourworldindata.org/coronavirus), which was used to create the abridged
'covid-data.csv' file. 

**datafiles**

This directory houses all the example datasets, and iso-codes.csv.
