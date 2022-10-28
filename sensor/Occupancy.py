import paho.mqtt.client as mqtt
import random
import time

def getHumanExisting():
    return random.randrange(0, 2)

if __name__ == "__main__":
    mqttc = mqtt.Client("human_detect_sensor")
    mqttc.connect('localhost')
    mqttc.loop_start()

    try:
        while True:
            data = getHumanExisting()
            (result, m_id) = mqttc.publish("home/occupancy", data)
            print("Publish : ", data)
            time.sleep(2)

    except KeyboardInterrupt:
        print("Finished!")
        mqttc.loop_stop()