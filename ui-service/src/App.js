import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);
  const [recommendation, setRecommendation] = useState(null);

  const handleCityChange = (e) => {
    setCity(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const weatherResponse = await axios.get(`http://localhost:5000/weather?city=${city}`);
      setWeather(weatherResponse.data);
      
      const recommendationResponse = await axios.get(`http://localhost:5001/recommendation?city=${city}`);
      setRecommendation(recommendationResponse.data);
    } catch (error) {
      console.error('Error fetching data', error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          City:
          <input type="text" value={city} onChange={handleCityChange} />
        </label>
        <button type="submit">Get Recommendation</button>
      </form>
      
      {weather && (
        <div>
          <h2>Weather in {weather.city}</h2>
          <p>Temperature: {weather.temperature} °C</p>
          <p>Description: {weather.description}</p>
        </div>
      )}
      
      {recommendation && (
        <div>
          <h2>Recommendation</h2>
          <p>{recommendation.recommendation}</p>
        </div>
      )}
    </div>
  );
}

export default App;
