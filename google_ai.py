from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import base64
import time

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
# Load the model
model = load_model("keras_model.h5", compile=False)
# Load the labels
class_names = open("labels.txt", "r").readlines()
# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)


def FaceDetection():
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    
    # Backup data for post-processing
    data = image
    

    # Make the image a numpy array and reshape it to the models input shape.
    # (batch size, x, y , RGB channels)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)      

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    
    confidence_score = prediction[0][index]
    
    class_name = class_names[index]

    # Print prediction and confidence score
    print("Result:", class_name)
    # print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")


    # #Listen to the keyboard for presses.
    # keyboard_input = cv2.waitKey(1)

    # # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
    #     break



    # Show the image in a window
    # cv2.putText(data, class_name, (80, 40), cv2.FONT_ITALIC, 0.8, (76, 219, 224), 1)
    # cv2.imshow("Webcam Image", data)
    # base64 encoded data for uploading to platform
    # r,data = cv2.imencode(".jpg", data, [cv2.IMWRITE_JPEG_QUALITY, 50])
    # data = base64.b64encode(data)



    cv2.waitKey(1000)
    return class_name

def StopFaceDetection():
    camera.release()
    cv2.destroyAllWindows()



# # For TESTING
# while True:
#     mydata, classname = FaceDetection()
#     print (classname)
#     time.sleep(2)