from time import sleep

#Aula N°20

print("Aula N°20 \n")
sleep(0.2)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------- #

def line(txt:str):
    if(len(txt) < 30):
        print('-' * 30)
        print(txt.center(30))
        print('-' * 30)
    else:
        print('-' * len(txt))
        print(txt)
        print('-' * len(txt))
def contador(*num:int):
    tam = len(num)
    print(f'Rebebi os valores {num} e são ao todo {tam} numeros')
def doblelist(lst:list):
    for x, y in enumerate(lst):
        lst[x] *= 2
def soma(*num:int):
    s = 0
    for x in num:
        s += x
    print(f'A soma entre {num} é {s}')

lista = [7, 2]

line('Bom dia, tudo bem? Espero que sim, este é o exemplo de um titulo que eu criei com uma função customizada')

contador(6, 6, 6, 6, 6, 6)
contador(2, 2)

doblelist(lista)

print(lista)

soma(1, 2, 3)
soma(1, 2, 3, 4)