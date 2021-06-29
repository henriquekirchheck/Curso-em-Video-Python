from time import sleep

#Aula N°10

print("Aula N°10 \n")
sleep(0.2)


""" car = int(input('Anos do carro: '))

if(car <= 3):
    print('Carro Novo')
elif(car > 3):
    print('Carro Velho')

print('Carro Novo' if car <= 3 else 'Carro Velho') """

""" nome = str(input('Qual o seu nome?: '))

if nome == 'Gustavo':
    print('Que nome lindo vc tem')
elif nome == 'sus' or 'SUS' or 'Sus':
    print('AMOGUS')
else:
    print('Seu nome é tão normal')

print('Bom dia {}!' .format(nome)) """

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua media foi {:.2f}' .format(m))

if m >= 6.0:
    print('Sua media foi boa!')
else:
    print('Sua media foi ruim!')
