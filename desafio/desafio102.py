# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num:int, show:bool = False):
    """
    Feito para dar o fatorial de um numero
    :param num: O numero que você quer fatoriado
    :param show: Se você quer ou não ser mostrado a logica de como essa conta foi feita
    :return: Retorna os valores
    """
    result = 1
    lst = list()
    if(show == False):
        for loop in range(num, 0, -1):
            result *= loop
        return result
    elif(show == True):
        for loop in range(num, 0, -1):
            result *= loop
            lst.append(str(loop))
            if(loop != 1):
                lst.append('*')
            else:
                lst.append('=')
        lst.append(str(result))
        return (' '.join(lst))


print(fatorial(128, True))