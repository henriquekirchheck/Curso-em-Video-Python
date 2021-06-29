# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from time import sleep

medidade = 0

masculino = {}
feminino = {}
nfeminino = []

for loop in range(1, 5):
    print('Digite as informações da {} pessoa:' .format(loop))
    nome = str(input('   Nome: '))
    genero = str(input('   Genero: '))
    idade = int(input('   Idade: '))
    print('')

    genero = genero.lower()

    medidade = medidade + idade

    if(genero in('masculino', 'homem', 'menino', 'garoto', 'menininho', 'garotinho', 'homenzinho', 'homenzão', 'garotão','meninizão')):
        masculino[nome] = idade
    if(genero in('feminino', 'mulher', 'menina', 'garota', 'menininha', 'garotinha', 'mulherzinha', 'mulherzona', 'garotona','meninona')):
        feminino[nome] = idade
    sleep(0.5)

for x, y in feminino.items():
    if(y < 20):
        nfeminino.append(x)
    
print('A media de idade é {}' .format((medidade / 4)))
print('A nome do homem mais velho é {}' .format(max(masculino, key=masculino.get)))
print('Os nomes das mulheres com idade menor de 20 anos são {}' .format(', '.join(nfeminino)))

