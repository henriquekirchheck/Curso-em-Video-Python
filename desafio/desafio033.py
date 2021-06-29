# Faça um programa que leia tres numeros e mostre o maior e o menor deles

n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))
n3 = int(input('Terceiro Numero: '))

n = [n1,n2,n3]
n = sorted(n)

if(n[0] == n[2]):
    print('é o mesmo numero')
else:
    print('O maior numero é {} e o menor numero é {}!' .format(n[2], n[0]))