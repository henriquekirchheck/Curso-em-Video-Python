from time import sleep

print('Calculadora do Henrique')
loop = 'True'

while loop in('True', 'true', 'sim', 'Sim', 'Yes', 'yes', '1', 'y', 'Y', 's', 'S'):
    sleep(1)
    print('    ')

    n1 = int(input('N°1: '))
    print('    ')
    n2 = int(input('N°2: '))
    a = (input('+ - * / == != **: '))
    print('    ')

    print('    ')
    print('    ')

    sleep(2)

    if a == '+':
        n3 = n1 + n2
        print('O resultado de {} mais {} é {}' .format(n1,n2,n3))

    if a == '-':
        n3 = n1 - n2
        print('O resiltado de {} menos {} é {}' .format(n1,n2,n3))

    if a == '*':
        n3 = n1 * n2
        print('O resultado de {} vezes {} é {}' .format(n1,n2,n3))

    if a == '/':
        n3 = n1 / n2
        print('O resultado de {} dividido por {} é {}' .format(n1,n2,n3))

    if a == '==':
        if n1 == n2:
            n3 = ('são iguais')
        else:
            n3 = ('não são iguais')
        print('O numero {} e {} {}' .format(n1,n2,n3))

    if a == '!=':
        if n1 != n2:
            n3 = ('são diferentes')
        else:
            n3 = ('não são diferentes')
        print('O numero {} e {} {}' .format(n1,n2,n3))

    if a == "**":
        n3 = n1 ** n2
        print('A potencia de {} sobre {} é {}' .format(n1,n2,n3))

    idk = 'True'
    while idk == 'True':
        loop = input('Fazer outro calculo?: ')

        if loop not in('False', 'false', 'não', 'Não', 'nao', 'Nao', 'No', 'no', '0', 'n', 'N', 'True', 'true', 'sim', 'Sim', 'Yes', 'yes', '1', 'y', 'Y', 's', 'S'):
            print('Não é valido, tente denovo')
            print('')
        else:
            idk = 'False'

sleep(2)
print('')
print('A calculadora vai desligar em 60 segundos')
sleep(60)
