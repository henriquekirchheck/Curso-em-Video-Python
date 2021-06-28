# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(lar, com):
    a = lar * com
    print(f'A area de um terreno {lar}m * {com}m é de {a}m2')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)