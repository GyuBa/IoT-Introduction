import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("home/light")


def on_message(client, userdata, msg):
    print(msg.payload)
client = mqtt.Client("AirConditioner")

client.on_connect = on_connect
client.connect("localhost")