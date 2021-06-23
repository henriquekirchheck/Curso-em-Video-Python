# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas

km = int(input('quantos km teve a viagem: '))

if(km <= 200):
    price = km * 0.5
elif(km > 200):
    price = km * 0.45

print('O preço da viagem é R${:.2f}!' .format(price))
