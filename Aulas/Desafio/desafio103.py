# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador:str = '', gols = 0):
    if((jogador == '') and (gols == '')):
        print(f'O jogador desconhecido fez 0 gol(s) no campeonato')
    elif(jogador == ''):
        print(f'O jogador desconhecido fez {gols} gol(s) no campeonato')
    elif(gols == ''):
        print(f'O jogador {jogador} fez 0 gol(s) no campeonato')
    else:
        print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


jogador = str(input('O nome do jogador: '))
gols = str(input('O numero de gols: '))

ficha(jogador, gols)