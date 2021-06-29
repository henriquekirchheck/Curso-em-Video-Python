# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
import time

x = 0
num = int(input('Digite um numero: '))
print('')

for c in range(1, num + 1):
    if((num % c) == 0):
        print('\x1b[1;31m', c, '\x1b[m', end='')
        x = x + 1
    else:
        print('\x1b[1;34m', c, '\x1b[m', end='')
if(x == 2):
    print('\n\nO numero {} é primo!' .format(num))
elif((x > 2) or (x == 1)):
    print('\n\nO numero {} não é primo!' .format(num))