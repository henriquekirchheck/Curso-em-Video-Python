# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

dados = ['Dummy', -5.0, -5.0]
alunos = []
med = 0
    
print('-=-' * 15)
print('Não digite nada para parar'.center(45))
print('-=-' * 15)

while True:
    dados[0] = str(input('Digite o nome de alguma pessoa: '))
    if(dados[0] == ''):
        print('-=-' * 15)
        break                                                   
    dados[1] = float(input('Digite a primeira nota da pessoa: '))
    dados[2] = float(input('Digite a segunda nota da pessoa: '))
    if(((dados[1] >= 0) and (dados[2] >= 0)) and ((dados[1] <= 10) and (dados[2] <= 10))):
        alunos.append(dados.copy())
        print('-=-' * 15)
    else:
        print('-=-' * 15)
        print('Alguma coisa deu errado, tente novamente!')
        print('-=-' * 15)

for x, a in enumerate(alunos):
    for y, z in enumerate(alunos[x]):
        if(y == 0):
            None
        elif(y == 1):
            med += z
        else:
            med += z
            med = med / 2
            print(f'O aluno {alunos[x][0]} tem {med} na media.')
            med = 0
        

