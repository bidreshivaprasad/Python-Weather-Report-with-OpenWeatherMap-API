import requests
import json
import geocoder # pip install geocoder

# Get the location of the current location (latitude, longitude)
def get_user_location():
    g = geocoder.ip('me')
    if g.latlng:
        return g.latlng
    else:
        return None

# Get the location Name of the current location from (latitude, longitude) to City Name
def get_city_name(latitude, longitude):
    g = geocoder.osm([latitude, longitude], method='reverse')
    if g.city:
        return g.city
    else:
        return None    

# Get the Weather report from the current location
def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"  # You can change the units to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    if response.status_code == 200:
        # Extract relevant weather information from the API response
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display the weather information
        print(f"Weather at your location: {get_city_name(latitude, longitude)}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error occurred while retrieving weather data.")


api_key = "YOUR_API_KEY" # Add your API key here in "xxxxxxxxxxxxxxxxxxxxx"
user_location = get_user_location()
if user_location:
    latitude, longitude = user_location
    get_weather(api_key, latitude, longitude)
else:
    print("Unable to determine the user's location.")
