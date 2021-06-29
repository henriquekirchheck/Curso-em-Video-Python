def metade(valor:int):
    """
    Retorna a metade do valor que você botou
    :param valor: o valor que você quer a metade
    :return: A metade do valor
    """
    valor /= 2
    return valor

def dobro(valor:int):
    """
    Retorna o dobro do valor que você botou
    :param valor: o valor que você quer o dobro
    :return: O dobro do valor
    """
    valor *= 2
    return valor

def aumentar(valor:int, porcentagem:int):
    """
    Retorna o valor que você colocou com a porcentagem de aumento
    :param valor: O valor que você quer aumentar uma porcentagem
    :param porcentagem: A porcentagem que você quer aumentar
    :return: O valor já aumentado
    """

    porcentagem /= 100
    porcentagem += 1
    valor *= porcentagem

    return valor

def diminuir(valor:int, porcentagem:int):
    """
    Retorna o valor que você colocou com a porcentagem de diminuição
    :param valor: O valor que você quer diminuir uma porcentagem
    :param porcentagem: A porcentagem que você quer diminuir
    :return: O valor já diminuido
    """

    porcentagem /= 100
    valor *= porcentagem

    return valor