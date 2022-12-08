import RPi.GPIO as GPIO
import time


class Actuator:
    def __init__(self, name: str, servoPin: list, fanpin: int):
        self.name = name
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(fanpin, GPIO.OUT)
        GPIO.setup(servoPin[0], GPIO.OUT)
        GPIO.setup(servoPin[1], GPIO.OUT)

        self.fanPin = fanpin
        self.SERVO_MAX_DUTY = 12  # servo max frequency
        self.SERVO_MIN_DUTY = 3  # servo min frequency
        self.servo = [GPIO.PWM(servoPin[0], 50), GPIO.PWM(servoPin[1], 50)]
        self.servo[0].start(0)
        self.servo[1].start(0)

    def getName(self):
        return self.name

    def shoeCaseOpen(self, index: int):
        for i in range(130, 1, -1):
            duty = self.SERVO_MIN_DUTY + (i * (self.SERVO_MAX_DUTY - self.SERVO_MIN_DUTY) / 180.0)
            self.servo[index - 1].ChangeDutyCycle(duty)
            time.sleep(0.02)

    def shoeCaseClose(self, index: int):
        for i in range(1, 130):
            duty = self.SERVO_MIN_DUTY + (i * (self.SERVO_MAX_DUTY - self.SERVO_MIN_DUTY) / 180.0)
            self.servo[index - 1].ChangeDutyCycle(duty)
            time.sleep(0.02)

    def fanRun(self):
        GPIO.output(self.fanPin, True)

    def fanStop(self):
        GPIO.output(self.fanPin, False)

    def alert(self):
        pass

    def stop(self):
        self.servo[0].stop()
        self.servo[1].stop()
        GPIO.cleanup()
