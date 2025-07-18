#!/usr/bin/python3

import paho.mqtt.client as mqttClient
import time
from blinkstick import blinkstick
from queue import Queue
import statistics
from power_color import color

led_count = 6
sample_count = 120 
q = Queue(maxsize=led_count * sample_count)
blink_limit = 2000

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    # Get reading
    now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    power1 = int(message.payload.decode("utf-8"))
    print('----------------------------')
    print(f'{now_str}: {power1} kW')

    # Save for history
    if (q.full()):
        q.get(0)
    q.put(power1)

    # Display history
    readings = list(q.queue)
    readings.reverse()
    index = 0
    for index in range(led_count):
        reading_index_start = index * sample_count
        reading_index_end = (index + 1) * sample_count - 1
        bucket = readings[reading_index_start:reading_index_end]
        if (len(bucket) > 0):
            c = statistics.mean(bucket)
            print(f'Bucket {index}: {c} kW is {color(c)}')
            bstick.set_color(0, index + 2, hex=color(c))

    # Display current reading
    print(f'NOW: {power1} kW is {color(power1)}')
    if (power1 >= 4000):
        bstick.pulse(0, 0, hex=color(power1), repeats=11, duration=1)
    elif (power1 >= 3000):
        bstick.pulse(0, 0, hex=color(power1), repeats=4, duration=350)
    elif (power1 >= 2000):
        bstick.pulse(0, 0, hex=color(power1), repeats=2, duration=900)
    else:
        bstick.set_color(0, 0, hex=color(power1))


Connected = False   #global variable for the state of the connection
  
broker_address= "127.0.0.1"
port = 1883
user = "emonpi"
password = "emonpimqtt2016"

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect                     #attach function to callback
client.on_message = on_message                     #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

bstick = blinkstick.find_first()

if bstick is None:
    print ("No BlinkSticks found...")
else:
    print ("Displaying Power usage (Blue < 100kW, Green < 200kW...)")
    print ("Press Ctrl+C to exit")

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("emon/emonpi_5/power1")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
