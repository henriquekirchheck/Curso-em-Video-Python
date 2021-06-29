# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Nome: '))
nome = nome.strip().lower()
nomebool = 'silva' in nome

if nomebool == True:
    print('Você tem "Silva" no seu nome')
    print(nome.title())
else:
    print('Você não tem "Silva" no seu nome')
    print(nome.title())