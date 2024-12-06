from PIL import Image
import numpy as np

def calculate_warmness_coldness(image_src):

    image = Image.open(image_src)

    # Convert image to RGB and get pixel data
    image_rgb = image.convert('RGB')
    pixels = np.array(image_rgb)
    
    # Split image into RGB channels
    red = pixels[:,:,0]
    green = pixels[:,:,1]
    blue = pixels[:,:,2]

    # Calculate warmness (reds and yellows)
    warm_score = np.sum((red > green) & (red > blue)) + np.sum((green > red) & (green > blue))

    # Calculate coldness (blues and greens)
    cold_score = np.sum((blue > red) & (blue > green)) + np.sum((green > red) & (green > blue))
    
    # Normalize the scores to get a final warm/cold score
    total_pixels = image.size[0] * image.size[1]
    warmness_coldness_score = (warm_score - cold_score) / total_pixels
    return warmness_coldness_score

def calculate_colorfulness(image_src):
    image = Image.open(image_src)

    image_rgb = image.convert('RGB')
    pixels = np.array(image_rgb)
    
    # Calculate color variance (colorfulness)
    r, g, b = pixels[:,:,0], pixels[:,:,1], pixels[:,:,2]
    colorfulness_score = np.std(r) + np.std(g) + np.std(b)
    
    return colorfulness_score



