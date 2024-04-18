import cv2
import numpy as np

def resize_image(image, width, height, dest_path):
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA) #INTER_NEAREST?
    cv2.imwrite(dest_path, resized_image)
    return resized_image

def divide_image(image, dest_path):
    divided_img = np.divide(image, 2)
    cv2.imwrite(dest_path, divided_img)
    return divided_img

def main():
    # Load an image
    image_path = 'birds.png'  
    image = cv2.imread(image_path)

    # Resize
    img_resized = resize_image(image, 300, 300, 'birds_resized.png')
    
    # Resize
    img_divided = divide_image(img_resized,'birds_divided.png')

if __name__ == "__main__":
    main()