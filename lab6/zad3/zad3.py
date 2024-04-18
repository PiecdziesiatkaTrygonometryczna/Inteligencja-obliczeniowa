import os
import cv2
import numpy as np

def main():
    # Input and output folders
    input_folder = 'bird_miniatures'
    output_folder = 'output_images'

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load an image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (700, 700), interpolation=cv2.INTER_AREA)

            # Simple Thresholding
            _, simple_thresh = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, simple_thresh)

            print(f"Processed {filename} and saved to {output_path}")

if __name__ == "__main__":
    main()
