import cv2
import numpy as np

def resize_image(image, width, height, dest_path):
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA) #INTER_NEAREST?
    cv2.imwrite(dest_path, resized_image)
    return resized_image



def main():
    # Load an image
    image_path = 'birds.png'  
    image = cv2.imread(image_path)

    # Resize
    img_resized = resize_image(image, 300, 300, 'birds_resized.png')
    

if __name__ == "__main__":
    main()