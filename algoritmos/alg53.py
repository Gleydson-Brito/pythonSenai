
from os import system
import time

numero = int(input('Informe o número: '))

while numero >= 1:
    system('clear')
    print(numero)
    numero -= 1
    time.sleep(1)
