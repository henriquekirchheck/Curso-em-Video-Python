# Faça o PC 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuario descobrir qual foi o número escolhido pelo PC

import random
from time import sleep

num = int(input('Escolha um numero: '))

pcNum = random.randint(1, num)

#print(pcNum)

num = int(input('Escolha um numero entre 1 e {}: ' .format(num)))


if pcNum == num:
    print('Parabens! Você acertou!')
else:
    print('Você errou.')
