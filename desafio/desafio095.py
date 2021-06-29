# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

total = npc = 0
gols = list()
jogador = dict()
jogadores = list()

while True:
    print('-=' * 22)
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    np = int(input('Quantas partidas {} jogou?: '.format(jogador['nome'])))
    for g in range(1, np + 1):
        gol = (int(input(f'   Quantos gols na partida {g}?: ')))
        gols.append(gol)
        total += gol
    jogador['gols'] = gols.copy()
    jogador['total'] = total

    if(np > npc):
        npc = np

    jogadores.append(jogador.copy())

    jogador.clear()
    gols.clear()
    gol = total = 0

    if(len(jogadores) >= 999):
        break

    qc = str(input('Quer continuar?: [S/N] ')).lower().strip()

    if(qc == 'n'):
        break

print('-=' * 22)

print('cod', 'nome'.ljust(20), 'gols'.ljust(npc * 3), 'total')
print('-' * 44)
for a, b in enumerate(jogadores):
    print(f'{a}'.rjust(3), b['nome'].ljust(20), ' '.join(str(i) for i in b['gols']).ljust(npc * 3), b['total'])
print('-' * 44)

while True:
    c = int(input('Mostrar dados de qual jogador?: ("999" para parar) '))
    print('-' * 44)
    if(c == 999):
        break
    elif((c > 999) or (c < 0)):
        print('Digite um valor valido')
    else:
        print('Levantamento do jogador {}'.format(jogadores[c]['nome']))
        for ind, gpj in enumerate(jogadores[c]['gols']):
            print(f'No jogo {ind + 1} fez {gpj}')


