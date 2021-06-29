# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um numero: '))

for c in range(1, 11):
    r = c * num
    if(c == 10): print('{} x {} = {}' .format(num, c, r))
    else: print('{} x  {} = {}' .format(num, c, r))
