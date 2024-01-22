import sys
import time
import random
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["lab1-iot.nutnhan1","lab1-iot.nutnhan2"]
AIO_USERNAME = "ShiroNeko"
AIO_KEY = "aio_Ultr72tZ2mDsAMEMsH6cOTp2G9v7"

def connected(client):
    print("Ket noi server thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe topic thanh cong!!")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan gia tri: " + payload + " tu \"" + feed_id + "\"")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

cnt = 10
while True:
    cnt = cnt-1
    if cnt <=0 :
        cnt = 10
        print("Publishing data...")
        temp = random.randint(-10,50)
        humid = random.randint(50,100)
        brt = random.randint(0,100)
        client.publish("lab1-iot.cambien1",temp)
        client.publish("lab1-iot.cambien2",humid)
        client.publish("lab1-iot.cambien3",brt)
        print("Done publishing!!!")

    time.sleep(1)