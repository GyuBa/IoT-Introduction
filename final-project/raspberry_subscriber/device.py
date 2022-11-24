import paho.mqtt.client as mqtt


class Device:
    def __init__(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def getWaterSensor(self):
        pass

    def getTemperatureSensor(self):
        pass

    def getHumidity(self):
        pass

    def getDeodorantEmpty(self):
        pass

    def inShoe(self):
        pass