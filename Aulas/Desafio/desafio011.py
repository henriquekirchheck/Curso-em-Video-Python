
''' Faça um programa que leia largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m² '''

lar = float(input('Largura: '))
alt = float(input('Altura: '))

m2 = lar * alt
tin = m2 / 2

print('A casa vai usar {} litros de tinta' .format(tin))