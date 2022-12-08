from Sender import Sender
from device import Device

if __name__ == "__main__":
    device = Device("device", 3, [1, 2], 21)
    sender = Sender(device, "192.168.111.48")

    try:
        while True:
            sender.sendFan()
            sender.sendDeodorantIsEmpty()
            sender.sendInShoe()
    except KeyboardInterrupt:
        sender.stop()
