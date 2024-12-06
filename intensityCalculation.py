from tensorflow.keras.applications import vgg16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
from PIL import Image, ImageOps
import numpy as np

base_model = vgg16.VGG16(weights='imagenet', include_top=False)

layer_name = 'block3_conv3'  # Mid-level layer capturing textures and patterns
model = Model(inputs=base_model.input, outputs=base_model.get_layer(layer_name).output)

def resize_with_padding(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = ImageOps.fit(img, target_size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    return img

def preprocess_image(image_path, target_size=(224, 224)):
    img = resize_with_padding(image_path, target_size)  # Maintain aspect ratio
    img_array = np.array(img)  # Convert to NumPy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return preprocess_input(img_array)  # Normalize for VGG16

# Extract features
def extract_features(image_path):
    preprocessed_image = preprocess_image(image_path)
    feature_maps = model.predict(preprocessed_image)  # Shape: (1, height, width, channels)
    density = np.mean(feature_maps)  # Average 
    return density

def normalize_dict_values(my_dict, new_min=0, new_max=1):
    # Get the minimum and maximum values in the dictionary
    old_min = min(my_dict.values())
    old_max = max(my_dict.values())

    # Normalize each value
    normalized_dict = {
        key: int(new_min + (value - old_min) / (old_max - old_min) * (new_max - new_min))
        for key, value in my_dict.items()
    }
    return normalized_dict



