# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

minor = 0
adult = 0

for loop in range(1, 8):
    age = int(input('Qual é a idade da {} pessoa?: ' .format(loop)))
    if(age < 18):
        minor = minor + 1
    else:
        adult = adult + 1
print('Tem {} pessoas menor de idade e {} pessoas adultas' .format(minor, adult))