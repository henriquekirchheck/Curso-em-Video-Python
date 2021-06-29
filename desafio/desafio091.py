# Crie um programa onde 4 playeres joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter

ranking = {}
place = 0

print('-=' * 30)
print('Valores sorteados: ')

sleep(0.7)
player1 = randint(1,6)
print(f'Jogador N1 tirou {player1} no dado')
sleep(0.7)
player2 = randint(1,6)
print(f'Jogador N2 tirou {player2} no dado')
sleep(0.7)
player3 = randint(1,6)
print(f'Jogador N3 tirou {player3} no dado')
sleep(0.7)
player4 = randint(1,6)
print(f'Jogador N4 tirou {player4} no dado')

print('-=' * 30)

player = {
    'Jogador N1' : player1,
    'Jogador N2' : player2,
    'Jogador N3' : player3,
    'Jogador N4' : player4
}

ranking = sorted(player.items(), key=itemgetter(1), reverse=True)

print(('-=' * 5).ljust(10), 'Ranking'.upper().center(10), ('-=' * 5).ljust(10))
for k, v in ranking:
    place += 1
    print(f'{place}° lugar: {k} com o dado de numero {v}')