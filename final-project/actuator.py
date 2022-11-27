from device import Device

class Actuator:
    def __init__(self, name:str):
        self.name = name

    def getName(self):
        return self.name

    def shoeCaseOpen(self):
        pass

    def shoeCaseClose(self):
        pass

    def fanRun(self):
        pass

    def fanStop(self):
        pass

    def alert(self):
        pass
