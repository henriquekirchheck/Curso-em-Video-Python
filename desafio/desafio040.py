# Leia duas notas de um aluno e diga a media, depois diga se ele foi aprovado, esta em recuperação ou se ele foi reprovado

n1 = float(input('Qual é a primeira nota?: '))
n2 = float(input('Qual é a segunda nota?: '))

n = (n1 + n2) / 2

if(n < 5):
    print('O aluno foi reprovado')
elif(n > 6.9):
    print('O aluno foi aprovado')
else:
    print('O aluno ficou de recuperação')
    
