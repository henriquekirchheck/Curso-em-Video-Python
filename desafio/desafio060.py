# Faça um programa que leia um número qualquer e mostre o seu fatorial

num = int(input('Digite um numero: '))
result = 1

print(f'Calculando {num}! = ', end='')

while(num != 0):
    result = result * num
    if(num == 1):
        print(num, end=' = ')
        print(result)
    else:
        print(num, end=' x ')
    num = num - 1

