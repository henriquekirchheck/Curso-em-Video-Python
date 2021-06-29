# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('\nDigite uma frase: '))
min = ''.join(frase.lower().split())
rev = ''.join(frase.lower().split())[::-1]

if(min == rev):
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')