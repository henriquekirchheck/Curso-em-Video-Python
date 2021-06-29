# Aprimore o desafio anterior, mostrando no final:
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha

matriz = [[None, None, None] ,[None, None, None], [None, None, None]]
max = spar = ster = max2l = 0

for x in range(0, len(matriz)):
    for y in range(0, len(matriz)):
        n = (int(input(f'Digite o valor do [{x + 1}, {y + 1}]: ')))
        matriz[x][y] = n
        if(n % 2 == 0):
            spar += n
        if(y == 2):
            ster += n

for e, f in enumerate(matriz):
    for g in matriz[e]:
        if(len(str(g)) > max):
            max = len(str(g))

for x in range(0, len(matriz)):
    for y in range(0, len(matriz)):
        print(f'[{str(matriz[x][y]).center(max)}]', end=' ')
    print('')

matriz2max = matriz[1].copy()
matriz2max.sort

print(f'\nA soma dos numeros pares é {spar}')
print(f'A soma da terceira coluna é {ster}')
print(f'O maior valor da segunda linha é {matriz2max[-1]}')


