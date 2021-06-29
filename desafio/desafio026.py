# Faça um programa que leia uma frase pelo teclado e mostre
 # Quantas vezes aparece a letra "a".
 # Em que posição ela aparece pela primeira vez
 # Em que posição ela aparece pela ultima vez

frase = str(input('Frase: '))

frase1 = frase.strip().lower().count('a')
frase2 = frase.strip().lower().find('a') + 1
frase3 = frase.strip().lower().rfind('a') + 1

print('A letra "a" aparece {} vezes na frase' .format(frase1))
print('A primeita ocorencia da letra "a" aparece no {} caracter' .format(frase2))
print('A ultima ocorencia da letra "a" aparece no {} caracter' .format(frase3))