from time import sleep

#Aula N°11

print("Aula N°11 \n")
sleep(0.2)

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}
nome = 'Henrique'

print('Praze em te conhecer, {}{}{}!' .format(cores['azul'], nome, cores['limpa']))

print(cores)

print('\x1b[7;41;45mOlá')
