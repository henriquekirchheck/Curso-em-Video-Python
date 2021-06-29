
# Leia um preço de um produto e mostre seu novo preço com 5% de desconto #

vo = float(input('Preço = R$'))
des = int(input('Desconto = '))
print(' ')

des = des / 100
dg = vo * des
vd = vo * (1 - des)

print('Valor original: R${:.2f} \nDesconto ganho: R${:.2f} \nValor descontado: R${:.2f}' .format(vo, dg, vd))