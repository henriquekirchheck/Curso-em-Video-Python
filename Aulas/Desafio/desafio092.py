# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
import datetime as dt


nome = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de trabalho (0 não tem): '))

info = {'Nome' : nome,
        'Idade' : dt.date.today().year - ano,
        'CTPS' : ctps}

if(ctps != 0):
    info['Ano de contratação'] = int(input('Ano de contratação: '))
    info['Salario'] = int(input('Salario: R$'))
    info['Aposentadoria'] = info['Idade'] + ((info['Ano de contratação'] + 35) - dt.date.today().year)

print('-=' * 15)

for x, y in info.items():
    print(f'-- {x} tem o valor {y}')