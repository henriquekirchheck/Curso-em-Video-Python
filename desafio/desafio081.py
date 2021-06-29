#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

num = list()

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

if(5 in num):
    val = 'Tem'
else:
    val = 'Não tem'

num.sort(reverse=True)
print(f'Foram digitados {len(num)} numeros \nA lista de valores de forma decrecente {num} \n{val} um numero 5 na lista')