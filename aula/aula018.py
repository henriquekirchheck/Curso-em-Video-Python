from time import sleep

#Aula N°18

print("Aula N°18 \n")
sleep(0.2)

pessoas = list()
dados = ['Dummy', 00]

print('-=-' * 10)
print('Não digite nada para parar')
print('-=-' * 10)

while True:
    dados[0] = str(input('Digite o nome de alguma pessoa: '))
    if(dados[0] == ''):
        print('-=-' * 10)
        break                                                   
    dados[1] = int(input('Digite a idade da pessoa: '))
    if(dados[0] != ''):
        pessoas.append(dados.copy())
        print('-=-' * 10)

for x in pessoas:
    print(f'{x[0]} tem {x[1]} anos de idade')