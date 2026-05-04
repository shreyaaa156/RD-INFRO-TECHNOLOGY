import requests
import pandas as pd

# OpenWeather API Key
API_KEY = "f40047a95045c1a84282eca533f63db0"

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

# Export to CSV
df.to_csv("weather_output.csv", index=False)

print("\nDataset exported successfully!")