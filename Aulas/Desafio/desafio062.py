print('=====================')
print(' 10 Termos de um PA')
print('=====================')

loop = True
loop1 = True
p = int(input('Primeiro Termo: '))
pt = p
r = int(input('Razão: '))
t = 10
counter = 0

while(loop == True):
    while(loop1 == True):   
        print('{} ->' .format(p), end=' ')
        p = p + r
        counter = counter + 1
        if(p == (r * t) + pt):
            print('Acabou')
            loop1 = False

    t = int(input('Quantos termos você quer mostar a mais? '))

    if(t == 0):
        loop = False
    else:
        pt = p
        loop1 = True       
print(f'Progressão finalizada com {counter} termos mostrados') 
