import requests

# Replace with your OpenWeatherMap API Key
API_KEY = "b7f25c88fe6b592f1c73ed22c68fa434"

print("=" * 40)
print("      BASIC WEATHER APPLICATION")
print("=" * 40)

city = input("\nEnter City Name: ").strip()

# Input Validation
if city == "":
    print("Error: City name cannot be empty.")
    exit()

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code == 200:

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32

        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 40)
        print("          WEATHER REPORT")
        print("=" * 40)
        print(f"City            : {city.title()}")
        print(f"Temperature (C) : {temperature_c:.2f} °C")
        print(f"Temperature (F) : {temperature_f:.2f} °F")
        print(f"Humidity        : {humidity}%")
        print(f"Weather         : {weather.title()}")
        print(f"Wind Speed      : {wind_speed} m/s")
        print("=" * 40)

    elif response.status_code == 404:
        print("Error: City not found.")

    elif response.status_code == 401:
        print("Error: Invalid API Key.")

    else:
        print("Something went wrong.")
        print(data)

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: No Internet Connection.")

except Exception as e:
    print("Unexpected Error:", e)