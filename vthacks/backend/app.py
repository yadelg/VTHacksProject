import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

import random

#from .backend import model

app = Flask(__name__)

# from ....VTHacks.backend import model

cors = CORS(app, origins='*')


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
    #print(energy_data[['count', city, 'Prediction']])

    # Print the prediction for the specific year
    return '%.2f'%(prediction[0][0])

#print(model(2038, "Washington D.C."))

dict = {
    "city": "Boston",
    "year": 2024
}

# cityInput = "Boston"
# yearInput = 2028
    
@app.route('/submit', methods=['POST'])
def get_data():
    data = request.get_json()
    dict["city"] = data["city"]
    dict["year"] = int(data["year"])
    prediction = model(dict["year"], dict["city"])
    #print(year + " " + city)
    print(prediction)
    return data
        
        
# @app.route('/search', methods=['GET'])
# def return_prediction():
#     prediction = model(yearInput, cityInput)
#     return jsonify(
#         {
            
#             "prediction": [
#                 prediction
#                 #random.randint(3, 9)
#             ]
#         }
#     )

@app.route('/search', methods=['GET'])
def return_prediction():
    #data = get_data()
    
    #print(data)
    prediction = model(dict["year"], dict["city"])
    print(dict["year"])
    print(dict["city"])
    return jsonify({"prediction": prediction})
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
