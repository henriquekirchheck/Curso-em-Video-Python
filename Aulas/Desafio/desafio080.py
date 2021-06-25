# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

num = [0]
fn = True

for x in range(0, 5):
    n = int(input('Digite um numero: '))
    for y, z in enumerate(num):
        print(y, z)
        if(num == [0]):
            num.clear()
        if(n in num):
            com = num.index(n)
            num.insert(com, n)
            break
        elif((n < z) and (y > 0)):
            num.insert(y, n)
        elif((n < z) and (y == 0)):
            num.insert(0, n)
            break
        elif((n > z) and (y == len(num) - 1)):
            num.append(n)
            break
        else:
            if(fn == True):
                num.append(n)
                fn = False
            elif(fn == False):
                None
    print(num)



        
    