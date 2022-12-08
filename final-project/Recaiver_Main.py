from Receiver import Receiver
from actuator import Actuator

if __name__ == "__main__":
    actuator = Actuator("actuator", [18, 19], 25)
    receiver = Receiver(actuator, ["device/fan", "device/deodorant", "device/open", "device/close"])
    try:
        receiver.run()

        while True:
            pass

    except KeyboardInterrupt:
        receiver.stop()
