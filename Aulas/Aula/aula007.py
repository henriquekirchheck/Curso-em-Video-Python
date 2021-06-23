from time import sleep

print("Aula N°7 \n")
sleep(2)

''' Começo do Codigo '''


''' Formatação da linha '''
'''
nome = input('Qual é seu nome?: ')
print('Prazer em te conhecer {:20}!' .format(nome))
print('Prazer em te conhecer {:>20}!' .format(nome))
print('Prazer em te conhecer {:<20}!' .format(nome))
print('Prazer em te conhecer {:^20}!' .format(nome))
print('Prazer em te conhecer {:=^20}!' .format(nome))
'''

''' Calculos '''
'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, a subtração {}, o produto {} e a divisão {:.5f}' .format(s, su, m, d),  end=' | ')
print('Divisão inteira {} e potencia {}' .format(di, e))
'''

print('Fim da aula')
sleep(10)
