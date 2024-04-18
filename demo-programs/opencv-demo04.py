import cv2
import numpy as np

def resize_image(image, width, height, dest_path):
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA) 
    cv2.imwrite(dest_path, resized_image)
    return resized_image

def gray_image(image, dest_path):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # how is this computed?
    cv2.imwrite(dest_path, gray_image)
    return gray_image

def main():
    # Load an image
    image_path = 'birds.png'  
    image = cv2.imread(image_path)

    # Resize
    img_resized = resize_image(image, 300, 300, 'birds_resized.png')
    
    # Convert to grayscale
    img_gray = gray_image(img_resized, 'birds_gray.png')
    # Info on image
    print(type(img_gray))
    print(img_gray.ndim)
    print(img_gray.shape)
    print(img_gray[0, 0])

if __name__ == "__main__":
    main()










#Gray = 0.299*Red + 0.587*Green + 0.114*Blue