import requests
import pandas as pd

API_KEY = "f40047a95045c1a84282eca533f63db0"

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

print("\nFinal Data:")
print(df)

df.to_csv("weather_output.csv", index=False)

print("\nData saved successfully!")