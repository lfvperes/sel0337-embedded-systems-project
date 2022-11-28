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

# definindo led pelo numero do pino de saida
my_led = PWMLED(18)
# nivel do led a ser incrementado
x = 0

# laco principal
while True:
    # pisca LED gradualmente usando senoide variando de 0 ate 1 e PWM
    my_led.value = (sin(x) + 1) / 2
    sleep(0.1)

    if x >= 2 * pi:
        # zerando para evitar overflow
        x = 0
    else:
        # incrementando nivel da entrada no led
        x += 0.1



