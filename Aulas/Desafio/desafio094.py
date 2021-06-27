# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#  A) Quantas pessoas foram cadastradas 
#  B) A média de idade  
#  C) Uma lista com as mulheres 
#  D) Uma lista de pessoas com idade acima da média

people = list()
mulheres = list()
idademed = list()
person = dict()
medidade = 0

print('Não digite um nome para parar'.center(30))
print('-=' * 15)

while True:
    person['nome'] = str(input('Digite o nome de uma pessoa: ')).strip()
    if(person['nome'] == ''):
        break
    while True:
        person['sexo'] = str(input('Digite o sexo: [M, F] ')).lower().strip()
        if(person['sexo'] in 'mf'):
            break
    person['idade'] = int(input('Digite a idade: '))
    people.append(person.copy())
    person.clear()
    print('-=' * 15)
print('-=' * 15)

print(f'Foram cadastradas {len(people)} pessoas')

for x, a in enumerate(people):
    for y, z in people[x].items():
        if(y == 'idade'):
            medidade += z
        if((y == 'sexo') and (z == 'f')):
            mulheres.append(people[x]['nome'])

medidade = medidade / len(people)

for x, a in enumerate(people):
    for y, z in people[x].items():
        if((y == 'idade') and (z > medidade)):
            idademed.append(people[x]['nome'])

print(f'A media de idade é {medidade:.0f}')
print('A lista de mulheres é: {}'.format(' '.join(mulheres)))
print('As pessoas com idade maior da media são: {}'.format(' '.join(idademed)))

