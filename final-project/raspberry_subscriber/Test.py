from sensor import WaterSensor, ForceSensor

if __name__ == "__main__":
    water = WaterSensor.WaterSensor()
    force = ForceSensor.ForceSensor()

    print("water : ", water.getData())
    print("force : ", force.getData())