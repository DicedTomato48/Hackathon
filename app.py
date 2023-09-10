from flask import Flask, request, render_template, jsonify, send_from_directory
import cv2
import numpy as np # This might be needed.
import base64 # decoding camera ...nevermind
import os
import matplotlib.pyplot as plt
import math
import csv
import random


# classes
from clothing import Clothing
# other imports
from colorthief import ColorThief
from colorpicking import *
from color_mapping import *
from weather_api import *

app = Flask(__name__, static_url_path='/static')

import csv

ref = ['databases\clothing_top.csv', 'databases\clothing_shoes.csv', 'databases\clothing_bottom.csv', 'databases\clothing_outerwear.csv']
for i in range(len(ref)):
    header = ["color", "type", "image_filename"]
    csv_file_path = ref[i]
    with open(csv_file_path, mode='w', newline='') as fileref:
        csv_writer = csv.writer(fileref)
        csv_writer.writerow(header)

# helper functions
def grayscale_to_color(grayscale_value):
    # map grayscale values to color names or RGB tuples
    if grayscale_value < 128:
        return 'Black'
    else:
        return 'White'
    
def euclidean_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

# function to classify an RGB tuple into a basic color category
def classify_color(rgb_tuple):
    closest_color = None
    min_distance = float('inf')  # Initialize with a large value
    for color_name, color_rgb in base_colors.items():
        distance = euclidean_distance(rgb_tuple, color_rgb)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name
    return closest_color
    
    
# DATA STRUCTURES... these are temporary for now... need good data structures
clothing_objects = []
captured_frames = []

# other variables
image_counter = 1
UPLOAD_FOLDER = 'uploaded_images'
clothing_categories = ["Shirt", "Pants","Shoes"]
captured_colors = []

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/capture', methods=['POST'])
def capture():
    global image_counter
    image_data = request.form['imageData']
    clothing_type = request.form['clothingType']
    image_bytes = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_bytes, np.uint8)
    # decoding
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    image_filename = f'{image_counter}.jpg'
    image_counter += 1

    image_path = os.path.join(UPLOAD_FOLDER, image_filename)
    
    # testing
    # adds the image to the folder
    cv2.imwrite(image_path, image)
    
    # gets the dominant color (btw im kinda forced to use the american spelling to keep stuff consistent)
    # code from https://www.youtube.com/watch?v=nEYap1mupUQ
    ct = ColorThief(f'uploaded_images\{image_filename}')
    dominant_color = ct.get_color(quality=1)
    #plt.imshow([[dominant_color]])
    #plt.show()
    
    
    # euclidian distance between two colour vectors to get closest color
    basic_color_category = classify_color(dominant_color)
    
    color_list = []
    for color in color_category:
            if basic_color_category in color_category[color]:
                color_list.append(color)
                
    
    print(f'Detected color is closest to: {basic_color_category}')
    print(f"{basic_color_category} is present in the following color schemes: {', '.join(color_list)} ")
    
    # color_list[0] is the general colour .... idk why we made it a list????
    # basic_color_category is the specific color
    clothing_instance = Clothing(colour=basic_color_category, clothing_type=clothing_type)
    
    # save to csv database
    print(f'clothing type is {clothing_type}')
    if clothing_type == 'Shirtshort':
        csv_filename = 'databases\clothing_top.csv'
    elif clothing_type == 'Shirtlong':
        csv_filename = 'databases\clothing_top.csv'
    elif clothing_type == 'Jacket':
        csv_filename = 'databases\clothing_outerwear.csv'
    elif clothing_type == 'Pants':
        csv_filename = 'databases\clothing_bottom.csv'
    elif clothing_type == 'Shorts':
        csv_filename = 'databases\clothing_bottom.csv'
    elif clothing_type == 'Knitwear':
        csv_filename = 'databases\clothing_outerwear.csv'
    elif clothing_type == 'Shoes':
        csv_filename = 'databases\clothing_shoes.csv'
    else:
        return "unknown clothing type??????"
    
    
    with open(csv_filename, mode='a', newline='') as fileref:
        writer = csv.writer(fileref)
        writer.writerow([clothing_instance.colour, clothing_instance.clothing_type, image_filename])
        captured_colors.append(clothing_instance.colour)

    return "done"

@app.route('/uploaded_images/<filename>')
def uploaded_images(filename):
    image_folder = './uploaded_images'
    return send_from_directory(image_folder, filename)

# dead
@app.route('/show_generated_outfits')
def show_generated_outfits():
    image_files = os.listdir('./uploaded_images')
    return render_template('gallery.html', image_files=image_files)

# opens the page for generated outfits
@app.route('/generate_outfits')
def generate_outfits():
    weather = Weather()
    available_colors = ret_all_colour_for_weather(weather.get_weather_details())
    print(f'available colors are {available_colors}')

    # basic mvp
    new_outfit = []
    outfit_component_locations = ['databases\clothing_top.csv', 'databases\clothing_bottom.csv', 'databases\clothing_shoes.csv']
    half_chance = random.randint(0,1)
    if half_chance > 0.5:
        outfit_component_locations.append('databases\clothing_outerwear.csv')
    
    
    um, most_probable, det, max_temp, min_temp = current.get_hourly_weather_forecast()
    available_colors = all_colours_total(most_probable, max_temp)
    print(f'total available colors are {available_colors}')
    
    for clothing_type in outfit_component_locations:
        print(clothing_type)
        #random_color = random.choice(available_colors)
        #print(random_color)
        
        selected_article = None
        with open(clothing_type, newline='') as fileref:
            reader = csv.DictReader(fileref)
            for row in reader:
                #new_outfit.append(row['image_filename'])
                #break
                for color in available_colors:
                    if row['color'] == color:
                        selected_article = row['image_filename']
                        new_outfit.append(selected_article)
                        
    print('x')      
    for article in new_outfit:
        print(article) 
        print('x')
    
    return render_template('generations.html', outfits = new_outfit)
    
    

@app.route('/view_frames')
def view_frames():
    return jsonify(captured_frames)

if __name__ == '__main__':
    app.run(debug=True)
