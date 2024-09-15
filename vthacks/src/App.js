import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [searchedYear, setSearchedYear] = useState(2028);
  const [searchedCity, setSearchedCity] = useState("");
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
        <h1>Energy Price Prediction</h1>
        <div class="form-group">
            <label for="city-select">Select City:</label>
            <select id="city-select" onChange={handleCityDropDown}>
                <option value="Boston">Boston</option>
                <option value="New York">New York</option>
                <option value="Atlanta">Atlanta</option>
                <option value="Washington D.C.">Washington D.C.</option>
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
            </select>
        </div>
        <button id="submit-button" onClick={submit}>Submit</button>
        <div id="result">
            <h2>Prediction:</h2>
            <span id="price">{price}</span>
        </div>
    </div>
  );
}

export default App;
