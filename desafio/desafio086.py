# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[None, None, None] ,[None, None, None], [None, None, None]]
max = 0

for x in range(0, len(matriz)):
    for y in range(0, len(matriz)):
        matriz[x][y] = (str(input(f'Digite o valor do [{x + 1}, {y + 1}]: ')))

for z, b in enumerate(matriz):
    for a in matriz[z]:
        if(len(a) > max):
            max = len(a)

for x in range(0, len(matriz)):
    for y in range(0, len(matriz)):
        print(f'[{matriz[x][y].center(max)}]', end=' ')
    print('')
