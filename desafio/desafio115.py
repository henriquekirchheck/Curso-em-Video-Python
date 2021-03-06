from utils import colours, string, text

directory = 'D:/Programação/Curso-em-Video-Python/desafio/desafio115/pessoas.txt'

text.createFile(directory)

while True:
    right = False
    colours.colour('bold', 'cyan')
    string.line('menu principal', 60, True)
    colours.colour()

    print('{}1{} - {}Ver pessoas cadastradas{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline', 'purple', ret=True), colours.colour(ret=True)))
    print('{}2{} - {}Cadastrar nova pessoa{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline','purple', ret=True), colours.colour(ret=True)))
    print('{}3{} - {}Remover cadastro{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline','purple', ret=True), colours.colour(ret=True)))
    print('{}4{} - {}Apagar todos os cadastros{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline','purple', ret=True), colours.colour(ret=True)))
    print('{}5{} - {}Sair do Programa{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline','purple', ret=True), colours.colour(ret=True)))

    print('{}{}{}'.format(colours.colour('bold', 'cyan', ret=True) ,'-' * 60, colours.colour(ret=True)))

    while(right == False):
        try:
            option = int(input('{}Sua opção > '.format(colours.colour('null', 'green', ret=True))))
            if(option == 88224646):
                right = True
            elif((option >= 6) or (option <= 0)):
                print('{}Digite um valor valido{}'.format(colours.colour('null', 'red'), colours.colour(ret=True)))
            else:
                right = True
        except KeyboardInterrupt:
            print('{}O usuario decidiu parar o programa{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
            option = 5
            right = True
        except:
            print('{}Digite um valor inteiro valido{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))

    print('{}{}{}'.format(colours.colour('bold', 'cyan', ret=True) ,'-' * 60, colours.colour(ret=True)))
    
    if(option == 1):
        conteudo = text.readFile(directory)
        if(conteudo != []):
            for x, y in enumerate(conteudo):
                lista = y.split(',')

                if(lista[3] == 'x'):
                    None
                else:
                    print('{} - {} {} anos'.format(lista[0].rjust(7), lista[1].ljust(37), lista[2].rjust(3)))
        else:
            print('{}Não há pessoas cadastradas{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
    elif(option == 2):
        try:
            nome = str(input('Digite o nome: '))
        except KeyboardInterrupt:
            print('{}O usuario decidiu parar o processo{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
            nome = ''

        while True:
            if(nome != ''):
                try:
                    idade = int(input('Digite a idade: '))
                except KeyboardInterrupt:
                    print('{}O usuario decidiu parar o processo{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
                    nome = ''
                    break
                except:
                    print('{}Digite um valor inteiro valido{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
                else:
                    break
            else:
                break
        if(nome != ''):
            try:
                conteudo = text.readFile(directory)
                if(conteudo != []):
                    lista = conteudo[-1].split(',')
                    newindex = (int(lista[0]) + 1)
                else:
                    newindex = 0
            except:
                newindex = 0
            pessoa = f'{newindex},{nome},{idade},z'
            text.addLinetoFile(pessoa, directory)
    elif(option == 3):
        while True:
            try:
                n = int(input('Digite o numero da pessoa (CTRL + C para cancelar): '))
            except KeyboardInterrupt:
                print('{}O usuario decidiu parar o processo{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
                n = ''
                break
            except:
                print('{}Digite um valor inteiro valido{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
            else:
                break
        
        if(n != ''):
            conteudo = text.readFile(directory)
            if(conteudo != []):
                novalista = list()
                for x in conteudo:
                    lista = x.split(',')

                    if(lista[0] == str(n)):
                        lista[3] = 'x'
                        novalista.append(','.join(lista))
                    else:
                        novalista.append(','.join(lista))

                text.recreateFile(novalista, directory)

    elif(option == 4):
        while True:
            try:
                confirmação = str(input('Você tem certeza?: [S/N] ')).lower().strip()
                if(confirmação in 'sn'):
                    break
                else:
                    print('{}Digite um valor valido{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
            except KeyboardInterrupt:
                confirmação = 'n'
                break
        if(confirmação == 'n'):
            print('{}A remoção de todos os cadastros foi cancelada{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
        else:
            text.removeTextfromFile(directory)
    elif(option == 5):
        break
    elif(option == 88224646):
        while True:
            right = False    
            
            colours.colour('bold', 'cyan')
            string.line('Menu secreto', 60, True)
            colours.colour()

            print('{}1{} - {}Ver pessoas desativadas{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline', 'purple', ret=True), colours.colour(ret=True)))
            print('{}2{} - {}Ativar pessoa{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline','purple', ret=True), colours.colour(ret=True)))
            print('{}3{} - {}Sair do Menu Secreto{}'.format(colours.colour('bold', 'green', ret=True), colours.colour(ret=True), colours.colour('underline','purple', ret=True), colours.colour(ret=True)))

            print('{}{}{}'.format(colours.colour('bold', 'cyan', ret=True) ,'-' * 60, colours.colour(ret=True)))

            while(right == False):
                try:
                    option = int(input('{}Sua opção > '.format(colours.colour('null', 'green', ret=True))))
                    if((option >= 4) or (option <= 0)):
                        print('{}Digite um valor valido{}'.format(colours.colour('null', 'red'), colours.colour(ret=True)))
                    else:
                        right = True
                except KeyboardInterrupt:
                    print('{}O usuario decidiu parar o programa{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
                    option = 3
                    right = True
                except:
                    print('{}Digite um valor inteiro valido{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))

            print('{}{}{}'.format(colours.colour('bold', 'cyan', ret=True) ,'-' * 60, colours.colour(ret=True)))

            if(option == 1):
                conteudo = text.readFile(directory)
                if(conteudo != []):
                    for x, y in enumerate(conteudo):
                        lista = y.split(',')

                        if(lista[3] == 'z'):
                            None
                        else:
                            print('{} - {} {} anos'.format(lista[0].rjust(7), lista[1].ljust(37), lista[2].rjust(3)))
                else:
                    print('{}Não há pessoas cadastradas{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
            elif(option == 2):
                while True:
                    try:
                        n = int(input('Digite o numero da pessoa (CTRL + C para cancelar): '))
                    except KeyboardInterrupt:
                        print('{}O usuario decidiu parar o processo{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
                        n = ''
                        break
                    except:
                        print('{}Digite um valor inteiro valido{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
                    else:
                        break
            
                if(n != ''):
                    conteudo = text.readFile(directory)
                    if(conteudo != []):
                        novalista = list()
                        for x in conteudo:
                            lista = x.split(',')

                            if(lista[0] == str(n)):
                                lista[3] = 'z'
                                novalista.append(','.join(lista))
                            else:
                                novalista.append(','.join(lista))

                        text.recreateFile(novalista, directory)
            elif(option == 3):
                break