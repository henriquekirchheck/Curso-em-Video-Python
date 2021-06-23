# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
from time import sleep

c = 0

ppt = 'PEDRA, PAPEL, TESOURA'

print('-' * 30)
print(ppt.center(30))
print('-' * 30)

while True:
    cpu = randint(1,3)
    player = int(input('\nEscolha entre pedra(1), papel(2) e tesoura(3)'))
    if(player == 1):
        if(cpu == 1):
            print('\nCPU diz: PEDRA')
            print('EMPATE!')
        elif(cpu == 2):
            print('\nCPU diz: PAPEL')
            print('Você perdeu...')
            break
        elif(cpu == 3):
            print('\nCPU diz: TESOURA')
            print('PARABENS!!! Você ganhou!')
            c += 1
    elif(player == 2):
        if(cpu == 1):
            print('\nCPU diz: PEDRA')
            print('PARABENS!!! Você ganhou!')
            c += 1
        elif(cpu == 2):
            print('\nCPU diz: PAPEL')
            print('EMPATE!')
        elif(cpu == 3):
            print('\nCPU diz: TESOURA')
            print('Você perdeu...')
            break
    elif(player == 3):
        if(cpu == 1):
            print('\nCPU diz: PEDRA')
            print('Você perdeu...')
            break
        elif(cpu == 2):
            print('\nCPU diz: PAPEL')
            print('PARABENS!!! Você ganhou!')
            c += 1
        elif(cpu == 3):
            print('\nCPU diz: TESOURA')
            print('EMPATE!')
print(f'\nVocê ganhou {c} vezes')