# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 3
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

from time import sleep
from gpiozero import LED, PWMLED
from math import sin, pi

def contagem_regressiva(time_seconds):
    while time_seconds > 0:
        countdown = f"{time_seconds // 60:02d}:{time_seconds % 60:02d}"
        print(countdown, end='\r')
        sleep(1)
        time_seconds -= 1
    
    print("Tempo esgotado!")

    print("Acendendo LED...")

input_success = False
while not input_success:
    try:
        time_seconds = int(input("Entre com o tempo total em segundos: "))
        input_success = True
        if time_seconds < 0:
            input_success = False
            print("Tempo não pode ser negativo")
    except ValueError:
        print("Entrada precisa ser numérica")
        input_success = False

contagem_regressiva(time_seconds)
my_led = PWMLED(18)
x = 0
while True:
    # my_led.on()
    # sleep(0.5)
    # my_led.off()
    # sleep(0.5)

    # implementing PWM
    my_led.value = sin(x)
    sleep(0.5)
    if x == 2 * pi:
        x = 0
    else:
        x += 0.01


