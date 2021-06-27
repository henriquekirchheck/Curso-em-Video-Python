# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Digite o nome: '))
media = float(input('Digite a media: '))

aluno = {'nome' : nome, 'media' : media}

print('O nome do aluno é {}'.format(aluno['nome']))
print('A media do aluno é {}'.format(aluno['media']))
if(aluno['media'] < 7):
    print('O aluno foi reprovado')
else:
    print('O aluno foi aprovado')