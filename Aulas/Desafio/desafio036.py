# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal sabendo que ela não pode exeder 30% do salario ou entãoo emprestimo será negado

valor = float(input('\nQual é o valor da casa?: R$'))
salario = float(input('Qual é o seu salario?: R$'))
ano = int(input('Em quantos anos a casa vai ser paga?: '))

presMensal = valor / (ano * 12)
print('\nR${:.2f}' .format(presMensal))

if(presMensal >= (salario * (30 / 100))):
    print('Recusado')
elif(presMensal <= (salario * (30 / 100))):
    print('Aprovado')
