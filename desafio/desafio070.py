# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

lista = dict()
total = 0
mais1000 = 0

print('-' * 30)
print('LOJA SUPER BARATÃO'.center(30))
print('-' * 30)

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    print('-' * 30)

    lista[nome] = preço

    exit = str(input('Você quer continuar?: [S/N] ')).strip().lower()[0]

    if(exit == 'n'):
        break
    print('-' * 30)

for x in lista.values():
    total += x

    if(x >= 1000.00):
        mais1000 += 1

x = min(lista, key=lista.get)

print('-' * 30)
print(f'O total é {total} \n{mais1000} produtos custam mais de R$1000 \n{x} é o produto mais barato')
print('-' * 30)
