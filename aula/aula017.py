from time import sleep

#Aula N°17

print("Aula N°17 \n")
sleep(0.2)
""" 
num = [2, 5, 4, 4, 9, 1]
num.append(7)
num[2] = 3
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o 4')
print(num)
print(f'Esta lista tem {len(num)} elementos')
  """
v = 0
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

print(' e '.join(str(v) for v in valores))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')