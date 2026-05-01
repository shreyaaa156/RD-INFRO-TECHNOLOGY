# RD-INFRO-TECHNOLOGY
Real-Time Weather Data Collection Project using Python and OpenWeather API
# Weather Data Collection Project 🌦️

## RD INFRO TECHNOLOGY – Data Analysis Internship

---

# Project Overview

This project collects real-time weather data from multiple Indian cities using the OpenWeather API. The collected data is processed using Python and Pandas, converted into a structured dataset, and exported into an Excel file for further analysis.

This project was completed as part of the Data Analysis Internship at RD INFRO TECHNOLOGY.

---

# Technologies Used

- Python
- Pandas
- Requests Library
- OpenWeather API
- OpenPyXL
- Visual Studio Code

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

✅ Exports data into Excel format

---

# Project Structure

```text
RD-INFRO-TECHNOLOGY/
│
├── weather_data_collection.py
├── weather_output.xlsx
└── README.md

Python Code:

import requests
import pandas as pd

# OpenWeather API Key
API_KEY = "YOUR_API_KEY"

# Cities to fetch weather data
cities = ["Bangalore", "Delhi", "Mumbai", "Chennai"]

# List to store collected data
weather_records = []

print("\nFetching weather data...\n")

for city in cities:

    # API endpoint
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    # API request
    response = requests.get(url)

    # Convert response into JSON
    data = response.json()

    # Validate response
    if "main" in data:

        weather_info = {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather Condition": data["weather"][0]["description"],
            "Wind Speed": data["wind"]["speed"]
        }

        weather_records.append(weather_info)

        print(f"Successfully fetched data for {city}")

    else:
        print(f"Failed to fetch data for {city}")

# Create DataFrame
df = pd.DataFrame(weather_records)

# Display final dataset
print("\nFinal Weather Dataset:\n")
print(df)

# Export to Excel
df.to_excel("weather_output.xlsx", index=False)

print("\nDataset exported successfully!")

Sample Output
City	        Temperature (°C)	Humidity (%)	Weather Condition	Wind Speed
Bangalore	     31.49	             49          	scattered clouds	 5.36
Delhi	         32.05	             40	             haze	             3.60
Mumbai	         32.99	             58	             haze	             6.17
Chennai	         36.88	             49	             scattered clouds	 2.57
#How to Run the Project

Step 1: Install Required Libraries
pip install requests pandas

Step 2: Add Your API Key
Replace:
API_KEY = "YOUR_API_KEY"
with your actual OpenWeather API key.

Step 3: Run the Program
python weather_data_collection.py

Key Learnings:
API Integration using Python
Working with JSON data
Real-time Data Collection
Data Structuring using Pandas
Exporting datasets into Excel format
Working with APIs in VS Code
Business Use Case

This project can help:

Weather monitoring systems
Smart city applications
Travel and tourism platforms
Environmental data tracking

Conclusion

This project demonstrates practical implementation of real-time data collection using APIs and Python. It showcases skills in data extraction, processing, and structured dataset generation for analytical purposes.
