# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela
num = []

def sort (list:list):
    length = len(list)
    for y in range(0,length):
        for x in range(0, length -1):
            print(f'Lista = {list}, x = {x}, y = {y}')
            if(list[x] > list[x + 1]):
                print('Entrou no if')
                n1 = list[x]
                list[x] = list[x + 1]
                list[x + 1] = n1
            
for x in range(0, 5):
    n = int(input('Digite um numero: '))
    num.append(n)

sort(num)

print(f'A lista é {num}')