print('=====================')
print(' 10 Termos de um PA')
print('=====================')

loop = True
p = pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

while(loop == True):
    print('{} ->' .format(p), end=' ')
    p = p + r
    if(p == (r * 10) + pt):
        loop = False

print('Acabou')