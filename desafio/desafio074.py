# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

a = randint(0, 99)
b = randint(0, 99)
c = randint(0, 99)
d = randint(0, 99)
e = randint(0, 99)

t = (a, b, c, d, e)

print(t)
print(sorted(t)[0])
print(sorted(t)[-1])

