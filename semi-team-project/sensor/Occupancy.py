import paho.mqtt.client as mqtt
import random
import time

#사람 존재 여부 값 반환
def getHumanExisting():
    return random.randrange(0, 2)

if __name__ == "__main__":
    #호스트 등록
    host = '192.168.230.48'
    #클라이언트 생성
    mqttc = mqtt.Client("human_detect_sensor")
    #클라이언트 연결
    mqttc.connect(host)
    #루프 시작
    mqttc.loop_start()

    try:
        while True:
            #사람 존재여부 값 저장
            data = getHumanExisting()

            #값 publish
            mqttc.publish("home/occupancy", data)

            #전달한 data 출력
            print("Publish : ", data)
            #2초간 정지
            time.sleep(2)

    except KeyboardInterrupt: #키보드 종료시 종료
        print("Finished!")
        mqttc.loop_stop()