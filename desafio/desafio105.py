# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#  Quantidade de notas
#  A maior nota
#  A menor nota
#  A media da turma
#  A situação (opcional)

def notas(*notas:float, situação:bool = False):

    """
    Uma função feita para mostrar:
    A quantidade de notas
    A maior nota
    A menor nota
    A media da turma
    A situação da turma

    :param notas: Uma ou mais notas de alunos
    :param situação: A situação da turma (opcional)
    :return: Dicionario com todas as informações mostradas acima

    """

    totalnota = dict()
    quantidenotas = len(notas)
    maiornota = 0
    menornota = 10
    media = 0

    for x in notas:
        if(x > maiornota):
            maiornota = x
        if(x < menornota):
            menornota = x
        media += x
    media /= quantidenotas

    totalnota['quantidade'] = quantidenotas
    totalnota['maiornota'] = maiornota
    totalnota['menornota'] = menornota
    totalnota['media'] = media

    if(situação == True):
        if(media < 4):
            totalnota['situação'] = 'horrivel'
        elif(media > 7):
            totalnota['situação'] = 'otima'
        else:
            totalnota['situação'] = 'rasoavel'

    return totalnota


print(notas(10, 10, 10, 10, 10, situação=True))