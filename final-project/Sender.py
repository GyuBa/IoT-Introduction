import paho.mqtt.client as mqtt
from device import Device


class Sender:
    def __init__(self, device: Device, address:str):
        self.sender = mqtt.Client(device.getName())
        self.sender.on_connect = self._onMessage
        self.sender.on_connect = self._onConnect
        self.device = device
        self.name = device.getName()
        self.address = address
        self.sender.connect(self.address)

    def sendFan(self):
        if self.device.checkTempHumidity():
            self.sender.publish(self.name + "/fan", "RUN")
        else:
            self.sender.publish(self.name + "/fan", "STOP")

    def sendDeodorantIsEmpty(self):
        if self.device.getDeodorantEmpty():
            self.sender.publish(self.name + "/deodorant", "EMPTY")
        else:
            self.sender.publish(self.name + "/deodorant", "FULL")

    def sendInShoe(self):
        for _ in self.device.getForcePinList():
            if self.device.inShoe(_):
                self.sender.publish(self.name + "/close", str(_))

    def _onMessage(self):
        pass

    def _onConnect(self, client, userdata, flags, rc):
        pass

    def stop(self):
        self.device.clear()