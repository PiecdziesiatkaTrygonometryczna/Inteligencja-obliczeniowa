from imageai.Detection import ObjectDetection  

# instantiating the class  
recognizer = ObjectDetection()  

# defining the paths  
path_model = "./models/yolo-tiny.h5"  
path_input = "./input/images.jpg"  
path_output = "./output/newimage.jpg"  

# setting the path of the Model  
recognizer.setModelTypeAsTinyYOLOv3()  
# setting the path of the Model  
recognizer.setModelPath(path_model)  
# loading the model  
recognizer.loadModel()  
# calling the detectObjectsFromImage() function  
recognition = recognizer.detectObjectsFromImage(  
    input_image=path_input,  
    output_image_path=path_output  
)  

# iterating through the items found in the image  
for eachItem in recognition:  
    print(eachItem["name"], ":", eachItem["percentage_probability"])  
