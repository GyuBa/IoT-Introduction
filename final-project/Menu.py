from actuator import Actuator
class Menu:
    def __init__(self, actuator:Actuator):
        self.actuator = actuator
        self.shoeCase = [False] * 2

    def menu(self):
        pass

    def userInput(self):
        return int(input("선택 >"))
