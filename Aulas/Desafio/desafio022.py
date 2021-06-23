#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   O nome com todas as letras maiusculas
#   O nome com todas as letras minusculas
#   Quantas letras ao todo (sem considerar espaços)
#   Quantas letras tem o primeiro nome

Nome = str(input('\nSeu nome: '))

NOME = Nome.strip().upper()
nome = Nome.strip().lower()
NoMe = len(Nome.strip().replace(' ', ''))
nOmE = len(Nome.strip().split() [0])

print('Nome maiusculo: {} \nNome minusculo: {} \nQuantidade de letras no nome: {} \nQuantidade de Letras no primeiro nome: {} \n' .format(NOME, nome, NoMe, nOmE))