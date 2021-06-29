import string
import colours

def PyHELP():
    print('{}{}'.format(colours.colour('bold', 'white', 'blue'), string.line('Sistema de ajuda PyHELP'), colours.colour('clear')))
    
if __name__ == '__main__':
    PyHELP()