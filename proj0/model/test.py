from keras.models import load_model
from keras.utils import img_to_array
from keras.utils import load_img
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def predict_image(model, image_path: str): 
    image = load_img(image_path, target_size=(200, 200))
    input_arr = img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)
    return predictions[0][0]  # return the prediction value

# Main function
def main():
    model = load_model('model/model2.keras', compile=False)  # Load your model
    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

    # Test the model on all data from the dataset_dogs_vs_cats/test folder
    test_datagen = ImageDataGenerator(rescale=1.0/255.0)
    test_it = test_datagen.flow_from_directory('dataset_dogs_vs_cats/test/',
                                               class_mode='binary', batch_size=64, target_size=(200, 200),
                                               shuffle=False)  # Set shuffle=False to maintain order

    # Evaluate model on test data and print accuracy
    _, acc = model.evaluate(test_it, verbose=1)
    print(f'Model Accuracy on Test Data: {acc * 100:.2f}%')

    # Save predictions to a text file
    # with open('predictions.txt', 'w') as f:
    #     f.write("Filename\tPredicted\tActual\n")
    #     for i in range(len(test_it.filenames)):
    #         filename = test_it.filenames[i]
    #         actual_label = test_it.labels[i]
    #         predicted_label = predict_image(model, 'dataset_dogs_vs_cats/test/' + filename)
    #         f.write(f"{filename}\t{predicted_label}\t{actual_label}\n")
    # print("Predictions saved to 'predictions.txt'")

if __name__ == '__main__':
    main()
