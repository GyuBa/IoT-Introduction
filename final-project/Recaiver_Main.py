from Receiver import Receiver
from actuator import Actuator

if __name__ == "__main__":
    actuator = Actuator("Moter-Move")
    receiver = Receiver(actuator, ["device/fan", "device/deodorant", "device/shoe"])

    try:
        receiver.run()

    except KeyboardInterrupt:
        receiver.stop()
