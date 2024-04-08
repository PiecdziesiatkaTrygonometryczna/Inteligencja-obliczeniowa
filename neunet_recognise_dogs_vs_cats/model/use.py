from keras.models import load_model
from matplotlib import pyplot
from matplotlib.image import imread
from keras.utils import img_to_array
from keras.utils import load_img
import numpy as np
import os
import math
from skimage.transform import resize


def plot_images(image_paths, model):
    # Calculate the number of rows and columns dynamically based on the number of images
    num_images = len(image_paths)
    num_columns = int(math.sqrt(num_images) + 1)  # Number of columns per row
    num_rows = (num_images + num_columns - 1) // num_columns  # Round up division
    
    # Set the figure size based on the number of rows and columns
    fig_height = 2 * num_rows  # Adjust the multiplier as needed for desired height
    fig_width = 2 * num_columns  # Adjust the multiplier as needed for desired width
    pyplot.figure(figsize=(fig_width, fig_height))  # Adjust figure size as needed

    # Plot images
    for i, filename in enumerate(image_paths):
        # Define subplot
        pyplot.subplot(num_rows, num_columns, i + 1)
        # Load image pixels
        image = imread(filename)
        aspect_ratio = image.shape[1] / image.shape[0]
        width = int(150 * aspect_ratio)
        image = resize(image, (150, width))  # Resize image to desired height and calculated width
        # Plot raw pixel data
        pyplot.imshow(image)
        pyplot.axis('off')  # Remove axes for cleaner display
        # Predict the image
        prediction = predict_image(model, filename)
        animal = "Cat" if prediction <= 0.5 else "Dog"
        # Set the title to the prediction value
        pyplot.title(f'{animal} ({"{:.2f}".format(prediction)})', fontsize=12)

    # save the figure
    pyplot.tight_layout()
    pyplot.savefig("plot.png")

def predict_image(model, image_path:str): 
    image = load_img(image_path, target_size=(200, 200))
    input_arr = img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)
    return predictions[0][0]  # return the prediction value

# main function
def main():

    model = load_model('model/model2.keras', compile=False) # insert name of a model

    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

    image_paths = [ # insert paths to all images to predict animals from
        # "./dataset_dogs_vs_cats/test/cats/cat.359.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.288.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.2805.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.683.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.859.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.1041.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.1168.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.837.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.940.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.1408.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.1917.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.2002.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.2206.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.304.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.694.jpg",
        # "./dataset_dogs_vs_cats/test/cats/cat.763.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.1162.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.1427.jpg",
        # "./dataset_dogs_vs_cats/test/dogs/dog.2235.jpg"
    ]

    dirs = ["tescik"] # insert directories to predict animals from all .jpg images from that directories
    for dir in dirs:
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, file)) and file.endswith('.jpg'): # you can also add: and file.endswith('.png') to predict from png images
                image_paths.append(os.path.join(dir, file))

    plot_images(image_paths, model)

if __name__ == '__main__':
    main()
