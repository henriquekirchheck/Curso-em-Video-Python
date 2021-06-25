# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num = list()
par = list()
impar = list()

print('\nDigite uma letra para parar')
print('-=-' * 10)

while True:
    n = str(input('Digite um numero: '))
    if(n.isnumeric()):
        num.append(int(n))
    elif(n.isalpha()):
        print('-=-' * 10)
        break
    else:
        print('-=-' * 10)
        print('Tente de novo')
        print('-=-' * 10)

for x in num:
    if((x % 2) == 0):
        par.append(x)
    else:
        impar.append(x)

print(f'Os numeros são {num}')
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')