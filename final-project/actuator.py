import RPi.GPIO as GPIO
import time

class Actuator:
    def __init__(self, name:str, servoPin:int, fanpin:int):
        self.name = name
        GPIO.setup(fanpin,GPIO.OUT)
        self.pin = servoPin
        self.fanPin = fanpin
        self.SERVO_MAX_DUTY = 12  # servo max frequency
        self.SERVO_MIN_DUTY = 3  # servo min frequency
        self.servo = GPIO.PWM(servoPin, 50)

        self.servo.start(0)

    def getName(self):
        return self.name

    def shoeCaseOpen(self):
        for i in range(1, 130):
            duty = self.SERVO_MIN_DUTY + (i * (self.SERVO_MAX_DUTY - self.SERVO_MIN_DUTY) / 180.0)
            self.servo.ChangeDutyCycle(duty)
            time.sleep(0.02)
        time.sleep(1)

    def shoeCaseClose(self):
        for i in range(130, 1, -1):
            duty = self.SERVO_MIN_DUTY + (i * (self.SERVO_MAX_DUTY - self.SERVO_MIN_DUTY) / 180.0)
            self.servo.ChangeDutyCycle(duty)
            time.sleep(0.02)
        time.sleep(1)

    def fanRun(self):
        GPIO.output(self.fanPin, True)

    def fanStop(self):
        GPIO.output(self.fanPin, False)

    def alert(self):
        pass
