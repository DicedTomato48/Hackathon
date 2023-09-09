class WeatherColour:
    
    # need to remove optional argument
    def __init__(self, colour=None, clothing_type=None):
        self.colour = colour
        self.clothing_type = clothing_type

    """
    Planning:
    matching colour choices:
        Complementary colors: https://www.w3schools.com/colors/colors_compound.asp
        analogous colors: https://www.w3schools.com/colors/colors_analogous.asp
        Monochromatic colors: https://www.w3schools.com/colors/colors_monochromatic.asp
        Neutral colors: https://www.w3schools.com/colors/colors_neutral.asp
        Triadic colors: https://www.w3schools.com/colors/colors_triadic.asp

    Weather types and best colours:
        Hot and Sunny weather: Got it, on it
            Best Colors: Light and cool colors like white, pastels (light pink, baby blue, pale yellow), 
            and soft neutrals (beige, light gray) are excellent choices for hot and sunny days. 
            They reflect sunlight and help keep you cool.
            Avoid jackets, preferably shorts and short sleeves. 
        Cold and Overcast Weather:
            Best Colors: Warm and rich colors like deep reds, oranges, 
            and earthy tones (brown, olive green) can add warmth to your appearance 
            and complement the cool weather.
        Rainy Weather:
            Best Colors: Bright and cheerful colors can help uplift your mood on rainy days.
            Consider wearing colors like yellow, coral, or turquoise to counter the gloomy weather.
        
    Types of clothing depending on weather:
        Hot and Sunny weather: Short Slevees and Shorts

        Mid Weather: Long Sleeves and Pants, Jackets(optional)

        Cold and Overcast Weather: Long Sleeves, Jackets, Pants

        Rainy Weather: Jacket 100%


    Thresholds for weather:
        Hot and Sunny weather is above 24 degrees celsius
        "Mid weather" is between 18 and 24 degrees celsius
        Cold and Overcast Weather is below 18 degrees celsius



        
        
        output: Dictionary that contains the weather and the best colours for that weather
        we also need a dictionary that contains an item of clothing and its associated colour and matches them?
        
             
    """
    def get_weather_colour(self):
        weather_colour_dict = {
            "Hot and Sunny": ["White", "Pink", "Yellow"],
            "Cold and Overcast": ["Red", "Orange"],
            "Mid Weather": ["Blue", "Green", 'White', "Brown"],
            "Chilly": ["Blue", "Green", "White"],
            "Rainy": ["Black", "Blue", "Green", "White"]
        }
        return weather_colour_dict
    
    
    
    
    
 
 
    


    

class Clothing:

    """

    Output: Dictionary containing all the clothes that match based on the weather class, would be like shirt: bla.png(?),bla,bla pants: bla, bla, bla 
    """


