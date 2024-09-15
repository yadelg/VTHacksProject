import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [searchedYear, setSearchedYear] = useState(2024);
  const [searchedCity, setSearchedCity] = useState("Boston");
  const [price, setPrice] = useState(0);
  const [submitted, setSubmitted] = useState(false);

  const fetchAPI = async() => {
    const response = await axios.get("http://localhost:5000/search");
    setPrice(response.data.prediction);
  }

  const submit = async(e) => {
    e.preventDefault();
    let answers = {
      "city": searchedCity,
      "year": searchedYear
    }
    const response = await axios.post("http://localhost:5000/submit", answers, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    setSubmitted(true);
  }

  const handleCityDropDown = event => {
    setSearchedCity(event.target.value);
  }

  const handleYearDropDown = event => {
    setSearchedYear(event.target.value);
  }

  useEffect(() => {
    fetchAPI();
    setSubmitted(false);
  }, [submitted]);

  return (
    <div class="container">
        <h1>⚡Amplytics⚡</h1>
        <h3>Predicting Electricity Cost per kWh</h3>
        <div class="form-group">
            <label for="city-select">Select City:</label>
            <select id="city-select" onChange={handleCityDropDown}>
                <option value="Boston">Boston</option>
                <option value="New York">New York</option>
                <option value="Philadelphia">Philadelphia</option>
                <option value="Chicago">Chicago</option>
                <option value="Detroit">Detroit</option>
                <option value="Minneapolis">Minneapolis</option>
                <option value="St. Louis">St. Louis</option>
                <option value="Atlanta">Atlanta</option>
                <option value="Baltimore">Baltimore</option>
                <option value="Miami">Miami</option>
                <option value="Tampa">Tampa</option>
                <option value="Washington D.C.">Washington D.C.</option>
                <option value="Dallas">Dallas</option>
                <option value="Houston">Houston</option>
                <option value="Denver">Denver</option>
                <option value="Phoenix">Phoenix</option>
                <option value="Los Angeles">Los Angeles	</option>
                <option value="Riverside">Riverside</option>
                <option value="San Diego">San Diego</option>
                <option value="San Francisco">San Francisco</option>
                <option value="Seattle">Seattle</option>
                <option value="Urban Alaska">Urban Alaska</option>
                <option value="Urban Hawaii">Urban Hawaii</option>
            </select>
        </div>
        <div class="form-group">
            <label for="year-select">Select Year:</label>
            <select id="year-select" onChange={handleYearDropDown}>
                <option value="2024">2024</option>
                <option value="2025">2025</option>
                <option value="2026">2026</option>
                <option value="2027">2027</option>
                <option value="2028">2028</option>
                <option value="2029">2029</option>
                <option value="2030">2030</option>
                
            </select>
        </div>
        <button id="submit-button" onClick={submit}>Submit</button>
        <div id="result">
            <h2>Prediction:</h2>
            <span id="price">${price} per kWh</span>
        </div>
        <br></br>
        <br></br>
        <div>
          <h2>How it works:</h2>
          <p>Uses Linear Regression and past data on electrical costs in metropolitan areas 
            in order to predict future costs for electricity in those areas
            per kilowatt hour.
          </p>
        </div>
    </div>
  );
}

export default App;
