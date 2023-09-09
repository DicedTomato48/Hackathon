from colorpicking import *

def ret_all_colour_for_weather(weather: str):
    color_weather_mapping = {
    'hot': ['Yellow', 'Pink', 'Blue'], #lite colours and cool colours
    'cold': ['Red', 'Blue', 'Purple'], #warm and dark colours
    'rain': ['Green', 'Yellow', 'Orange', 'Pink'], #bright and cheerful colours
    'sun': ['Green', 'Yellow', 'Pink', 'Brown', 'Orange'], #similar to hot
    'fog': ['Black'],
    'cloud': ['White'], #similar to cold
    'wind' : ['Green'], #similar to cold
    'overcast': ['White'], #similar to cold
    } # we can use sets, to find the intersecting colours for many different scenarios, like Sunny and windy 
    # or rainy and foggy. the thing is, for the accuracy, could you please assign the correct colour to the appropriate weather ?
    # I have no idea if they are correct, i have copied it from a website, can we get on a call, its kinda hard to talk here properly
    main_available_colour = []
    try:
        get_color = lambda x, color: x.get(color)
        for item in color_weather_mapping.keys():
            if item in weather.lower():
                weather = item
        list_colour = color_weather_mapping.get(weather)
        for colors in list_colour:
            main_available_colour.extend(get_color(color_category, colors)) 
    except:
        raise ValueError("Invalid weather type")
    return main_available_colour

if __name__ == "__main__":
    print(ret_all_colour_for_weather("overcast")) # so, for rainy you can have all of these colours

   #all of them, the logic, w