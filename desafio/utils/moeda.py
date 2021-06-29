def metade(valor:int, formatado:bool = False):
    """
    Retorna a metade do valor que você botou
    :param valor: o valor que você quer a metade
    :param formatado: Se você quer que o valor estaja formatado para R$
    :return: A metade do valor
    """
    valor /= 2

    if(formatado == True):
        valorformatado = ('R${:.2f}'.format(valor))
        valor = valorformatado.replace('.', ',')

    return valor

def dobro(valor:int, formatado:bool = False):
    """
    Retorna o dobro do valor que você botou
    :param valor: o valor que você quer o dobro
    :param formatado: Se você quer que o valor estaja formatado para R$
    :return: O dobro do valor
    """
    valor *= 2

    if(formatado == True):
        valorformatado = ('R${:.2f}'.format(valor))
        valor = valorformatado.replace('.', ',')

    return valor

def aumentar(valor:int, porcentagem:int, formatado:bool = False):
    """
    Retorna o valor que você colocou com a porcentagem de aumento
    :param valor: O valor que você quer aumentar uma porcentagem
    :param porcentagem: A porcentagem que você quer aumentar
    :param formatado: Se você quer que o valor estaja formatado para R$
    :return: O valor já aumentado
    """

    porcentagem /= 100
    porcentagem += 1
    valor *= porcentagem

    if(formatado == True):
        valorformatado = ('R${:.2f}'.format(valor))
        valor = valorformatado.replace('.', ',')

    return valor

def diminuir(valor:int, porcentagem:int, formatado:bool = False):
    """
    Retorna o valor que você colocou com a porcentagem de diminuição
    :param valor: O valor que você quer diminuir uma porcentagem
    :param porcentagem: A porcentagem que você quer diminuir
    :param formatado: Se você quer que o valor estaja formatado para R$
    :return: O valor já diminuido
    """

    porcentagem /= 100
    valor *= porcentagem

    if(formatado == True):
        valorformatado = ('R${:.2f}'.format(valor))
        valor = valorformatado.replace('.', ',')

    return valor