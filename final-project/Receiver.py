import paho.mqtt.client as mqtt
from actuator import Actuator


class Receiver:
    def __init__(self, actuaotor: Actuator, subscribeList: list):
        self.methodList = {"fan":self.fan, "deodorant":self.alert, "shoe":self.shoeCase}
        self.receiver = mqtt.Client(actuaotor.getName())
        self.subscribeList = subscribeList
        self.receiver.on_connect = self._onMessage
        self.receiver.on_connect = self._onConnect
        self.actuator = actuaotor
        self.name = actuaotor.getName()
        self.address = "localhost"
        self.receiver.connect(self.address)

    def shoeCase(self, data:str):
        print("shoe-case", data)

    def fan(self, data:str):
        print("fan", data)

    def shoeCaseOpen(self):
        print("case-open")

    def shoeCaseClose(self):
        print("case-close")

    def fanRun(self):
        print("fan-run")

    def fanStop(self):
        print("fan-stop")

    def alert(self, data:str):
        print("alert", data)

    def _onMessage(self, client, userdata, msg):
        for topic, method in self.methodList.items():
            if topic in msg.topic:
                data = str(msg.payload)
                method(data)
        print("None")

    def _onConnect(self):
        for _ in self.subscribeList:
            self.receiver.subscribe(_)

    def run(self):
        self.receiver.loop_forever()

    def stop(self):
        self.receiver.disconnect()
        for _ in self.subscribeList:
            self.receiver.unsubscribe(_)

