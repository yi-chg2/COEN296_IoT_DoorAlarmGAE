import time, urllib, urllib2
import RPi.GPIO as io
import os

io.setmode(io.BCM)

door_pin1 = 24
led_1 = 16

io.setup(door_pin1, io.IN, pull_up_down=io.PUD_UP)
io.setup(led_1, io.OUT)
var1 = "ON!"
count = 0

def blink_led():
    io.output(led_1, True)
    time.sleep(0.3)
    io.output(led_1, False)
    time.sleep(0.3)
    
while True:
    if io.input(door_pin1):
        print("LOCAL PRINT : DOOR ALARM ON!!!")
        var1 = "ON!"
        count = count +1
        query_args = {"SENSOR_ID":"Alarm1","SENSOR_STATUS":var1,"SENSOR_COUNT":count}
        encoded_args = urllib.urlencode(query_args)
        url = 'https://thematic-caster-124023.appspot.com/upload_data'
        print urllib2.urlopen(url, encoded_args).read()
        while io.input(door_pin1):
            blink_led()
    else:
        io.output(led_1, False)
        if var1 == "ON!":
            print("LOCAL PRINT : DOOR ALARM OFF")
            var1 = "off"
            query_args = {"SENSOR_ID":"Alarm1","SENSOR_STATUS":var1,"SENSOR_COUNT":count}
            encoded_args = urllib.urlencode(query_args)
            url = 'https://thematic-caster-124023.appspot.com/upload_data'
            print urllib2.urlopen(url, encoded_args).read()
        
    
    time.sleep(0.5)
