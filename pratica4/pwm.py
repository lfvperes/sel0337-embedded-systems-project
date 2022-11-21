# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 4
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

# importa as bibliotecas que serao usadas
from time import sleep
from gpiozero import PWMLED
from math import sin, pi

my_led = PWMLED(18)
x = 0
while True:

    # pisca LED gradualmente usando senoide variando de 0 ate 1 e PWM
    my_led.value = (sin(x) + 1) / 2
    sleep(0.1)
    if x >= 2 * pi:
        x = 0
    else:
        x += 0.1



