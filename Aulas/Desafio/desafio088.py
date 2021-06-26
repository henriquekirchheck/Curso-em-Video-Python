# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint as random

jogo = list()

print('-' * 30)
print('Joga na Mega Sena'.upper().center(30))
print('-' * 30)

jogos = int(input('Quantos jogos você quer que eu sorteie: '))

print('\n-=-=-=-', f'Sorteando {jogos} jogos'.upper().center(24), '-=-=-=-')
for x in range(0, jogos):
    for y in range(0, 6):
        while True:
            ran = random(1, 60)
            if(ran not in jogo):
                jogo.append(ran)
                break
            else:
                None
    print(f'Os numeros são: {jogo}')
    jogo.clear()

print('-=-=-=-', 'Boa Sorte'.upper().center(24), '-=-=-=-')

        
