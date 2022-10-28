import paho.mqtt.client as mqtt

prev = '0'

def occupancy_on_connect(client, userdata, flags, rc):
    client.subscribe("home/occupancy")

def on_message(client, userdata, msg):  # 구독한 Topic의 메시지 출력
    global prev
    data = str(msg.payload)[2]
    if data != prev:
        if data == str('0'):
            client.publish("home/light", "off")
        else:
            client.publish("home/light", "on")
    prev = data



if __name__ == "__main__":
    occupancy = mqtt.Client("Occpancy_Home")
    occupancy.on_connect = occupancy_on_connect
    occupancy.on_message = on_message

    occupancy.connect("localhost")

    try:
        occupancy.loop_forever()

    # Ctrl + C를 입력하여 종료
    except KeyboardInterrupt:
        print("Finished!")
        occupancy.unsubscribe(["home/occupancy"])
        occupancy.disconnect()
