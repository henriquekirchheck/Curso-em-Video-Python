from time import sleep

#Aula N°12

print("Aula N°12 \n")
sleep(0.2)

nome = str(input('Qual seu nome: '))

if(nome == 'Henrique'):
    print('Seu nome é muito bonito')
elif((nome == 'Maria') or (nome == 'Pedro')):
    print('Seu nome é popular')
elif(nome in 'Ana Matilda Silverio'):
    print('Seu nome é legal')
else:
    print('seu nome é comum')