# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for loop in range(1,8):
    n = int(input(f'Digite o {loop} valor: '))
    if(n % 2 == 0):
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print('-=-' * 15)
print(f'Os numeros pares são: {valores[0]}')
print(f'Os numeros impares são: {valores[1]}')