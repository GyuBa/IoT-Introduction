import paho.mqtt.client as mqtt
import random
import time

#랜덤한 온도값 반환
def getTemperature():
    return random.randrange(15, 36)

#랜덤한 습도값 반환
def getHumidity():
    return random.randrange(30, 91)


if __name__ == "__main__":
    #호스트 등록
    host = '192.168.230.48'
    #클라이언트 생성
    mqttc = mqtt.Client("home_status")
    #연결
    mqttc.connect(host)
    #loop 시작
    mqttc.loop_start()

    try:
        while True:
            #온도, 습도 값 저장
            temperature = getTemperature()
            humidity = getHumidity()
            #각각의 값을 publish
            mqttc.publish("home/temperature", temperature)
            mqttc.publish("home/humidity", humidity)
            #각각의 정보를 C, %를 추가해서 출력
            print("home/temperature : ", temperature, "C")
            print("home/humidity", humidity, "%")
            #3초간 정지
            time.sleep(3)

    except KeyboardInterrupt:   #키보드 종료 시 종료
        print("Finished!")
        mqttc.disconnect()
