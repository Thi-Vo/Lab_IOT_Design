import sys
import time
import random

from mqtt import *
import google_ai as ai
from sim_uart import *

AIO_FEED_ID = ["lab1-iot.nutnhan1","lab1-iot.nutnhan2"]
AIO_USERNAME = "ShiroNeko"
AIO_KEY = "aio_FotU35G1kvV7GpzbEwahTUrXzT3Y"
# AIO_KEY = (base64.b64decode(AIO_KEY.encode("utf-8"))).decode("utf-8")


#In this case,
#Data is collected from sensor and publish with a period time.sleep()
#AI_recognition is publish with a period STAMP*time.sleep() to reduce computer load
def main():
    client = myMQTT_CLient(AIO_USERNAME, AIO_KEY)
    client.MQTT_Sub(AIO_FEED_ID)


    STAMP = 6       #STAMP and time.sleep define the period of publishing
    stamp = STAMP 
    connect_to_port()  
    while True:
        stamp = stamp - 1

        read_from_port(client)
        # print("Publishing data...")
        # temp = random.randint(-10,50)
        # humid = random.randint(50,100)
        # brt = random.randint(0,100)
        # client.MQTT_Pub("lab1-iot.cambien1",temp)
        # client.MQTT_Pub("lab1-iot.cambien2",humid)
        # client.MQTT_Pub("lab1-iot.cambien3",brt)
        # print("Done publishing!!!")
        
        if stamp <=0 :
            classname = ai.FaceDetection()
            client.MQTT_Pub("ai-detection", classname)
            print("Publish to AI")
            stamp = STAMP
        
        time.sleep(2)
    ai.StopFaceDetection()


if __name__ == "__main__":
    main()


   