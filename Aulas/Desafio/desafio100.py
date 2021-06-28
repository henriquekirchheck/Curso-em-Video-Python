# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

def sorteia(list:list, quant:int = 5):
    from random import randint as rd
    from time import sleep
    print(f'Sorteando {quant} numeros:', end=' ')
    for loop in range(0, quant):
        random = rd(1, 10)
        print(random, end=' ')
        list.append(random)
        sleep(0.5)
    print()
def somapar(list:list):
    soma = 0
    for loop in list:
        if((loop % 2) == 0):
            soma += loop
    print(f'A soma dos numeros pares da lista {list} é {soma}')


lista = list()

sorteia(lista, 10)
somapar(lista)
