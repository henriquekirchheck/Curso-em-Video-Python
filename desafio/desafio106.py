def PyHELP():
    from utils.string import line
    from utils.colours import colour
    from time import sleep

    colour('bold', 'white', 'blue')
    line('Sistema de ajuda PyHELP')
    colour()

    while True:
        colour('null', 'green')
        fun = str(input('Função ou biblioteca > '))
        colour()
        if(fun != 'exit'): 
            colour('bold', 'red')
            line(f'Pesquisando pela biblioteca ou função {fun}')
            colour()
            sleep(1.5)

            help(fun)
        else:
            colour()
            break

if __name__ == '__main__':
    PyHELP()