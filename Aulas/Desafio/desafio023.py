# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um numero inteiro de 0 a 9999: '))
numstr = str(num)

uni = numstr [3]
dez = numstr [2]
cen = numstr [1]
mil = numstr [0]

print('\n Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}\n' .format(uni, dez, cen, mil))