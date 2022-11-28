from sensor import WaterSensor, ForceSensor
from sensor import DHT11
if __name__ == "__main__":
    dht = DHT11.DHT11(21)

    print(dht.getData())