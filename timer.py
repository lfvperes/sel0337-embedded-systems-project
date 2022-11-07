# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 4
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

# importa as bibliotecas que serao usadas
from time import sleep
from gpiozero import LED, PWMLED
from math import sin, pi

# define a funcao de contagem regressiva que mostra a contagem de tempo formatada em mm:ss
def contagem_regressiva(time_seconds):
    # while para a contagem de tempo quando chega no zero
    while time_seconds > 0:
        # usa divisao inteira e modulo para a contagem
        countdown = f"{time_seconds // 60:02d}:{time_seconds % 60:02d}"
        print(countdown, end='\r')
        sleep(1)
        time_seconds -= 1
    
    print("Tempo esgotado!")

    print("Acendendo LED...")

# pede entrada novamente ate ser correta
input_success = False
while not input_success:
    try:
        time_seconds = int(input("Entre com o tempo total em segundos: "))
        input_success = True
        # verifica se o tempo e positivo
        if time_seconds < 0:
            input_success = False
            print("Tempo não pode ser negativo")
        # error handling caso entrada nao seja valida
    except ValueError:
        print("Entrada precisa ser numérica")
        input_success = False

contagem_regressiva(time_seconds)
my_led = PWMLED(18)
x = 0
while True:
    # pisca LED na metade do brilho
    # my_led.on()
    # sleep(0.5)
    # my_led.off()
    # sleep(0.5)

    # pisca LED gradualmente usando senoide variando de 0 ate 1 e PWM
    my_led.value = (sin(x) + 1) / 2
    sleep(0.1)
    if x >= 2 * pi:
        x = 0
    else:
        x += 0.1



