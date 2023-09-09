import datetime
import re
from curl_cffi import requests

class Weather:

    ip_url = "http://www.geoplugin.net/json.gp?ip="

    def __init__(self):
        self.__current_time = datetime.datetime.now()
        self.__ip = requests.get("https://api.ipify.org/?format=json", impersonate="chrome110").json()["ip"]

    def get_city(self):
        new_ip_session = requests.Session()
        if self.__ip.count(".") == 3 and all(x.isnumeric() for x in self.__ip.split(".")):
            response = new_ip_session.get(f"{Weather.ip_url}{self.__ip}")
        else:
            raise ValueError("Invalid IP address is passed")

        city = re.search(r'"geoplugin_city":"(.*?)"', str(response.content)).group(1)
        return city

    def get_weather_details(self):
        city_name = self.get_city()
        get_weather_det_ses = requests.Session()
        res_weather = get_weather_det_ses.get(f"http://api.weatherapi.com/v1/current.json?key=ee9cd5ab9e1643038e615755230909&q={city_name}&aqi=no", impersonate="chrome110")
        temperature_celsius = res_weather.json()["current"]["temp_c"]
        

        parse_condition = re.search(r'"condition":{(.*?)","code"', str(res_weather.content)).group(1).split('","')
        parse_condition = [x.split('":"')[1] for x in parse_condition]
        return f"Current condition: {parse_condition[0]}\nCurrent Temperature: {temperature_celsius}°C\nWeather Icon: https:{parse_condition[1]}\nCurrent Time: {self.__current_time}\nYour IP Address: {self.__ip}"

    def get_hourly_weather_forecast(self):
        city_name = self.get_city()
        hourly_forecast_ses = requests.Session()
        res_hourly_forecast = hourly_forecast_ses.get(f"http://api.weatherapi.com/v1/forecast.json?key=ee9cd5ab9e1643038e615755230909&q={city_name}&days=1&aqi=no&alerts=no&hourly=yes", impersonate="chrome110")
        forecast_data = res_hourly_forecast.json()["forecast"]["forecastday"][0]["hour"]

        forecast_info = "Hourly Weather Forecast:\n"
        weather_priority = {}
        all_temperatures = []
        for hour in forecast_data:
            time = hour["time"]
            condition = hour["condition"]["text"]
            temperature = hour["temp_c"]
            forecast_info += f"{time}: {condition}, {temperature}°C\n"
            all_temperatures.append(float(temperature))
            try:
                _ = weather_priority.get(condition)
                weather_priority[condition] += 1
            except:
                weather_priority[condition] = 1
        # print(weather_priority)
            
        # {'Clear': 2, 'Cloudy': 5, 'Overcast': 6, 'Sunny': 2, 'Patchy rain possible': 3, 'Partly cloudy': 6}
        ''''Check the most probable weather for the day'''
        list_weather_val = list(weather_priority.values())
        largest_possibility = list_weather_val.index(max(list_weather_val))
        weather_items_list = list(weather_priority.keys())[largest_possibility]

        umbrella = False
        if "rain" in str(weather_priority).lower():
            umbrella = True

        return umbrella, weather_items_list, forecast_info, max(all_temperatures), min(all_temperatures)

    def __str__(self):
        um, most_probable, det, max_temp, min_temp = self.get_hourly_weather_forecast()
        statement = "****** Take an UMBRELLA ******\n\n" if um else ""
        return f"{statement}The most probable weather is: {most_probable}\n\n====[Temperature Details]====\nLowest Temperature: {min_temp}\nHighest Temperature: {max_temp}\n{self.get_weather_details()}\n{det}"

if __name__ == "__main__":
    obj_weather = Weather()
    print(obj_weather)
