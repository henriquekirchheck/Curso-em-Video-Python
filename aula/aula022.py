from time import sleep

#Aula N°22

print("Aula N°22 \n")
sleep(0.2)

try:
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    r = n1 / n2
except (ValueError, TypeError):
    print('Tivemos um erro com os valores digitados')
except ZeroDivisionError:
    print('Não é possivel dividir por zero')
except KeyboardInterrupt:
    print('\n O usuario parou o programa')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('\nTenha um bom dia')

