import requests

# Python Packages

import pandas as pd # Used for tables (ex. csv).
import os # Python library for navigating computer files.

import seaborn as sns # Used with matplotlib for graphing
import matplotlib.pyplot as plt # visualization tool

import sklearn # linear regression tool
from sklearn.linear_model import LinearRegression
import numpy as np

# Data fetching code -- Use pandas to read CSV

# TEMPORARY, replace temp with CSV file name
def model(year, city):
    data_path = "./all_cities_data_count_price.csv" # <--- name of CSV ex. electricity_perKWH.csv
    energy_data = pd.read_csv(data_path)
    currYear = 2024
    dataMonths = (2024-2018) * 12

    energy_data.head()

    # Initializing X and Y Variables 
    X = energy_data[['count']]
    Y = energy_data[[city]]

    # Declaring and Training the Model
    linear = LinearRegression()
    linear.fit(X, Y)

    energy_data['Prediction'] = linear.predict(((year - currYear) * 12) + dataMonths)
    print(energy_data['Prediction'])

model(2030, "Boston")






