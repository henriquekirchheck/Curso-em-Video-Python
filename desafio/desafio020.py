# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

a1 = str(input('Aluno n1: '))
a2 = str(input('Aluno n2: '))
a3 = str(input('Aluno n3: '))
a4 = str(input('Aluno n4: '))

a = [a1, a2, a3, a4]
shuffle(a)

print('A lista é:\n {}' .format(a))