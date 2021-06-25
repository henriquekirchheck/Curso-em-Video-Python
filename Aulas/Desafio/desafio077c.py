# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
palavras = ('aprender', 'programar', 'linguagem')

for x in palavras:
    print('')
    print(f'A palavra {x} tem as vogais ', end='')
    for y in x:
        if(y in 'aeiou'):
            print(y, end='')

