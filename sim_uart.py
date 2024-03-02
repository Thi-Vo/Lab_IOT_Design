import serial.tools.list_ports
import time

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return "COM5"

ser = None

def connect_to_port():
    port = getPort()    
    global ser
    ser = serial.Serial(port , baudrate =115200)
    if(ser is not None):
        print("Successfully connected to", port)

mess = ""
def read_from_port(client):
    global ser
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            # processData("test",mess[start:end + 1])    #for testing
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]


def processData(client, data):
    if data == "":
        return
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "TEMP":
        # print("TEMP", splitData[2])     #for testing
        client.MQTT_Pub("lab1-iot.cambien1", splitData[2])
        print("Pulished to temp")
    elif splitData[1] == "HUMID":
        # print("HUMID", splitData[2])    #for testing
        client.MQTT_Pub("lab1-iot.cambien2", splitData[2])
        print("Pulished to humidity")
    elif splitData[1] == "BRIGHT":
        # print("BRIGHT", splitData[2])    #for testing
        client.MQTT_Pub("lab1-iot.cambien3", splitData[2])
        print("Pulished to brightness")
    else:
        # print(splitData[1],':', splitData[2])   #for testing
        print("Undefined command")


#test main flow
# connect_to_port()
# while True:
#     read_from_port()
#     time.sleep(1)