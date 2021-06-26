# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#  C) Uma listagem com as pessoas mais leves.

pessoas = list()
pesado = list()
leve = list()
dados = ['Dummy', 00]

print('-=-' * 10)
print('Não digite nada para parar')
print('-=-' * 10)

while True:
    dados[1] = str(input('Digite o nome de alguma pessoa: '))
    if(dados[1] == ''):
        print('-=-' * 10)
        break                                                   
    dados[0] = int(input('Digite o peso da pessoa: '))
    if(dados[1] != ''):
        pessoas.append(dados.copy())
        print('-=-' * 10)

pessoas.sort()
np = len(pessoas)

for x in pessoas:
    if(x[0] == pessoas[-1][0]):
        pesado.append(x[1])
    elif(x[0] == pessoas[0][0]):
        leve.append(x[1])

leve = ' '.join(leve)
pesado = ' '.join(pesado)

print(f'O numero de pessoas é {np}')
print(f'O maior peso encontrado é {pessoas[-1][0]}: {pesado}')
print(f'O menor peso encontrado é {pessoas[0][0]}: {leve}')