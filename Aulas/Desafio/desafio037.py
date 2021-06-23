#Peça para o usuario um numero inteiro e peça uma base de conversão

num = int(input('\nDigite um numero inteiro: '))
base = int(input('Escolha entre binario(1), octal(2) e hexadecimal(3): '))
print('')
hexcount = 10
done = False

numalf = {
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F',
}

if(base == 1):
    binary = []
    while(done == False):

        rest = num % 2
        num = num // 2
        binary.append(rest)

        if(num == 0):
            result = binary[::-1]
            
            done = True

if(base == 2):
    octal = []
    while(done == False):

        rest = num % 8
        num = num // 8
        octal.append(rest)

        if(num == 0):
            result = octal[::-1]
            
            done = True

if(base == 3):
    hexadecimal = []
    while(done == False):

        rest = num % 16
        num = num // 16
        hexadecimal.append(rest)

        if(num == 0):
            while(hexcount <= 15):
                count = [i for i, x in enumerate(hexadecimal) if x == hexcount]
                if(count != []):
                    for x,y in zip(count, numalf[hexcount]):
                        hexadecimal[x] = y
                hexcount = hexcount + 1
            result = hexadecimal[::-1]
            done = True
                

print(''.join(str(e) for e in result))