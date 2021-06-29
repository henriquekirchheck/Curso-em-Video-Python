#Faça um programa que mostre que um ano bissexto
from datetime import date

ano = int(input('\nEscolha um ano: '))
if(ano == 0): ano = date.today().year
resto100 = ano % 100
resto4 = ano % 4
resto400 = ano % 400

if((resto4 == 0) and (resto100 != 0)) or ((resto400 == 0)):
    print('O ano de {} é bissexto' .format(ano))
else:
    print('O ano de {} não é bissexto' .format(ano))
