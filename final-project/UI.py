import paho.mqtt.client as mqtt


class UI:
    def __init__(self):
        self.UIsender = mqtt.Client("UI")
        self.UIsender.on_message = self._onMessage
        self.UIsender.on_connect = self._onConnect
        self.address = "192.168.235.48"
        self.UIsender.connect(self.address)
        self.device = ["device1", "device2"]

    def menu(self):
        userSelCase = self.caseSelect()
        self.UIsender.publish(f"{self.device[userSelCase-1]} / open", userSelCase)

    def caseSelect(self):
        print("where open you want?")
        print("1 case")
        print("2 case")
        return int(input("선택 > "))

    def _onMessage(self):
        pass

    def _onConnect(self):
        print("UI onConnect")


if __name__ == "__main__":
    ui = UI()
    while True:
        ui.menu()

