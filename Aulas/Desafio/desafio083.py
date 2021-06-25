# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

abre = fecha = 0

ex = str(input("Digite ume expressão que use parênteses: "))

for z in ex.strip().lower():
    if(z == '('):
        abre += 1
    elif(z == ')'):
        fecha += 1
if(abre == fecha):
    print('Esta correto')
else:
    print('Esta errado')