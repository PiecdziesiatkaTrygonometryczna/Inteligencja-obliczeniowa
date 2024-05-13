# pip install opencv-python
import cv2
import numpy as np




def main():
    # Load an image
    image_path = 'birds.png'  
    image = cv2.imread(image_path)

    # Info on image
    print(type(image))
    print(image.ndim)
    print(image.shape)

    print(image[0, 0])


if __name__ == "__main__":
    main()