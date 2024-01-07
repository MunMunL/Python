import requests



parameters = {
    "latitude": 35.689487,
    "longitude": 139.691711,
    "hourly": ["weather_code"],
}

url = "https://api.open-meteo.com/v1/forecast"

response = requests.get(url, params=parameters)
# print(response.status_code)
response.raise_for_status()
data = response.json()
hourly_weather_code = data["hourly"]
hourly_slice = hourly_weather_code["weather_code"][0:12]

is_raining = False

for hour_data in hourly_slice:
    if hour_data > 50:
        is_raining = True

if is_raining:
    print("Bring an umbrella")