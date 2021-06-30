def leiaInt(inputof):
    from utils.colours import colour
    while True:
        try:
            a = int(input(inputof))
        except (TypeError, ValueError):
            colour('bold', 'red')
            print('Erro: por favor digite um numero inteiro valido')
            colour()
        except KeyboardInterrupt: 
            colour('bold', 'red')
            print('O usuario decidiu não digitar esse numero')
            colour()
            a = 0
            return a
        except Exception as error:
            colour('bold', 'red')
            print(f'Ocoreu um erro desconhecido: {error.__class__}')
            colour()
        else:
            return a

def leiaFloat(inputof):
    from utils.colours import colour
    while True:
        try:
            a = float(input(inputof))
        except (TypeError, ValueError):
            colour('bold', 'red')
            print('Erro: por favor digite um numero real valido')
            colour()
        except KeyboardInterrupt: 
            colour('bold', 'red')
            print('O usuario decidiu não digitar esse numero')
            colour()
            a = 0
            return a
        except Exception as error:
            colour('bold', 'red')
            print(f'Ocoreu um erro desconhecido: {error.__class__}')
            colour()
        else:
            return a

print('O valor inteiro digitado foi {} e o real foi {}'.format(leiaInt('Digite um numero inteiro: '), leiaFloat('Digite um numero real: ')))