from builtins import bool

from sensor import WaterSensor, ForceSensor, DHT11


class Device:
    def __init__(self, name: str, waterChannel, forceChannel, dhtPin):
        self.name = name
        self.waterSensor = WaterSensor.WaterSensor(waterChannel)
        self.forceSensor = ForceSensor.ForceSensor(forceChannel)
        self.dht11 = DHT11.DHT11(dhtPin)

    def getName(self):
        return self.name

    def getDeodorantEmpty(self) -> bool:
        if self.waterSensor.getData() < 60:
            return True
        else:
            return False

    def inShoe(self) -> bool:
        if self.forceSensor.getData() > 40:
            return True
        else:
            return False

    def checkTempHumidity(self) -> bool:
        temperature, humidity = self.dht11.getData()

        if temperature > 6:
            return True
        else:
            return False

    def clear(self) -> None:
        self.waterSensor.clear()
        self.forceSensor.clear()
        self.dht11.clear()
