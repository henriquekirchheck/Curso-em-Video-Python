
# Leia o Salario de um funcionario e mostre seu novo salário, com 15% de aumento #

vo = float(input('Salário = R$'))
des = int(input('Aumento = '))
print(' ')

des = des / 100
dg = vo * des
vd = vo * (1 + des)

print('Valor original: R${:.2f} \nAumento ganho: R${:.2f} \n Valor aumentado: R${:.2f}' .format(vo, dg, vd))