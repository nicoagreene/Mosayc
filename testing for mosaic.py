from PIL import Image
import os 

# Load and convert the image to RGB mode if necessary
img = Image.open('mushroom.png')
if img.mode != 'RGB':
    img = img.convert('RGB')
width, height = img.size

# Define the target colors


# with each chunk iterate through dictionary 



folder_colors = {'red': [204, 0, 0], 'blue': [15, 20, 20], 'green': [250, 250, 250]}




def replacepixel(img, folder):
    pixels = img.load()  # Load the pixel map
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            pixels[x, y] = color_match(pixel, folder)

def color_match(pix, folder):
    range_num = 100
    closest_color = None
    smallest_distance = float('inf')
    
    # Check each target color
    for color_name, target_color in folder.items():
        distance = sum((pc - tc) ** 2 for pc, tc in zip(pix, target_color))
        if distance < smallest_distance:
            closest_color = target_color
            smallest_distance = distance

    # Return the closest color if within the acceptable range, else return the original color
    if smallest_distance <= range_num ** 2:
        return tuple(closest_color)
    else:
        return pix

# Replace pixels in the image
replacepixel(img, folder_colors)

# Show the modified image
img.show()


def color_match(pix, folder):
    range_num = 220
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            rmin = pixel(x,y)[0] - range_num
            rmax = pixel(x, y)[0] + range_num
            gmin = pixel(x,y)[1] - range_num
            gmax = pixel(x,y)[1] + range_num 
            bmin = pixel(x,y)[2] - range_num
            bmax = pixel(x,y)[2] + range_num
            dist = ((block_color(x,y)[0])**2 + (block_color(x,y)[1])**2 + (block_color(x,y)[2])**2)**0.5

            for file in folder.keys():
                #with open(path) as i
                if folder[file][0] >= rmin and folder[file][0] <= rmax:
                    if folder[file][1]  >= gmin and folder[file][1] <= gmax:
                        if folder[file][2] >= bmin and folder[file][2] <= bmax:
                            return file
                