# Faça um programa que faça uma contagem regreciva de 10 segundos para para fogos de artificio

from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('Feliz ano novo!!!')