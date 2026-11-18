# Image Classification Using a Pretrained Model

1. Project Description

This project uses Artificial Intelligence to identify objects in images using Python, TensorFlow and a pretrained model called MobileNetV2.

2. How the Pretrained Model Works

A pretrained model is an AI model that has already been trained using many images.

In my project, I used MobileNetV2. Instead of training a new model, I used the knowledge that MobileNetV2 had already learned.

First, my program loads an image and resizes it to 224 × 224 pixels. Then, it prepares the image and sends it to the model.

MobileNetV2 analyzes the image and predicts the possible object categories. Finally, my program displays the predicted labels and their confidence percentages.

## 3. Technologies Used

- Python 3.13
- TensorFlow 2.21.0
- MobileNetV2
- Pillow
- Visual Studio Code

4. Sample Images

The project uses three sample images:

- cat.jpg
- dog.jpg
- car.jpg

 5. Sample Results

| Image | Predicted Label | Confidence |
|---|---|---:|
| cat.jpg | Egyptian_cat | 29.37% |
| dog.jpg | Rhodesian_ridgeback | 28.30% |
| car.jpg | sports_car | 36.36% |

6. How to Run the Project

1. Install Python.
2. Create a virtual environment.
3. Install the required libraries using:

   `py -m pip install -r requirements.txt`

4. Run the program:

   `py main.py`

 7. Conclusion

This project helped me understand how pretrained AI models can identify objects in images. I learned how to use MobileNetV2, process images and display predictions using Python.