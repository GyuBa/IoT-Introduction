import paho.mqtt.client as mqtt
import random
import time

def getTemperature():
    return random.randrange(15, 36)


def getHumidity():
    return random.randrange(30, 91)


if __name__ == "__main__":
    mqttc = mqtt.Client("home_status")
    mqttc.connect('localhost')
    mqttc.loop_start()

    try:
        while True:
            temperature = getTemperature()
            humidity = getHumidity()

            mqttc.publish("home/temperature", temperature)
            mqttc.publish("home/humidity", humidity)

            print("home/temperature : ", temperature, "C")
            print("home/humidity", humidity, "%")
            time.sleep(3)

    except KeyboardInterrupt:
        print("Finished!")
        mqttc.disconnect()
