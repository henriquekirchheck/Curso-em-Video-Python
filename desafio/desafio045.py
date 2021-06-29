# Faça um programa que jogue pedra papel tesoura com você

import random

player = int(input('\nEscolha um material: \n Pedra: 1 \n Papel: 2 \n Tesoura: 3 \n--> '))
cpu = random.randint(1, 3)

if(player == 1):
    if(cpu == 1):
        print('\nCPU diz: PEDRA')
        print('EMPATE!')
    elif(cpu == 2):
        print('\nCPU diz: PAPEL')
        print('Você perdeu...')
    elif(cpu == 3):
        print('\nCPU diz: TESOURA')
        print('PARABENS!!! Você ganhou!')
elif(player == 2):
    if(cpu == 1):
        print('\nCPU diz: PEDRA')
        print('PARABENS!!! Você ganhou!')
    elif(cpu == 2):
        print('\nCPU diz: PAPEL')
        print('EMPATE!')
    elif(cpu == 3):
        print('\nCPU diz: TESOURA')
        print('Você perdeu...')
elif(player == 3):
    if(cpu == 1):
        print('\nCPU diz: PEDRA')
        print('Você perdeu...')
    elif(cpu == 2):
        print('\nCPU diz: PAPEL')
        print('PARABENS!!! Você ganhou!')
    elif(cpu == 3):
        print('\nCPU diz: TESOURA')
        print('EMPATE!')