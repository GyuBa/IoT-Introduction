from Receiver import Receiver
from actuator import Actuator

if __name__ == "__main__":
    actuator = Actuator("actuator_", [18, 19], 25)
    receiver = Receiver(actuator, ["device/open", "device/close", "device/fan", "device/deodorant", "device/open", "device/close"])
    print("START")
    try:
        receiver.run()



    except KeyboardInterrupt:
        receiver.stop()
