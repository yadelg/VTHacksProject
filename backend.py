import requests

# Python Packages

import pandas as pd # Used for tables (ex. csv).
import os # Python library for navigating computer files.

import seaborn as sns # Used with matplotlib for graphing
import matplotlib.pyplot as plt # visualization tool

import sklearn # linear regression tool
import numpy as np

from bs4 import BeautifulSoup

url = "https://data.bls.gov/timeseries/A    PUS23B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"


def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    odd_rows = soup.find_all('tr', class_="odd")
    even_rows = soup.find_all('tr', class_="even")  

    odd_data = [[td.text for td in row.find_all('td')] for row in odd_rows]
    even_data = [[td.text for td in row.find_all('td')] for row in even_rows]

    combined_data = []

    for odd, even in zip(odd_data, even_data):
        combined_data.append(odd)
        combined_data.append(even)

    if len(odd_data) > len(even_data): 
        combined_data.extend(odd_data[len(even_data):])

    elif len(even_data) > len(odd_data):
        combined_data.extend(even_data[len(odd_data):])

    for row in combined_data:
        print(row)

fetch(url)




# Data fetching code -- Use pandas to read CSV

# TEMPORARY, replace temp with CSV file name
temp = 0
data_path = temp # <--- name of CSV ex. electricity_perKWH.csv
energy_data = pd.read_csv(data_path)

energy_data.head()
# plot comparing price over years to 
sns.scatterplot(x = 'Year', y = 'Price_Per_KWH', data = energy_data)




