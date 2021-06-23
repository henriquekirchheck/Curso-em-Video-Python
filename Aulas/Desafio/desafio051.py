print('=====================')
print(' 10 Termos de um PA')
print('=====================')

p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

for loop in range(p, ((r * 10) + p), r):
    print('{} ->' .format(loop), end=' ')
print('Acabou')