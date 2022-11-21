import paho.mqtt.client as mqtt

#이전 사람정보, 온도, 습도 값 저장
prev = '0'
temp = 0
humi = 0

#subscribe 하는 토픽 등록
request_list = [("home/temperature", 0),
                ("home/humidity", 0),
                ("home/occupancy", 0)]

# 연결시 동작하는 콜백함수
def occupancy_on_connect(client, userdata, flags, rc):
    #토픽 subscribe
    for _ in request_list:
        client.subscribe(_)

#메시지 받으면 동작하는 콜백함수
def on_message(client, userdata, msg):
    #이전 정보 저장
    global prev
    # 만일 받은 msg 토픽이 occupancy 일경우
    if msg.topic == "home/occupancy":
        #전달받은 값 0, 1을 받아서
        data = str(msg.payload)[2]
        #비교 후 publish
        if data != prev:
            if data == str('0'):
                client.publish("home/light", "off")
            else:
                client.publish("home/light", "on")
        #현재값 저장
        prev = data
    #받은 토픽이 온도, 습도일 경우
    else:
        global humi
        global temp
        #값 저장후 int로 변환
        data = int(str(msg.payload)[2:-1])
        # 각각의 토픽에 따라 값 저장
        if msg.topic == "home/temperature":
            temp = data
        elif msg.topic == "home/humidity":
            humi = data
        airConditionalController(client)

#에어컨 제어
def airConditionalController(client):
    #Debug용 온습도 출력
    print(temp, humi)
    if temp * humi != 0:
        #불쾌지수 계산
        score = 0.81 * temp + (0.01 * humi * (0.99 * temp - 14.3)) + 46.3
        #Debug 불퀴지수 출력
        print(score)
        #낮음이면 off
        if score < 68:
            client.publish("home/airconditioner", "off")
        #보통이면 아무것도 안함
        elif score < 75:
            pass

        #높음, 매우높음 on
        else:
            print("on")
            client.publish("home/airconditioner", "on")

if __name__ == "__main__":
    #클라이언트 생성
    occupancy = mqtt.Client("Occpancy_Home")
    #연결시 동작할 on_connect 콜백함수 등록
    occupancy.on_connect = occupancy_on_connect
    #메시지 받고 동작할 on_message 콜백함수 등록
    occupancy.on_message = on_message
    #호스트 등록
    occupancy.connect("192.168.230.48")

    try:
        #무한 동작
        occupancy.loop_forever()

    # Ctrl + C를 입력하여 종료
    except KeyboardInterrupt:
        print("Finished!")
        occupancy.unsubscribe(["home/occupancy"])
        occupancy.disconnect()
