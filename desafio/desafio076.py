# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular
product = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro', 'Computador')
prices = ('1.75', '2.00', '15.90', '25.00', '4.20', '9.99', '120.32', '22.30', '34.90', '10000.00')
print('-' * 30)
print('Listagem de preços'.center(30))
print('-' * 30)
for x in range(0, len(product)):
    print(product[x].ljust(18), f'R$ {prices[x].rjust(8)}')
