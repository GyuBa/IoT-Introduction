import paho.mqtt.client as mqtt
from device import Device


class Receiver:
    def __init__(self):
        self.methodList = {}

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