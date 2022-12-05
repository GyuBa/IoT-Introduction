from Receiver import Receiver
from actuator import Actuator

if __name__ == "__main__":
    actuator1 = Actuator("device1", 18, 25)
    actuator2 = Actuator("device2", 19, 25)
    receiver1 = Receiver(actuator1, ["device1/fan", "device1/deodorant", "device1/shoe", "device1/open"])
    receiver2 = Receiver(actuator2, ["device2/fan", "device2/deodorant", "device2/shoe", "device2/open"])

    try:
        receiver1.run()
        receiver2.run()

        while True:
            pass

    except KeyboardInterrupt:
        receiver1.stop()
        receiver2.stop()
