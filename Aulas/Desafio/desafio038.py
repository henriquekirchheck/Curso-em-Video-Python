#Peça dois valores e escreva na tea o maior ou diga se os dois são iguais

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

n = [n1, n2]
n.sort()

print('')

if(n[0] == n[1]):
    print('Os numeros são iguais!')
else:
    if(n[1] == n1):
        print('O primeiro valor é maior!')
    if(n[1] == n2):
        print('O segundo valor é maior!')