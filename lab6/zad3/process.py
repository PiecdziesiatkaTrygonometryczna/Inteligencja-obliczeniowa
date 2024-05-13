import cv2
import numpy as np
import os
import shutil

input_folder = 'bird_miniatures'
output_folder = 'output_images'

# Clear the output folder
shutil.rmtree(output_folder, ignore_errors=True)  # Delete if it exists
os.makedirs(output_folder)  # Create it fresh

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        filepath = os.path.join(input_folder, filename)

        # Load the image
        image = cv2.imread(filepath)

        # Convert to grayscale if necessary
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        # Calculate the histogram
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

        # Find bin with the most pixels
        max_index = np.argmax(hist)
        max_value = hist[max_index][0]

        # Apply thresholding (dynamically based on histogram)
        threshold_value = max_index - 10
        ret, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

        # Save the thresholded image
        output_filename = os.path.splitext(filename)[0] + '_thresholded.jpg'
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, thresh)
