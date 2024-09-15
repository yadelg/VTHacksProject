import requests

# Python Packages

import pandas as pd # Used for tables (ex. csv).
import os # Python library for navigating computer files.

import seaborn as sns # Used with matplotlib for graphing
import matplotlib.pyplot as plt # visualization tool

import sklearn # linear regression tool
from sklearn.linear_model import LinearRegression
import numpy as np

from bs4 import BeautifulSoup

# Data fetching code -- Use pandas to read CSV

# TEMPORARY, replace temp with CSV file name
def model(year, dataset):
    data_path = dataset # <--- name of CSV ex. electricity_perKWH.csv
    energy_data = pd.read_csv(data_path)
    currYear = 2023
    dataMonths = (2023-2018) * 12

    energy_data.head()
    # plot comparing price over years to 
    sns.scatterplot(x = 'Month', y = 'Price_Per_KWH', data = energy_data)

    # Initializing X and Y Variables 
    X = energy_data[['Month']]
    Y = energy_data[['Price_Per_KWH']]

    # Declaring and Training the Model
    linear = LinearRegression()
    linear.fit(X, Y)

    energy_data['Prediction'] = linear.predict((year - currYear) * 12 + dataMonths )







