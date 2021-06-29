
# Calcule a quantidade a se pagar po um carro alugado, se o dia custe R$60 e o km custe R$0,15

dia = int(input('Dias: '))
km = float(input('Km: '))

rs1 = dia * 60
rs2 = km * 0.15
rs = rs1 + rs2

print('O preço é R${:.2f}' .format(rs))