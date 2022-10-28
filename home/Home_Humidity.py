import paho.mqtt.client as mqtt

temp = 0
humi = 0

request_list = [("home/temperature", 0),
                ("home/humidity", 0)]

def on_connect(client, userdata, flags, rc):
    for _ in request_list:
        client.subscribe(_)

def on_message(client, userdata, msg):  # 구독한 Topic의 메시지 출력
    global humi
    global temp
    data = int(str(msg.payload)[2:-1])

    if msg.topic == "home/temperature":
        temp = data
    elif msg.topic == "home/humidity":
        humi = data
    airConditionalController(client)



def airConditionalController(client):
    print(temp, humi)
    if temp * humi != 0:
        score = 0.81 * temp + 0.01 * humi
        print(score)
        if score < 68:
            client.publish("home/airconditioner", "off")
        elif score < 75:
            pass
        else:
            print("on")
            client.publish("home/airconditioner", "on")

if __name__ == "__main__":
    host = "localhost"
    client = mqtt.Client("Humidity_Home")

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host)

    try:
        client.loop_forever()

    # Ctrl + C를 입력하여 종료
    except KeyboardInterrupt:
        print("Finished!")
        client.unsubscribe(["home/temperature"])
        client.unsubscribe(["home/humidity"])
        client.disconnect()
