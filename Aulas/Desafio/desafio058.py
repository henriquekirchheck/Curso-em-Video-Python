# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint as random

cpu = random(1, 10)
player = None
win = False
cheat = False
counter = 0

while(win == False):
    if(cheat == True):
        print(f'O numero da cpu é \033[1;34m{cpu}\033[m \n')

    player = int(input('Adivinhe um numero de 1 a 10: '))

    if(player == 8822464613):
        cheat = True
        print('''
        +=========================+
        Você ativou o cheat secreto
        +=========================+
        ''')
    elif(player == cpu):
        counter = counter + 1
        if(counter == 1):
            print(f'\nParabens, você ganhou!!!\nVocê precisou de {counter} tentativa')
        else:
            print(f'\nParabens, você ganhou!!!\nVocê precisou de {counter} tentativas')
        win = True
    else:
        counter = counter + 1
        print('\nInfelismente você perdeu, tente novamente\n')
        