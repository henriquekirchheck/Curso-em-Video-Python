# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

galist = []
nove = 0

for x in range(0,4):
    num = int(input('Escolha um numero: '))
    galist.append(num)
numtuple = tuple(galist)

galist.clear()

for x in numtuple:
    if(x == 9):
        nove += 1

print(f'O numero 9 apareceu {nove} vezes')

if 3 in numtuple:
    tres = numtuple.index(3) + 1
    print(f'O numero tres apareceu pela primeira vez no {tres} numero')

print(f'Os numeros pares foram: ', end='')

for x in numtuple:
    if(x in (0, 2, 4, 6, 8)):
        print(f'{x}', end=' ')
