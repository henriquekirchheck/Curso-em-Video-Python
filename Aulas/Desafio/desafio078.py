# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
value = list()

for x in range(0,5):
    value.append(int(input('Digite um valor: ')))

cvalue = value.copy()
cvalue.sort()

print('-' * 30)
print(f'O maior valor é {cvalue[-1]} e foi encontrado no indice {value.index(cvalue[-1])}')
print(f'O menor valor é {cvalue[0]} e foi encontrado no indice {value.index(cvalue[0])}')