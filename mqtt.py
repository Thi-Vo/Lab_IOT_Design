import sys
from Adafruit_IO import MQTTClient
import time



class myMQTT_CLient:
    def connected(self, client):
        print("Ket noi server thanh cong ...")
        # for topic in AIO_FEED_ID:
        #     client.subscribe(topic)

    def subscribe(self, client, userdata , mid , granted_qos):
        # print("Subscribe topic thanh cong!!", mid)
        pass

    def disconnected(self, client):
        print("Ngat ket noi!!")
        sys.exit (1)

    def message(self, client, feed_id , payload):
        print("Nhan gia tri: " + payload + " tu \"" + feed_id + "\"")

    def MQTT_Pub(self, topic, data):
        self.client.publish(topic, data)

    def MQTT_Sub(self, topic):
        for i in topic:
            self.client.subscribe(i)
            print("Subcribe topic:", i)

    def __init__(self, username, key):
        # global AIO_KEY
        self.client = MQTTClient (username , key)
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()