#Escreva um programa que calcule o aumento de funcionarios
#Para salarios superiores a R$1250.00 calcule um aumento de 10%
#Para salarios inferiores ou iguais, o aumento é de 15%

salario = float(input('\nQual o salario do funcinario?: R$'))

if(salario <= 1250):
    aumento = 1.15
    novosalario = salario * aumento
elif(salario > 1250):
    aumento = 1.10
    novosalario = salario * aumento

print('\nSeu salario depois do aumento é de: R${:.2f}' .format(novosalario))