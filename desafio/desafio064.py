# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles

end = False
times = 0
add = 0

while(end == False):
    n = int(input(f'Digite o {times + 1}° valor ou digite "0" pra terminar o programa: '))
    if(n != 0):
        add = add + n
        times = times + 1
    if((n == 0) and (times == 1)):
        print(f'O numero foi adicionado {times} vez e o resultado é {add}')
        end = True
    elif(n == 0):
        print(f'Os numeros foram adicionados {times} vezes e o resultado é {add}')
        end = True