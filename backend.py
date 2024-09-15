import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def model(year, city):
    data_path = "./all_cities_data_count_price.csv"  # Name of CSV file
    energy_data = pd.read_csv(data_path)
    currYear = 2024
    dataMonths = (2024 - 2018) * 12

    # Initializing X and Y Variables 
    X = energy_data[['count']]
    Y = energy_data[[city]]

    # Declaring and Training the Model
    linear = LinearRegression()
    linear.fit(X, Y)

    # Prepare input for prediction as a 2D array
    input_data = np.array([[(year - currYear) * 12 + dataMonths]])

    # Make prediction for the single input value
    prediction = linear.predict(input_data)

    # If you want to see the prediction for the entire DataFrame
    # Calculate the prediction for each row based on the number of months
    energy_data['Prediction'] = linear.predict(X)

    # Print predictions for the whole DataFrame
    print(energy_data[['count', city, 'Prediction']])

    # Print the prediction for the specific year
    return prediction[0][0]

print(model(2030, "Boston"))
