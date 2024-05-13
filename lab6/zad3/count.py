import cv2
import os

def count_black_stains(image_path):
  # Load the image in grayscale
  image = cv2.imread(image_path, 0)

  # Apply thresholding to convert the grayscale image to a binary image
  threshold, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

  # Find contours in the binary image
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Count the number of contours (black stains)
  number_of_stains = len(contours)

  return number_of_stains

def process_images(folder_path):
  for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check image extensions
      image_path = os.path.join(folder_path, filename)
      number_of_stains = count_black_stains(image_path)
      print(f"Image: {filename}, Number of birds: {number_of_stains}")

# Example usage
folder_path = "output_images"
process_images(folder_path)