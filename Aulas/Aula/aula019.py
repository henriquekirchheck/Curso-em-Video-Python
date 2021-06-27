from time import sleep

#Aula N°19

print("Aula N°19 \n")
sleep(0.2)

locadora = [{
    'titulo' : 'Star Wars',
    'ano' : 1977,
    'diretor' : 'George Lucas'
}, {
    'titulo' : 'Avengers',
    'ano' : 2012,
    'diretor' : 'Joss Whedon'
}, {
    'titulo' : 'Matrix',
    'ano' : 1999,
    'diretor' : 'Wachowski'
}]

print('-=-' * 8)

for i, f in enumerate(locadora):
    for k, v in  locadora[i].items():
        print(f'O {k} é {v}'.center(24))
    print('-=-' * 8)