# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

thing = str(input('Digite algo: '))

print(f'É alfanumerico? : {thing.isalnum()}')
print(f'É alfabetico? : {thing.isalpha()}')
print(f'É minuscula? : {thing.islower()}')
print(f'É maiuscula? : {thing.isupper()}')
print(f'É um espaço? : {thing.isspace()}')
print(f'É numerico : {thing.isnumeric()}')
