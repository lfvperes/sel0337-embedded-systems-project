# UNIVERSIDADE DE SAO PAULO 2022
# SEL0337 - APLICACAO DE MICROPROCESSADORES II
# PRATICA 3
# 
# CAMILA HIROMI TANAKA 10748201
# LUIS FILIPE VASCONCELOS PERES 10310641

from time import sleep
from gpiozero import LED

def contagem_regressiva(time_seconds):
    # sai do laco quando atinge zero
    while time_seconds > 0:
        # formatando o tempo como mm:ss e limpando a tela
        countdown = f"{time_seconds // 60:02d}:{time_seconds % 60:02d}"
        print(countdown, end='\r')
        # contagem regressva de 1s atualizando a variavel
        sleep(1)
        time_seconds -= 1
    
    print("Tempo esgotado!")

    print("Acendendo LED...")

input_success = False
while not input_success:
    # pedindo entrada do usuario ate dados corretos serem fornecidos
    try:
        time_seconds = int(input("Entre com o tempo total em segundos: "))
        input_success = True
        # tempo deve ser um numero positivo
        if time_seconds < 0:
            input_success = False
            print("Tempo não pode ser negativo")
    except ValueError:
        print("Entrada precisa ser numérica")
        input_success = False

# chamada do metodo
contagem_regressiva(time_seconds)
my_led = LED(18)
# piscando apos a contagem chegar a zero
while True:
    # liga, espera, desliga, espera, repete
    my_led.on()
    sleep(0.5)
    my_led.off()
    sleep(0.5)

