

from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from keras.utils import img_to_array
from keras.utils import load_img
import numpy as np
import os



def main():


  model = load_model('model/model2Copy.keras', compile=False)

  model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

  model.summary()
  model = re_train(model)
  model.summary()
  # predict_image(model, "/dataset_dogs_vs_cats/test/cats/cat.1.jpg")
  # predict_image(model, "/dataset_dogs_vs_cats/test/cats/cat.2.jpg")
  # predict_image(model, "/dataset_dogs_vs_cats/test/cats/cat.4.jpg")
  # predict_image(model, "/dataset_dogs_vs_cats/test/dogs/dog.1472.jpg")
  # predict_image(model, "/dataset_dogs_vs_cats/test/dogs/dog.6933.jpg")
  # predict_image(model, "/dataset_dogs_vs_cats/test/dogs/dog.12499.jpg") 

  # dir = "my_photos"
  # for file in os.listdir(dir):
  #     if os.path.isfile(os.path.join(dir, file)) and file.endswith('.jpg'):
  #         predict_image(model, os.path.join(dir, file))
          
  evaluate(model)


def predict_image(model, image_path:str): 
  image = load_img(image_path, target_size=(200, 200))
  input_arr = img_to_array(image)
  input_arr = np.array([input_arr])  # Convert single image to a batch.
  predictions = model.predict(input_arr)
  print(image_path, predictions)   # 0 kot, 1 pies

def evaluate(model):
  datagen = ImageDataGenerator(rescale=1.0/255.0)
  test_it = datagen.flow_from_directory('dataset_dogs_vs_cats/test/',
    class_mode='binary', batch_size=64, target_size=(200, 200))
  model.evaluate(test_it, verbose=1)

def re_train(model):
  datagen = ImageDataGenerator(rescale=1.0/255.0)
	# prepare iterators
  train_it = datagen.flow_from_directory('dataset_dogs_vs_cats/train/',
		class_mode='binary', batch_size=64, target_size=(200, 200))
  test_it = datagen.flow_from_directory('dataset_dogs_vs_cats/test/',
		class_mode='binary', batch_size=64, target_size=(200, 200))
	# fit model
  model.fit(train_it, steps_per_epoch=len(train_it),
		validation_data=test_it, validation_steps=len(test_it), epochs=6, verbose=1)
  

  return model


if __name__ == '__main__':
  main()