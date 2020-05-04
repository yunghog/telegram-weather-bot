# Python program to find current
# weather details of any city
# using openweathermap api

import requests, json
def tellWeather(city):
    api_key = "ee09cabd0c0770e88fd6cd931143eeca"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
    	y = x["main"]
    	current_temperature = y["temp"]
    	current_pressure = y["pressure"]
    	current_humidiy = y["humidity"]
    	z = x["weather"]
    	weather_description = z[0]["description"]
    	print(" Temperature (in kelvin unit) = " +
    					str(current_temperature) +
    		"\n atmospheric pressure (in hPa unit) = " +
    					str(current_pressure) +
    		"\n humidity (in percentage) = " +
    					str(current_humidiy) +
    		"\n description = " +
    					str(weather_description))
    else:
    	print(" City Not Found ")
    return(str(weather_description))
