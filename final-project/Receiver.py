import paho.mqtt.client as mqtt
from actuator import Actuator


class Receiver:
    def __init__(self, actuaotor: Actuator, subscribeList: list):
        self.methodList = {}
        self.receiver = mqtt.Client(actuaotor.getName())
        self.subscribeList = subscribeList
        self.receiver.on_connect = self._onMessage
        self.receiver.on_connect = self._onConnect
        self.actuator = actuaotor
        self.name = actuaotor.getName()
        self.address = "localhost"
        self.receiver.connect(self.address)

    def shoeCase(self):
        pass

    def fan(self):
        pass

    def shoeCaseOpen(self):
        pass

    def shoeCaseClose(self):
        pass

    def fanRun(self):
        pass

    def fanStop(self):
        pass

    def alert(self):
        pass

    def do(self, methodName):
        self.methodList[methodName]()

    def _onMessage(self, client, userdata, msg):
        pass

    def _onConnect(self):
        pass
