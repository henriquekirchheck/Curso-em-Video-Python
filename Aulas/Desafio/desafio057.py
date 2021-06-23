# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto
loop = True

while(loop == True):
    gender = str(input('Qual é o seu sexo?(M, F): '))

    if gender.lower() in('m', 'f'):
        loop = False
    else:
        print('\nVocê colocou um valor invalido, tente de novo!\n')
        loop = True