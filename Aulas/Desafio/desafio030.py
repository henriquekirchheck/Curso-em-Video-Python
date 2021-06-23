#Crie um programa que mostre se um numero é par ou impar

num = int(input('Escolha um numero: '))

numlast = num % 10

print(numlast)

if(numlast in(0, 2, 4, 6, 8)):
    print('O numero {} é par' .format(num))
else:
    print('O numero {} é impar' .format(num))