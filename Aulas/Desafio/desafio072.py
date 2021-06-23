# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

con = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito','dezenove', 'vinte')

while True:
    n = int(input('Escolha um numero entre 0 e 20: '))

    if((n < 0) or (n > 20)):
        print('\nPor favor. ', end='')
    else:
        break

print(f'O seu numero é {con[n]}')