# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

add = 0
num = []
end = False
count = -1

while(end == False):
    count += 1
    n = int(input('\nDigite um numero: '))
    num.append(n)
    
    resp = str(input('Quer continuar? (S, N) :')).lower()

    if(resp == 's'):
        end = False
    elif(resp == 'n'):
        end = True

for x in num:
    add = add + x

num.sort()

print(f'O maior numero é {num[-1]}, o menor numero é {num[0]} e a media de todos os numeros é {add / (count + 1)}')