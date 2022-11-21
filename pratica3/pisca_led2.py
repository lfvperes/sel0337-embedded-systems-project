# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 3
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

from gpiozero import LED
from time import sleep

from signal import pause

# um unico metodo para ligar e desligar
# o LED, dados os tempos
vermelho = LED(18)
vermelho.blink(0.5, 0.5)
pause()

