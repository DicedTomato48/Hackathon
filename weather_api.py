import datetime
import re
from curl_cffi import requests

class Weather:

    ip_url = "http://www.geoplugin.net/json.gp?ip="

    def __init__(self):
        self.__current_time = datetime.datetime.now()
        self.__ip = requests.get("https://api.ipify.org/?format=json", headers={"User-Agent": "chrome110"}).json()["ip"]

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
        res_weather = get_weather_det_ses.get(f"http://api.weatherapi.com/v1/current.json?key=ee9cd5ab9e1643038e615755230909&q={city_name}&aqi=no", headers={"User-Agent": "chrome110"})
        temperature_celsius = res_weather.json()["current"]["temp_c"]
        

        parse_condition = re.search(r'"condition":{(.*?)","code"', str(res_weather.content)).group(1).split('","')
        parse_condition = [x.split('":"')[1] for x in parse_condition]
        return f"Current condition: {parse_condition[0]}\nCurrent Temperature: {temperature_celsius}°C\nWeather Icon: https:{parse_condition[1]}\nCurrent Time: {self.__current_time}\nYour IP Address: {self.__ip}"

    def get_hourly_weather_forecast(self):
        city_name = self.get_city()
        hourly_forecast_ses = requests.Session()
        res_hourly_forecast = hourly_forecast_ses.get(f"http://api.weatherapi.com/v1/forecast.json?key=ee9cd5ab9e1643038e615755230909&q={city_name}&days=1&aqi=no&alerts=no&hourly=yes", headers={"User-Agent": "chrome110"})
        forecast_data = res_hourly_forecast.json()["forecast"]["forecastday"][0]["hour"]

        forecast_info = "Hourly Weather Forecast:\n"
        count = 0
        for hour in forecast_data:
            time = hour["time"]
            condition = hour["condition"]["text"]
            temperature = hour["temp_c"]
            forecast_info += f"{time}: {condition}, {temperature}°C\n"
            

            

        return forecast_info

    def __str__(self):
        return f"{self.get_weather_details()}\n{self.get_hourly_weather_forecast()}"

if __name__ == "__main__":
    obj_weather = Weather()
    print(obj_weather)
