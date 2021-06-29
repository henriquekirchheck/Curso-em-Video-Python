# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
cup = 'CADASTRE UMA PESSOA'
homcad = age18 = mul20 = 0


while True:
    print('-' * 30)
    print(cup.center(30))
    print('-' * 30)
     
    age = int(input('Idade: '))
    gender = str(input('Sexo: [M/F] ')).lower()

    print('-' * 30)

    if(gender == 'm'):
        homcad = homcad + 1
    elif(gender == 'f'):
        if(age < 20):
            mul20 = mul20 + 1 
    
    if(age >= 18):
        age18 = age18 + 1

    exit = str(input('Quer continuar? [S/N] ')).lower()

    if(exit == 'n'):
        break


print('-' * 30)
print(f'{age18} pessoa(as) com mais de 18 anos \n{homcad} homen(s) \n{mul20} mulher(es) com menos de 20 anos')
print('-' * 30)