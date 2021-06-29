# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

list = []

for loop in range(1,6):
    peso = float(input('Peso da {} pessoa: ' .format(loop)))
    list.append(peso)
list.sort()

print('A pessoa mais pesada tem {}kg e a mais leve tem {}kg' .format(list[4], list[0]))