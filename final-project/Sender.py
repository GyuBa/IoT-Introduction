import paho.mqtt.client as mqtt
from device import Device


class Sender:
    def __init__(self, device: Device, publishList: list):
        self.subscribeList = publishList
        self.sender = mqtt.Client(device.getName())
        self.sender.on_connect = self._onMessage
        self.sender.on_connect = self._onConnect
        self.device = device
        self.name = device.getName()
        self.address = "localhost"
        self.sender.connect(self.address)

    def sendTemperature(self):
        self.sender.publish(self.name+"/temperature", self.device.getTemperatureSensor())

    def sendHumidity(self):
        self.sender.publish(self.name+"/humidity", self.device.getHumidity())

    def sendDeodorantIsEmpty(self):
        if self.device.getDeodorantEmpty():
            self.sender.publish(self.name + "/deodorant", "EMPTY")

        else:
            self.sender.publish(self.name + "/deodorant", "NONE")

    def sendInShoe(self):
        if self.device.inShoe():
            self.sender.publish(self.name + "/shoe", "IN")
        else:
            self.sender.publish(self.name + "/shoe", "NONE")

    def _onMessage(self):
        pass

    def _onConnect(self):
        pass
