# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
lnum = list()

print('Digite um numero para adicionalo na lista')
print('Digite alguma letra para parar')
print('-' * 30)
while True:
    n = str(input('Digite um valor: '))
    if(n.isnumeric()):
        if(int(n) in lnum):
            print('Esse numero já esta na lista')
        elif(int(n) not in lnum):
            lnum.append(int(n))
    elif(n.isalpha()):
        break
    elif(n == ''):
        print('Você não digitou nada')
    elif(n.isalnum):
        print('Você digitou uma letra e um numero')

lnum.sort()

print(' '.join(str(a) for a in lnum))