# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
escolha = str('Escolha entre o jeito certo e errado: [C/E] ').strip().lower()

if(escolha == 'e'):

    palavras = ('aprender', 'programar', 'linguagem', 'bb')
    vogals = list()
    count = 0

    for x in palavras:
        vogals.clear()
        a = e = i = o = u = 0 
        while True:
            if(x.find('a', a) != -1 ):
                vogals.append('a')
                a = x.find('a', a) + 1
            elif(x.find('e', e) != -1 ):
                vogals.append('e')
                e = x.find('e', e) + 1
            elif(x.find('i', i) != -1 ):
                vogals.append('i')
                i = x.find('i', i) + 1
            elif(x.find('o', o) != -1 ):
                vogals.append('o')
                o = x.find('o', o) + 1
            elif(x.find('u', u) != -1 ):
                vogals.append('u')
                u = x.find('u', u) + 1
            else:
                if(vogals != []):
                    print('Na palavra {} temos {}' .format(x.upper(), ' '.join(vogals)))
                    break
                else:
                    print(f'Na palavra {x.upper()} não tem uma vogal')
                    break

elif(escolha == 'c'):
    palavras = ('aprender', 'programar', 'linguagem')

    for x in palavras:
        print()
        print(f'A palavra {x} tem as vogais ', end='')
        for y in x:
            if(y in 'aeiou'):
                print(y, end='')