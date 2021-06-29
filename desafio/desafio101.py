# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano:int):
    import datetime as dt
    hjano = dt.date.today().year

    idade = hjano - ano

    if(idade < 16):
        return 'negado', idade
    elif(idade >= 18):
        return 'obrigatorio', idade
    else:
        return 'opcional', idade

ano = int(input('Qual é o ano que você nasceu?: '))

print(f'O seu voto é {voto(ano)[0]}, pois você tem {voto(ano)[1]} anos')