import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
cors = CORS(app, origins='*')


@app.route('/search', methods=['GET'])
def return_prediction():
    return jsonify(
        {
            "year": [
                2028
            ],
            "prediction": [
                random.randint(3, 9),
                random.randint(3, 9),
                random.randint(3, 9),
                random.randint(3, 9)
               
            ]
        }
    )

@app.route('/submit', methods=['POST'])
def get_data():
    data = request.get_json()
    print(data["city"])
    return data
        
    
if __name__ == "__main__":
    app.run(debug=True)
    
