# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 5
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

import threading as th
import RPi.GPIO as GPIO
from time import sleep

# serao variaveis globais
# definindo intervalo
period = 4
# definindo flag
blink = True

# definindo numeros dos pinos
led = 18
button = 15

def button_callback(channel):
    """funcao callback a ser chamada quando o botao for acionado

    Args:
        channel
    """
    # usando a variavel definida fora da funcao
    global period
    if GPIO.input(button):
        # interrupcao quando o botao for acionado
        print("Interrupt")
        # tempo de espera mudando cada vez que o botao for pressionado
        period = 2
    else: period = 4

def timer_callback():
    """funcao de callback a ser chamada quando o timer terminar
    """
    # usando a variavel definida fora da funcao
    global blink
    print("fim do timer")
    # mudando flag que vai ser usada para parar de piscar o LED
    blink = False    

# configurando entrada e saida
GPIO.setmode(GPIO.BCM)
# setando como entrada o pino do numero salvo na variavel botao 
GPIO.setup(
    button,
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)
# adicionando deteccao de evento ao botao que chama a funcao de callback
GPIO.add_event_detect(button,
    GPIO.BOTH,
    callback=button_callback,
    bouncetime=50
)
# setando como saida o pino do numero salvo na variavel led
GPIO.setup(
    led,
    GPIO.OUT
)

# criando threads e timer, passando funcao de callback como argumento
S = th.Timer(35, timer_callback)
S.start()

# laco principal
while blink:
    # acende led, espera, apaga, espera, mostra o tempo
    GPIO.output(led, GPIO.HIGH)
    sleep(period)
    GPIO.output(led, GPIO.LOW)
    sleep(period)
    print(period)
# limpando terminal
GPIO.cleanup()
