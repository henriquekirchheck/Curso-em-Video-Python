# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Nome: '))

nomesep = nome.strip().split()
nomenum = int(len(nomesep)) - 1

print(' Primeiro Nome: {}\n Ultimo Nome: {}\n' .format(nomesep [0], nomesep [nomenum]))