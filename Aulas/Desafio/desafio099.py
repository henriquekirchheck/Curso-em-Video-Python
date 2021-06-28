# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(*num):
    from time import sleep
    print('Analizando os valores passados...')
    sleep(0.5)
    mnum = 0
    length = len(num)
    for x in num:
        if(x > mnum):
            mnum = x
        print(x, end=' ')
    print(f'Foram informados {length} valores ao todo')
    print(f'O maior valor informado foi {mnum}')


print('-=' * 30)
maior(2, 9, 4, 5, 7, 1)
print('-=' * 30)
maior(4, 7, 0)
print('-=' * 30)
maior(1, 2)
print('-=' * 30)
maior(6)
print('-=' * 30)
maior()
print('-=' * 30)