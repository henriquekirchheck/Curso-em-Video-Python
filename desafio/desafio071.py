# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

trya = True
rs1 = rs10 = rs20 = rs50 = 0



print('-' * 30)
print('Banco do Henrique'.center(30))
print('-' * 30)

while True:
    if(trya == True):
        money = int(input('Digite o valor em reais: R$'))
        trya = False
    
    if(money >= 50):
        rs50 = money // 50
        money = money % 50
    elif(money >= 20):
        rs20 = money // 20
        money = money % 20
    elif(money >= 10):
        rs10 = money // 10
        money = money % 10
    elif(money >= 1):
        rs1 = money // 1
        money = money % 1
    elif(money == 0):
        break
    else:
        print('\nO valor que você colocou voi invalido, tente novamente!\n')
        trya = True

print('-' * 30)

print(f'''Você vai receber: 
 {rs50} notas de 50 
 {rs20} notas de 20 
 {rs10} notas de 10 
 {rs1} notas de 1
Muito obrigado por usar o Banco! Tenha um bom dia''')