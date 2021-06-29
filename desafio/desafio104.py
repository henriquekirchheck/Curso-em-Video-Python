# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(inputof):
    while True:
        a = input(inputof)
        if(a.isnumeric()):
            return a
        else:
            print('Digite um numero valido')       



print(leiaInt('Digite um numero: '))
