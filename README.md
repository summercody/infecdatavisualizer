# Infection Data Visualizer

This repository houses multiple modules that provide different ways to visualize pandemic
and epidemic data graphically. It also provides two csv files with example data for COVID-19 through 01/09/22, and data 
about a handful of other pandemics and epidemics in history (Spanish Flu, HIV, Hong Kong Flu and the Bubonoic Plague).

**Technologies used:** Python, pandas, matplotlib

**IDE:** Pycharm

**covid_visualizer.py**

This module houses two functions, both of which allow the user to compare a chosen statistic about COVID-19 in different
countries.

**panepi_visualizer.py**

This module houses three functions that allow the user to compare the effects of different pandemics and epidemics
within and between specific continents. 

**datatoolslib.py**

This is a small library of functions that help the user get an overview of the data available in their chosen file. It 
also provides a way to look up iso codes, which is useful for working with covid_visualizer.py.

**covid-data.csv**

This file contains country-specific, continent-specific, and global data about COVID-19 through 01/09/22, which was
pulled from ["Our World In Data"](https://ourworldindata.org/coronavirus) and modified for size and increased usability. 

**panepi-data.csv**

This file contains basic continent-specific and global data about a handful of historical pandemics and epidemics, from
multiple sources. 

NB: As historical data of this nature is more difficult to find, there are many fields marked as "nan". The data is
best used as a means of displaying the functionality 'panepi_visualizer.py', and not as a comprehensive source of
information.

**iso-codes.csv**

This file contains a list of iso codes and their respective countries. A handful of codes are unique to "Our World in Data",
specifically those concerning continental and global data. It is largely used to create an iso dictionary in 'datatoolslib.py'.

**rawdata_cleaningcode**

This directory houses the raw data gathered from "Our World In Data", which was used to create the abridged
'covid-data.csv' file. It also contains all the one-off programs written to parse data and create new csv files when
necessary. 

NB: These files were moved to rawdata_cleaningcode after they were used, and are seperated from the files they were
initially referencing. If you would like to run them, make sure they are placed in the same directory
as their referenced files.
