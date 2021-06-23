#Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo os nome deles e escrevendo o nome do escolhido

import random

a1 = input('Aluno n1: ')
a2 = input('Aluno n2: ')
a3 = input('Aluno n3: ')
a4 = input('Aluno n4: ')

a = random.choice([a1, a2, a3, a4])
print('O aluno é: {}'.format(a))