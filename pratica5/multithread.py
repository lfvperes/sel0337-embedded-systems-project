# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 5
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

import threading as th
import RPi.GPIO as GPIO
from time import sleep

#freq = 1/4
period = 4
blink = True

led = 18
button = 15

def button_callback(channel):
    global period
    if GPIO.input(button):
        print("Interrupt")
        period = 2
    else: period = 4

def timer_callback():
    global blink
    print("fim do timer")
    blink = False    

GPIO.setmode(GPIO.BCM)
GPIO.setup(
    button,
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)
GPIO.add_event_detect(button,
    GPIO.BOTH,
    callback=button_callback,
    bouncetime=50
)
GPIO.setup(led, GPIO.OUT)

S = th.Timer(35, timer_callback)
S.start()

while blink:
    GPIO.output(led, GPIO.HIGH)
    sleep(period)
    GPIO.output(led, GPIO.LOW)
    sleep(period)
    print(period)
GPIO.cleanup()
