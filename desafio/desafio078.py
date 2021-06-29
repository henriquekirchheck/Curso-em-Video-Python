# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
value = list()
min = list()
max = list()

for loop in range(0,5):
    value.append(int(input(f'Digite um valor no indice {loop}: ')))

cvalue = value.copy()
cvalue.sort()

for x, y in enumerate(value):
    if(y == cvalue[0]):
        min.append(x)
    elif(y == cvalue[-1]):
        max.append(x)

print('-' * 30)
print(f'O maior valor é {cvalue[-1]} e foi encontrado nos indices {max}')
print(f'O menor valor é {cvalue[0]} e foi encontrado nos indices {min}')