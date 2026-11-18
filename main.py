
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os

# Load the pretrained model
print("Loading AI model...")
model = MobileNetV2(weights="imagenet")

print("AI model loaded successfully!")

# Folder containing our images
image_folder = "sample_images"

# Images to classify
images = ["cat.jpg", "dog.jpg", "car.jpg"]

# Classify each image
for image_name in images:

    image_path = os.path.join(image_folder,image_name)

    print("\nClassifying:", image_name)

    # Load and resize image
    image = load_img(image_path, target_size=(224, 224))

    # Convert image into an array
    image_array = img_to_array(image)

    # Prepare image for MobileNetV2
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    predictions = model.predict(image_array, verbose=0)

    # Display top 3 predictions
    results = decode_predictions(predictions, top=3)

    for result in results[0]:
        label = result[1]
        confidence = result[2] * 100

        print(f"{label}: {confidence:.2f}%")
