# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 3
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

from gpiozero import LED
from time import sleep

vermelho = LED(18)
# liga o LED, espera, desliga o LED, espera, repete
while True:
	vermelho.on()
	sleep(0.5)
	vermelho.off()
	sleep(0.5)

