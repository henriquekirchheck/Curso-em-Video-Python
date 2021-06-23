#Pergunte o preço e a condição de pagamento e depois coloque descontos ou juros de acordo com o metodo de pagamento

preço = float(input('Preço: R$'))
pagamento = int(input('Selecione forma de pagamento:\n Dinheiro: 1 \n Cheque: 2 \n Cartão: 3 \nEscolha um metodo: '))

if(pagamento in(1, 2)):
    preço = preço - (preço * 0.10)
    print('\nO total de suas compras é R${:.2f}' .format(preço))
elif(pagamento == 3):
    pagamento = int(input('\nDiga em quantas vezes você quer pagar essa compra: '))
    if(pagamento == 1):
        preço = preço - (preço * 0.05)
        print('\nO total de suas compras é R${:.2f}' .format(preço))
    elif(pagamento == 2):
        print('\nO total de suas compras é R${:.2f}' .format(preço))
    elif(pagamento >= 3):
        preço = preço + (preço * 0.20)
        print('\nO total de suas compras é R${:.2f}' .format(preço))