import RPi.GPIO as GPIO
import dht11
import time

class DHT11:
    def __init__(self, pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        self.instance = dht11.DHT11(pin)


# 라즈베리 파이의 GPIO 21번 핀이 DHT 센서의 데이터 핀(2번 핀)에 연결된 상태인 경                                     우
    def getData(self):

        result = self.instance.read()
        while not result.is_valid():
            result = self.instance.read()
        return result.temperature, result.humidity

    def clear(self):
        GPIO.cleanup()
