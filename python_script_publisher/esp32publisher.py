import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.hivemq.com", 1883, 8000)

# send a message to the raspberry/topic every 1 second, 5 times in a row
while True:
    data = input("Please Enter value which you want send to Broker on OR off : ")
    brk_data = input("Please Enter c to continue and e to exit loop: ")
    if brk_data == 'c':
        if data == 'on':
            # the four parameters are topic, sending content, QoS and whether retaining the message respectively
            client.publish('esp32/value_', payload=data, qos=0, retain=False)
            print(f"send {data} to esp32/value_")
            time.sleep(1)
            data = ''
        elif data == 'off':
            # the four parameters are topic, sending content, QoS and whether retaining the message respectively
            client.publish('esp32/value_', payload=data, qos=0, retain=False)
            print(f"send {data} to esp32/value_")
            time.sleep(1)
            data = ''
    elif brk_data == 'e':
        break
    
    client.loop(1)