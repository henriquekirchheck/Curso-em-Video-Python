# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci

tt = 0
t = int(input('Digite o numero de termos da sequência de Fibonacci: '))
n1 = 0
n2 = 1

print(f'\n{n1} -> ', end='')

while(tt != (t - 1)):
    n = n1 + n2
    n2 = n1
    n1 = n
    if(tt <= (t - 3)):
        print(n, end=' -> ')
    elif(tt == (t - 2)):
        print(f'{n} -> Fim')

    tt = tt + 1

