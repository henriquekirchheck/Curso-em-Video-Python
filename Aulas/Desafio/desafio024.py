# Crie um programa que leia o nome de uma cidade e responda se ela começa com Santo

city = str(input('Cidade: '))
citybool = 'Santo' in city

if citybool == True:
    print('A sua cidade tem a palavra "Santo"')
else:
    print('A sua cidade não tem a palavra "Santo"')
