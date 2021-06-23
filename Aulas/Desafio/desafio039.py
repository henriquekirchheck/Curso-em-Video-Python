#Faça um programa que leia o ano de nascimento de alguem e diga se ele ainda vai se alistar no serviço militar, ta na hora de se alistar ou se já passou da hora de se alistar e quato tempo falta ou já se passou

from datetime import date

jovem = int(input('Qual o ano de seu nascimento?: '))

idade = date.today().year - jovem
tempo = idade - 18

if(tempo == 0):
    print('É a hora de se alistar!')
elif(tempo < 0):
    print('Você tera que se alistar em {} anos' .format(tempo * -1))
elif(tempo > 0):
    print('Você está {} anos atrasado' .format(tempo))