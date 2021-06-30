def metade(valor:float, formatado:bool = False):
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

def dobro(valor:float, formatado:bool = False):
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

def aumentar(valor:float, porcentagem:int, formatado:bool = False):
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

def diminuir(valor:float, porcentagem:int, formatado:bool = False):
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

def resumo(valor:float, redução:int = 0, aumento:int = 0):
    from utils.string import line
    
    line('Resumo do valor', totalcaracters=30, upper=True)

    valorformatado = ('{:.2f}'.format(valor))
    valorformatado = valorformatado.replace('.', ',')

    valordobro = ('{:.2f}'.format(dobro(valor)))
    valordobro = valordobro.replace('.', ',')
    
    valormetade = ('{:.2f}'.format(metade(valor)))
    valormetade = valormetade.replace('.', ',')

    valorredução = ('{:.2f}'.format(diminuir(valor, redução)))
    valorredução = valorredução.replace('.', ',')

    valoraumento = ('{:.2f}'.format(aumentar(valor, aumento)))
    valoraumento = valoraumento.replace('.', ',')
    
    print(f'Preço analizado:'.ljust(16), 'R$'.rjust(3), valorformatado.ljust(9))
    print(f'Dobro do preço:'.ljust(16), 'R$'.rjust(3), valordobro.ljust(9))
    print(f'Metade do preço:'.ljust(16), 'R$'.rjust(3), valormetade.ljust(9))

    if((redução and aumento) != 0):
        print(f'{redução}% de redução:'.ljust(16), 'R$'.rjust(3), valorredução.ljust(9))
        print(f'{aumento}% de aumento:'.ljust(16), 'R$'.rjust(3), valoraumento.ljust(9))
    elif(redução != 0):
        print(f'{redução}% de redução:'.ljust(16), 'R$'.rjust(3), valorredução.ljust(9))
    elif(aumento != 0):
        print(f'{aumento}% de aumento:'.ljust(16), 'R$'.rjust(3), valoraumento.ljust(9))

    print('-' * 30)