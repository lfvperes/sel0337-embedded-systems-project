from time import sleep
from gpiozero import LED

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
my_led = LED(18)
while True:
    my_led.on()
    sleep(0.5)
    my_led.off()
    sleep(0.5)
