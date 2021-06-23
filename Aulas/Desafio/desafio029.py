# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapaçar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite

km = float(input('Velocidade do carro: '))

if km > 80.00:
    aboveKm = km - 80
    fine = aboveKm * 7
    print('Você andou {:.1f}Km/h acima do limite de velocidade (80Km/h) e recebeu uma multa de R${:.2f}.' .format(aboveKm, fine))
else:
    print('Pode passar!')
