import time

import paho.mqtt.client as mqtt
from actuator import Actuator


class Receiver:
    def __init__(self, actuaotor: Actuator, subscribeList: list):
        self.shoeCaseOpen = None
        self.methodList = {"fan":self.fan, "deodorant":self.alert, "shoe":self.shoeCase, "open":self.shoeCaseOpen}
        self.receiver = mqtt.Client(actuaotor.getName())
        self.subscribeList = subscribeList
        self.receiver.on_connect = self._onMessage
        self.receiver.on_connect = self._onConnect
        self.actuator = actuaotor
        self.name = actuaotor.getName()
        self.address = "localhost"
        self.receiver.connect(self.address)

    def shoeCase(self, data:str):
        if "IN" in data:
            time.sleep(1)
            self.actuator.shoeCaseClose()

    def fan(self, data:str):
        if "RUN" in data:
            self.actuator.fanRun()
        elif "STOP" in data:
            self.actuator.fanStop()


    def alert(self, data:str):
        if "EMPTY" in data:
            print("EMPTY")
        else:
            pass

    def _onMessage(self, client, userdata, msg):
        for topic, method in self.methodList.items():
            if topic in msg.topic:
                data = str(msg.payload)
                method(data)

    def _onConnect(self, client, userdata, flags, rc):
        for _ in self.subscribeList:
            self.receiver.subscribe(_)

    def run(self):
        self.receiver.loop_start()

    def stop(self):
        self.receiver.disconnect()
        for _ in self.subscribeList:
            self.receiver.unsubscribe(_)
            self.receiver.loop_stop()

