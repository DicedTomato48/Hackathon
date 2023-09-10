from weather_api import Weather
from enum import Enum, auto
import color_mapping

# class Temperature(Enum):
#     COLD = auto()
#     NORMAL = auto()
#     HOT = auto()

current = Weather()
um, most_probable, det, max_temp, min_temp = current.get_hourly_weather_forecast()

# print(max_temp)

def get_weather_clothes(temperature : int):
    if temperature > 24:
        return ['short sleeves', 'shorts'] # Temperature.HOT,
    elif 18 < temperature <= 24:
        return  ['long sleeves','pants'] #Temperature.NORMAL,
    elif temperature <= 18:
        return  ['jackets','long sleeves','pants'] #Temperature.COLD,

# def determine_colours(temperature: int):
#     status_temp = get_weather_clothes(temperature)
#     all_colour_set: set = color_mapping.set_all_colour_for_weather(status_temp[0])
#     return all_colour_set



class Clothing:

    """

    Output: Dictionary containing all the clothes that match based on the weather class, would be like shirt: bla.png(?),bla,bla pants: bla, bla, bla 
    """
    # need to remove optional argument
    def __init__(self, colour=None, clothing_type=None):
        self.colour = colour
        self.clothing_type = clothing_type


# print(get_weather_clothes(max_temp))