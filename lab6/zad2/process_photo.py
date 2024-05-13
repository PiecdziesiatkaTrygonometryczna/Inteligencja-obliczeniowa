import cv2
import numpy as np

# Load the image
image = cv2.imread('original.png')

# Define custom weights for each channel
weights = [0.114, 0.587, 0.299]

# Split the image into its RGB channels
B, G, R = cv2.split(image)

# Multiply each channel by its corresponding weight
weighted_channels = [
    np.multiply(R, weights[0]),
    np.multiply(G, weights[1]),
    np.multiply(B, weights[2])
]

# Sum up the weighted channels to get the grayscale image
gray_image = sum(weighted_channels)

# Convert to uint8 (8-bit) data type
gray_image = np.uint8(gray_image)

# Save the grayscale image to a file
cv2.imwrite('improved_wages.jpg', gray_image)

print("Grayscale image saved successfully.")
