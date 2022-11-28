from Sender import Sender
from device import Device

if __name__ == "__main__":
    device = Device("device")
    sender = Sender(device)

    try:
        while True:
            sender.sendFan()
            sender.sendDeodorantIsEmpty()
            sender.sendInShoe()
    except KeyboardInterrupt:
        sender.stop()
