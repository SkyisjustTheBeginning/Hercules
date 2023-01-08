import time
print("""
███████╗████████╗███████╗██████╗░███╗░░██╗░█████╗░██╗░░░░░███████╗░█████╗░██████╗░███████╗░█████╗░░█████╗░░██████╗████████╗
██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
█████╗░░░░░██║░░░█████╗░░██████╔╝██╔██╗██║███████║██║░░░░░█████╗░░██║░░██║██████╔╝█████╗░░██║░░╚═╝███████║╚█████╗░░░░██║░░░
██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗██║╚████║██╔══██║██║░░░░░██╔══╝░░██║░░██║██╔══██╗██╔══╝░░██║░░██╗██╔══██║░╚═══██╗░░░██║░░░
███████╗░░░██║░░░███████╗██║░░██║██║░╚███║██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░░██║██████╔╝░░░██║░░░
╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░""")
import requests
WeatherTarget = str(input("Enter Location:"))
api_key = "65825486e9c1aefba2408ed97a7dfb9b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + WeatherTarget

response = requests.get(complete_url)

x = response.json()
if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]
    current_pressure = y["pressure"]

    current_humidiy = y["humidity"]

    z = x["weather"]
    weather_description = z[0]["description"]
    current_temperature = current_temperature - 273.15
    Status = "Weather update for " + WeatherTarget + "\n" " Current Temperature:" + str(
                round(current_temperature)) + "\n" + " Current Humidity:" + str(
                round(current_humidiy)) + "\n" + " Current Pressure:" + str(
                round(current_pressure)) + "\n" + " Weather Description:" + str(weather_description)
    print(Status)
    print("This program will close in 2 minutes")
    time.sleep(120)