# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def line(txt:str, upper = False):
    if(upper == True):
        print('-' * (len(txt) + 2))
        print(txt.upper().center(len(txt) + 2))
        print('-' * (len(txt) + 2))
    else:    
        print('-' * (len(txt) + 2))
        print(txt.center(len(txt) + 2))
        print('-' * (len(txt) + 2))

line('CeV')

line('Curso em Video', upper=True)

line('Olá, como vai?')