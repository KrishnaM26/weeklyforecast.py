import requests
import json

##Location
wfo_site = ""
lat = ''
lon = ''

#api URLs
#forecasthourly_url = f'https://api.weather.gov/gridpoints/{site}/{lat},{lon}/forecast/hourly'
forecastweekly_url = f'https://api.weather.gov/gridpoints/{wfo_site}/{lat},{lon}/forecast'
#weatherbydate_url = f'https://api.weather.gov/stations/KPDK/observations/{start_time}'
##forecastcurrent_url = 'https://api.weather.gov/stations/KPDK/observations/latest'

#retrives all water and river api data
#weather_hr  = requests.get(forecasthourly_url)
weather_wk = requests.get(forecastweekly_url)
#weather_cur = requests.get(forecastcurrent_url)
#weather_timestamp = requests.get(weatherbydate_url)



#returns weekly weather forecast
def getweeklyforecast():
    weekly = json.loads(weather_wk.text)
    periods = weekly["properties"]["periods"]
    weekly_list = []

    for i in range(len(periods)):
        weekly_list.append({
            "name" : periods[i]['name'],
            "temperature": periods[i]['temperature'],
            "probabilityOfPrecipitation": periods[i]['probabilityOfPrecipitation']["value"],
            "windSpeed":  periods[i]['windSpeed'],
            "windDirection": periods[i]['windDirection'],
            "sForecast": periods[i]['shortForecast'],
            "dForecast": periods[i]['detailedForecast'],
            'isDayTime': periods[i]['isDaytime']
        })
    
    return weekly_list


def weeklyforecast():
    forecast = getweeklyforecast()
    format = []
    bar = "-"
    for i in range(len(forecast)):
       format.append(f"\n{bar}{' \U0001f30C' if forecast[i]['isDayTime'] != True else bar} {forecast[i]["name"]} {bar*2}\n Temperature: {forecast[i]['temperature']}°F\n Percipitation: {forecast[i]['probabilityOfPrecipitation']}%\n Wind: {forecast[i]['windSpeed']} - {forecast[i]['windDirection']}\n Description: {forecast[i]['dForecast']}\n {forecast[i]['sForecast']}")
    
    #day_time = format[::2]
    #night_time = format[1::2]
    
    for i in format:
        print(i)


weeklyforecast()
