
from PIL import Image
import os 

# Load and convert the image to RGB mode if necessary
img = Image.open('mushroom.png')
if img.mode != 'RGB':
    img = img.convert('RGB')
width, height = img.size


folder_colors2 = {'red': [204, 50, 75], 'black': [100, 110, 250], 'yellow ish': [220,220,130],}


#WORKS
def color_match(pix, dict): # pix is tuple representing color
    range_num = 100    #IF the distance is in this range then color can be replaced 
    closest_color = None   # variable which stores closest color in search 
    smallest_distance = float('inf') #setting smallest_distance to infinity, so we can track 
    
    # Check each target color
    for color_name, target_color in dict.items():
        distance = sum((pc - tc) ** 2 for pc, tc in zip(pix, target_color))   #zip basically makes a pair inside the tuple to compare the color valies of pix and target color 
        if distance < smallest_distance:
            closest_color = target_color
            smallest_distance = distance

    return tuple(closest_color)
    # Return the closest color if within the acceptable range, else return the original color
    if smallest_distance <= range_num ** 2:
        return tuple(closest_color)
    else:
        return pix


#WORKS
def replace_pixel(img):
    pixels = img.load()  # Load the pixel map
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y] 
            pixels[x, y] = color_match(pixel, folder_colors2) #Action repplaces pixels with the matched color 

replace_pixel(img)

img.show()