# RD-INFRO-TECHNOLOGY
Real-Time Weather Data Collection Project using Python and OpenWeather API
# Weather Data Collection Project 🌦️

## RD INFRO TECHNOLOGY – Data Analysis Internship

---

# Project Overview

This project collects real-time weather data from multiple cities using the OpenWeather API. The collected data is processed using Python and Pandas, converted into a structured dataset, and exported into a CSV/Excel file for analysis.

This project was completed as part of the Data Analysis Internship at RD INFRO TECHNOLOGY.

---

# Technologies Used

- Python
- Pandas
- Requests Library
- OpenWeather API
- CSV / Excel File Handling

---

# Features

✅ Collects live weather data using API

✅ Extracts:
- Temperature
- Humidity
- Weather Condition
- Wind Speed

✅ Supports multiple cities

✅ Converts raw JSON data into structured tabular format

✅ Exports data into CSV/Excel file

---

# Project Structure

```text
RD-INFRO-TECHNOLOGY/
│
├── weather_data_collection.py
├── weather_output.csv
├── README.md


#Python Code:

import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"

cities = ["Bangalore", "Delhi", "Mumbai", "Chennai"]

all_data = []

for city in cities:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if "main" in data:

        weather_data = {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"],
            "Wind Speed": data["wind"]["speed"]
        }

        all_data.append(weather_data)

    else:
        print(f"Error fetching data for {city}: {data['message']}")

df = pd.DataFrame(all_data)

print(df)

df.to_csv("weather_output.csv", index=False)

print("Weather data saved successfully!")

#Sample Output
City      	Temperature	  Humidity	 Weather	        Wind Speed
Bangalore	    29.37	        55	    scattered clouds	  5.81
Delhi        	27.05	        47	      haze	            4.12
Mumbai	      29.99	        74	      haze	            4.63
Chennai	      33.81	        58	      haze	             3.09

#How to Run the Project

Step 1: Install Required Libraries
pip install requests pandas

Step 2: Add Your API Key
Replace:
API_KEY = "YOUR_API_KEY"
with your actual OpenWeather API key.

Step 3: Run the Program
python weather_data_collection.py
Key Learnings
API Integration using Python
Working with JSON data
Data Collection techniques
Data Structuring using Pandas
Exporting datasets into CSV format

#Conclusion

This project demonstrates practical implementation of real-time data collection using APIs and Python. It showcases skills in data extraction, processing, and structured dataset generation for analytical purposes.
