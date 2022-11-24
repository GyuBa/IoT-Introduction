from sensor import WaterSensor, ForceSensor

if __name__ == "__main__":
    water1 = WaterSensor.WaterSensor(0)
    water2 = WaterSensor.WaterSensor(1)

    force1 = ForceSensor.ForceSensor(2)
    force2 = ForceSensor.ForceSensor(3)

    print("water : ", water1.getData())
    print("water : ", water2.getData())
    print("force : ", force1.getData())
    print("force : ", force2.getData())