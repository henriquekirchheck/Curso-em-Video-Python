from time import sleep

#Aula N°15

print("Aula N°15 \n")
sleep(0.2)

n = s = 0
c = 1

while True:
    n = int(input('Digite um numero: '))
    if(n == 999):
        break
    s += n
    c += 1
print(f'A soma vale {s}')
