import time

import paho.mqtt.client as mqtt
from actuator import Actuator


class Receiver:
    def __init__(self, actuaotor: Actuator, subscribeList: list):
        self.methodList = {"fan": self.fan, "deodorant": self.alert, "close": self.shoeCaseClose,
                           "open": self.shoeCaseOpen}
        self.receiver = mqtt.Client(actuaotor.getName())
        self.subscribeList = subscribeList
        self.receiver.on_connect = self._onConnect
        self.receiver.on_message = self._onMessage
        self.actuator = actuaotor
        self.name = actuaotor.getName()
        self.address = "192.168.111.48"
        self.receiver.connect(self.address)

    def shoeCaseOpen(self, data: str):
        self.actuator.shoeCaseOpen(int(data[2]))

    def shoeCaseClose(self, data: str):
        self.actuator.shoeCaseClose(int(data[2]))

    def fan(self, data: str):
        if "RUN" in data:
            self.actuator.fanRun()
        elif "STOP" in data:
            self.actuator.fanStop()

    def alert(self, data: str):
        if "EMPTY" in data:
            print("EMPTY")
        else:
            pass

    def _onMessage(self, client, userdata, msg):
        print("onMessage")
        for topic, method in self.methodList.items():
            if topic in msg.topic:
                data = str(msg.payload)
                method(data)

    def _onConnect(self, client, userdata, flags, rc):
        print("connect")
        for _ in self.subscribeList:
            self.receiver.subscribe(_)

    def run(self):
        print("run")
        self.receiver.loop_forever()

    def stop(self):
        self.actuator.stop()
        self.receiver.disconnect()
        for _ in self.subscribeList:
            self.receiver.unsubscribe(_)
            self.receiver.loop_stop()
