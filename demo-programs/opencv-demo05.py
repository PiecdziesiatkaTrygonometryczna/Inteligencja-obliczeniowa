import cv2
import numpy as np


def main():
    # Load an image
    image_path = 'birds.png'  
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (700, 700), interpolation=cv2.INTER_AREA) 
    
    # Simple Thresholding
    # Pixels above the threshold are set to the maximum value, and others are set to 0.
    _, simple_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Adaptive Thresholding
    # The threshold value is determined for smaller regions. 
    # This allows for varying lighting conditions across different areas of the image.
    adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                            cv2.THRESH_BINARY, 11, 2)

    # Apply Otsu's thresholding
    # Automatically determines the optimal threshold value for the entire image.
    _, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
 
    # Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the images
    cv2.imshow('Original Image', image)
    cv2.imshow('Simple Thresholding', simple_thresh)
    cv2.imshow('Adaptive Thresholding', adaptive_thresh)
    cv2.imshow('Otsu Thresholding', otsu_thresh)
    cv2.imshow('Gaussian Blur', gaussian_blur)

   # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


