from Sender import Sender
from device import Device

if __name__ == "__main__":
    device1 = Device("device1")
    device2 = Device("device2")
    sender1 = Sender(device1, 3, 1, 21)
    sender2 = Sender(device2, 3 ,2, 21)

    try:
        while True:
            sender1.sendFan()
            sender1.sendDeodorantIsEmpty()
            sender1.sendInShoe()
            sender2.sendFan()
            sender2.sendDeodorantIsEmpty()
            sender2.sendInShoe()
    except KeyboardInterrupt:
        sender1.stop()
        sender2.stop()
