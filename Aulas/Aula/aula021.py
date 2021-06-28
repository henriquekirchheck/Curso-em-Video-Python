from time import sleep

#Aula N°21

print("Aula N°21 \n")
sleep(0.2)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #

def contador(start:int = 0, end:int = 10, passo:int = 1):
    """
    --> Faz uma contagem e mostra na tela
    :param start: inicio da contagem (Se não informado, o default é: 0)
    :param end: fim da contagem (Se não informado, o default é: 10)
    :param passo: passo da contagem (Se não informado, o default é: 1)
    :return: sem retorno
    Função criado por mim
    """
    from time import sleep
    if((start > end) and (passo < 0)):
        passo += (passo * -2)
        print(f'O inicio é {end}, o fim é {start} e o passo é {passo}')
        for loop in range(end, (start + 1), passo):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    elif(start > end):
        print(f'O inicio é {start}, o fim é {end} e o passo é {passo}')
        for loop in reversed(range(end, (start + 1), passo)):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    elif(passo < 0):
        passo += (passo * -2)
        print(f'O inicio é {end}, o fim é {start} e o passo é {passo}')
        for loop in reversed(range(start, (end + 1), passo)):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    elif(passo == 0):
        passo = 1
        print(f'O inicio é {start}, o fim é {end} e o passo é {passo}')
        for loop in range(start, (end + 1), passo):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
    else:
        print(f'O inicio é {start}, o fim é {end} e o passo é {passo}')
        for loop in range(start, (end + 1), passo):
            sleep(0.15)
            print(loop, end=' - ')
        print('Fim')
def teste():
    global n
    n = 82
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
def par(n:int):
    if((n % 2) == 0):
        return True
    else:
        return False


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são: {f1}, {f2}, {f3}')

print(par(7 + 1))
#print(input.__doc__)
#help(input)

#help(contador)

#contador()

#n = 2

#teste()

#print(f'n = {n}\n\n')

#print(somar(3,2,5), somar(2,2), somar(6))


