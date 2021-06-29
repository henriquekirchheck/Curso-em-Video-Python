# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

#  a) de 1 até 10, de 1 em 1
#  b) de 10 até 0, de 2 em 2
#  c) uma contagem personalizada

def contador(inicio:int, fim:int, passo:int):
    from time import sleep
    if((inicio > fim) and (passo < 0)):
        passo += (passo * -2)
        print(f'O inicio é {fim}, o fim é {inicio} e o passo é {passo}')
        for loop in range(fim, (inicio + 1), passo):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    elif(inicio > fim):
        print(f'O inicio é {inicio}, o fim é {fim} e o passo é {passo}')
        for loop in reversed(range(fim, (inicio + 1), passo)):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    elif(passo < 0):
        passo += (passo * -2)
        print(f'O inicio é {fim}, o fim é {inicio} e o passo é {passo}')
        for loop in reversed(range(inicio, (fim + 1), passo)):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    elif(passo == 0):
        passo = 1
        print(f'O inicio é {inicio}, o fim é {fim} e o passo é {passo}')
        for loop in range(inicio, (fim + 1), passo):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    else:
        print(f'O inicio é {inicio}, o fim é {fim} e o passo é {passo}')
        for loop in range(inicio, (fim + 1), passo):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Escolha o inicio: '))
fim = int(input('Escolha o fim: '))
passo = int(input('Escolha o passo: '))

contador(inicio, fim, passo)