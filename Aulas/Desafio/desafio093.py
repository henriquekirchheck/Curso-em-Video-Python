# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
total = 0

nome = str(input('Nome do Jogador: '))
npar = int(input('Quantas partidas ele jogou: '))

jogador['nome'] = nome

for x in range(1, (npar + 1)):
    y = (int(input(f'Quanto gols na partida {x}: ')))
    gols.append(y)
    total += y

jogador['gols'] = gols
jogador['total'] = total

print('-=' * 15)
print(jogador)
print('-=' * 15)

for z, a in jogador.items():
    print(f'O campo {z} tem o valor {a}')

print('-=' * 15)

jogador['npar'] = npar

print('O jogador {} jogou {} partidas'.format(jogador['nome'], len(jogador['gols'])))
for x, y in enumerate(jogador['gols']):
    print(f'Na partida {x + 1}, fez {y} gols.')
print('Foi um total de {} gols'.format(jogador['total']))