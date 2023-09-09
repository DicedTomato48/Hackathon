# from a colour table https://www.rapidtables.com/web/color/RGB_Color.html
# WAY TOO MANY COLOURS... need more beiges and browns -> colours that are more common in clothing
base_colors = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'Black': (0, 0, 0),
    'White': (255, 255, 255),
    'Grey': (128,128,128),
    'Black':(0,0,0),
 	'Red':(255,0,0),
 	'Lime':(0,255,0),
 	'Yellow':(255,255,0),
 	'Cyan':(0,255,255),
 	'Magenta':(255,0,255),
 	'Maroon':(128,0,0),
 	'Olive':(128,128,0),
 	'Purple':(128,0,128),
 	'Teal':(0,128,128),
 	'Navy':(0,0,12),
    'Orange':(255,165,0),
    # Add more basic colors as needed
 	'dark red':(139,0,0),
 	'brown':(165,42,42),
 	'firebrick':(178,34,34),
 	'crimson':(220,20,60),
 	'red':(255,0,0),
 	'tomato':(255,99,71),
 	'coral':(255,127,80),
 	'indian red':(205,92,92),
 	'light coral':(240,128,128),
 	'dark salmon':(233,150,122),
 	'salmon':(250,128,114),
 	'light salmon':(255,160,122),
 	'orange red':(255,69,0),
 	'dark orange':(255,140,0),
 	'orange':(255,165,0),
 	'gold':(255,215,0),
 	'dark golden rod':(184,134,11),
 	'golden rod':(218,165,32),
 	'pale golden rod':(238,232,170),
 	'dark khaki':(189,183,107),
 	'khaki':(240,230,140),
 	'olive':(128,128,0),
 	'yellow':(255,255,0),
 	'yellow green':(154,205,50),
 	'dark olive green':(85,107,47),
 	'olive drab':(107,142,35),
 	'lawn green':(124,252,0),
 	'chartreuse':(127,255,0),
 	'green yellow':(173,255,47),
 	'dark green':(0,100,0),
 	'forest green':(34,139,34),
 	'lime':(0,255,0),
 	'lime green':(50,205,50),
 	'light green':(144,238,144),
 	'pale green':(152,251,152),
 	'dark sea green':(143,188,143),
 	'medium spring green':(0,250,154),
 	'spring green':(0,255,127),
 	'sea green':(46,139,87),
 	'medium aqua marine':(102,205,170),
 	'medium sea green':(60,179,113),
 	'light sea green':(32,178,170),
 	'dark slate gray':(47,79,79),
 	'teal':(0,128,128),
 	'dark cyan':(0,139,139),
 	'aqua':(0,255,255),
 	'cyan':(0,255,255),
 	'light cyan':(224,255,255),
 	'dark turquoise':(0,206,209),
 	'turquoise':(64,224,208),
 	'medium turquoise':(72,209,204),
 	'pale turquoise':(175,238,238),
 	'aqua marine':(127,255,212),
 	'powder blue':(176,224,230),
 	'cadet blue':(95,158,160),
 	'steel blue':(70,130,180),
 	'corn flower blue':(100,149,237),
 	'deep sky blue':(0,191,255),
 	'dodger blue':(30,144,255),
 	'light blue':(173,216,230),
 	'sky blue':(135,206,235),
 	'light sky blue':(135,206,250),
 	'midnight blue':(25,25,112),
 	'navy':(0,0,128),
 	'dark blue':(0,0,139),
 	'medium blue':(0,0,205),
 	'blue':(0,0,255),
 	'royal blue':(65,105,225),
 	'blue violet':(138,43,226),
 	'indigo':(75,0,130),
 	'dark slate blue':(72,61,139),
 	'slate blue':(106,90,205),
 	'medium slate blue':(123,104,238),
 	'medium purple':(147,112,219),
 	'dark magenta':(139,0,139),
 	'dark violet':(148,0,211),
 	'dark orchid':(153,50,204),
 	'medium orchid':(186,85,211),
 	'purple':(128,0,128),
 	'thistle':(216,191,216),
 	'plum':(221,160,221),
 	'violet':(238,130,238),
 	'orchid':(218,112,214),
 	'medium violet red':(199,21,133),
 	'pale violet red':(219,112,147),
 	'deep pink':(255,20,147),
 	'hot pink':(255,105,180),
 	'light pink':(255,182,193),
 	'pink':(255,192,203),
 	'antique white':(250,235,215),
 	'beige':(245,245,220),
 	'bisque':(255,228,196),
 	'blanched almond':(255,235,205),
 	'wheat':(245,222,179),
 	'corn silk':(255,248,220),
 	'lemon chiffon':(255,250,205),
 	'light golden rod yellow':(250,250,210),
 	'light yellow':(255,255,224),
 	'saddle brown':(139,69,19),
 	'sienna':(160,82,45),
 	'chocolate':(210,105,30),
 	'peru':(205,133,63),
 	'sandy brown':(244,164,96),
 	'burly wood':(222,184,135),
 	'tan':(210,180,140),
 	'rosy brown':(188,143,143),
 	'moccasin':(255,228,181),
 	'navajo white':(255,222,173),
 	'peach puff':(255,218,185),
 	'misty rose':(255,228,225),
 	'lavender blush':(255,240,245),
 	'linen':(250,240,230),
 	'old lace':(253,245,230),
 	'papaya whip':(255,239,213),
 	'sea shell':(255,245,238),
 	'mint cream':(245,255,250),
 	'slate gray':(112,128,144),
 	'light slate gray':(119,136,153),
 	'light steel blue':(176,196,222),
 	'lavender':(230,230,250),
 	'floral white':(255,250,240),
 	'alice blue':(240,248,255),
 	'ghost white':(248,248,255),
 	'honeydew':(240,255,240),
 	'ivory':(255,255,240),
 	'azure':(240,255,255),
 	'snow':(255,250,250),
 	'black':(0,0,0),
 	'dark gray':(169,169,169),
 	'silver':(192,192,192),
 	'light gray':(211,211,211),
 	'gainsboro':(220,220,220),
 	'white smoke':(245,245,245)
}
# Temp lists for the seperate categories\
    # REFINE THIS
color_category = {}
color_category['Red'] = ['Red','dark red','brown','firebrick','crimson','red','tomato','coral','indian red',
'light coral','dark salmon','salmon','light salmon','orange red']
color_category['Green'] = ['Green', 'Lime','dark khaki','khaki','olive','yellow green','dark olive green','olive drab','lawn green',
'chartreuse','green yellow','dark green','forest green','lime','lime green','light green','pale green','dark sea green',
'medium spring green','spring green','sea green', 'medium aqua marine','medium sea green','light sea green','aqua marine','mint cream','honeydew']
color_category['Blue'] = ['Blue', 'Cyan', 'Teal', 'light sea green', 'dark slate gray', 'teal', 'dark cyan', 'aqua', 'cyan',
'light cyan', 'dark turquoise', 'turquoise', 'medium turquoise', 'pale turquoise', 'aqua marine', 'powder blue',
'cadet blue', 'steel blue', 'corn flower blue', 'deep sky blue', 'dodger blue', 'light blue', 'sky blue',
'light sky blue', 'midnight blue', 'navy', 'dark blue', 'medium blue', 'blue', 'royal blue', 'light steel blue',
'alice blue', 'azure']
color_category['Black'] = ['Black', 'Grey', 'Navy', 'slate gray', 'light slate gray', 'black', 'dark gray', 'silver', 'light gray']
color_category['White'] = ['White', 'Grey', 'pale golden rod', 'light cyan', 'antique white', 'beige', 'bisque',
'blanched almond', 'wheat', 'corn silk', 'lemon chiffon', 'moccasin', 'navajo white', 'peach puff', 'linen',
'old lace', 'papaya whip', 'sea shell', 'mint cream', 'floral white', 'alice blue', 'ghost white',
'honeydew', 'ivory', 'snow', 'gainsboro', 'white smoke']
color_category['Yellow'] = ['Yellow', 'gold', 'dark golden rod', 'golden rod', 'pale golden rod', 'khaki', 'yellow',
'lemon chiffon', 'light golden rod yellow', 'light yellow']
color_category['Purple'] = ['Magenta', 'Purple', 'corn flower blue', 'blue violet', 'indigo', 'dark slate blue', 'slate blue',
'medium slate blue', 'medium purple', 'dark magenta', 'dark violet', 'dark orchid', 'medium orchid', 'purple',
'thistle', 'plum', 'violet', 'orchid', 'medium violet red', 'pale violet red', 'rosy brown']
color_category['Pink'] = ['deep pink', 'hot pink', 'light pink', 'pink', 'misty rose', 'lavender blush', 'lavender']
color_category['Brown'] = ['Maroon', 'Olive', 'brown', 'firebrick', 'saddle brown', 'sienna', 'chocolate', 'peru',
'sandy brown', 'burly wood', 'tan']
color_category['Orange'] = ['Orange', 'tomato', 'coral', 'dark salmon', 'light salmon', 'orange red', 'dark orange',
'orange', 'bisque', 'sandy brown']

color_palettes = {
    'Pallete1' : ['white_colors', 'brown_colors', 'black_colors'],
    'Pallete2' : ['white_colors', 'brown_colors'],
    'Pallete3' : ['white_colors', 'white_colors'],
    'Pallete4' : ['black_colors'],
    'Pallete5' : ['white_colors'],
    'Paltte6' : ['white_colors', 'blue_colors']
    # tODO
}


color_weather_mapping = {
    'Red': 'Rainy',
    'Green': 'Sunny',
    'Blue': 'Rainy',
    'Black': 'Foggy',
    'White': 'Cloudy',
    'Yellow': 'Sunny',
    'Purple': 'Rainy',
    'Pink': 'Sunny',
    'Brown': 'Sunny',
    'Orange': 'Sunny',
}

def is_light_color(rgb: tuple[int,int,int]):
	# Calculate the brightness of the color using the formula
	# brightness = 0.299 * R + 0.587 * G + 0.114 * B
	return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

	# Return True if brightness is greater than or equal to 128, indicating a light color
def separate_dark_bright():
	light_colors = []
	dark_colors = []

	for color in color_category.values():
		for specific_color in color:
			brightness = is_light_color(base_colors[specific_color])
			if brightness >= 128:
				light_colors.append(specific_color)
			elif brightness < 128:
				dark_colors.append(specific_color)

	#Dictionaries for light and dark colors with their RGB values
	print("Light Colors:")
	print(light_colors)

	print("\nDark Colors:")
	print(dark_colors)

if __name__ == '__main__':
	separate_dark_bright()
