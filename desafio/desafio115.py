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

            if((option >= 6) or (option <= 0)):
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
                lista = y.split()

                for a, b in enumerate(lista):
                    if(a == 0):
                        l = b.split(sep='_')
                        fnome = ' '.join(l)

                print('{} - {} {} anos'.format(str(x).center(3), fnome.ljust(44), lista[1].rjust(3)))
        else:
            print('{}Não há pessoas cadastradas{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
    elif(option == 2):
        try:
            nome = str(input('Digite o nome: '))
        except KeyboardInterrupt:
            print('{}O usuario decidiu parar o processo{}'.format(colours.colour('null', 'red', ret=True), colours.colour(ret=True)))
            nome = ''
        else:
            nome = '_'.join(nome.split())

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
            pessoa = f'{nome} {idade}'
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
            text.removeLinefromFile(n, directory)
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
