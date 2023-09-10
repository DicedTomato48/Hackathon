from colorpicking import *
from clothing import *
from weather_api import Weather
from colorpicking import color_category
# from colorpicking import color_category

temp_weather_mapping = {
    'hot': ['Light Yellow', 'Light Pink', 'Light Blue'], #lite colours and cool colours
    'cold': ['Dark Red', 'Dark Blue', 'Dark Purple', 'Dark Black', 'Dark White'], #warm and dark colours
}

color_weather_mapping = {
    'rain': ['Light Green', 'Light Yellow', 'Light Orange', 'Light Pink'], #bright and cheerful colours
    'sun': ['Light Green', 'Light Yellow', 'Light Pink', 'Light Brown', 'Light Orange'], #similar to hot
    'fog': ['Light Black', 'Dark Black', 'Dark White', 'Light White'], 
    'cloud': ['Dark White', 'Dark Red', 'Dark Blue','Dark Purple'], #similar to cold
    'wind' : ['Dark red', 'Dark Blue', 'Dark Purple', 'Dark Black', 'Dark White'], #similar to cold
    'overcast': ['Dark White'], #similar to cold
    }

current = Weather()
um, most_probable, det, max_temp, min_temp = current.get_hourly_weather_forecast()

def all_colours_total(weather, temperature):
    all_colors_list = []
    if temperature > 24:
        all_colors_list.extend(temp_weather_mapping['hot'])
    else:
        all_colors_list.extend(temp_weather_mapping['cold'])

    all_colors_list.extend(ret_all_colour_for_weather(weather))

    return all_colors_list

    



def ret_all_colour_for_weather(weather: str):
    global color_weather_mapping
    main_available_colour = []
    try:
        get_color = lambda x, color: x.get(color)
        for item in color_weather_mapping.keys():
            if item in weather.lower():
                weather = item
        list_colour = color_weather_mapping.get(weather)
        # for colors in list_colour:
        #     main_available_colour.extend(get_color(color_category, colors)) 
        main_available_colour.extend(list_colour)
    except:
        raise ValueError("Invalid weather type")
    return main_available_colour

# def set_all_colour_for_weather(status_temperature: Temperature):
#     hot_set, cold_set = None, None
#     for idx, item in enumerate(['hot', 'cold']):
#         match idx:
#             case 0:
#                 hot_set = set(ret_all_colour_for_weather(item))
#             case 1:
#                 cold_set = set(ret_all_colour_for_weather(item))
#     match status_temperature:
#         case Temperature.COLD:
#             return cold_set
#         case Temperature.HOT:
#             return hot_set
#         case Temperature.NORMAL:
#             return hot_set.union(cold_set)
#         case _:
#             raise ValueError("Invalid temperature is passed to the function")

def Complementary_Colours(color_list):
    for color in color_list:
        print(color_category[color])



   



if __name__ == "__main__":
    um, most_probable, det, max_temp, min_temp = current.get_hourly_weather_forecast()
    #print(ret_all_colour_for_weather("hot")) # so, for rainy you can have all of these colours
    color_list = (all_colours_total(most_probable, max_temp))
    #print(color)
    #print(ret_all_colour_for_weather('sun'))
    #print(all_colours_total(most_probable, max_temp))
    Complementary_Colours(color_list)
   
# um, most_probable, det, max_temp, min_temp = current.get_hourly_weather_forecast()
# all_colours_total = all_colours_total(most_probable, max_temp)