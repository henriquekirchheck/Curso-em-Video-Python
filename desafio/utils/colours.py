def colour(style = 'clear', text = 'white', back = 'black', ret:bool = False):
    """
    Will change the colour of the text and of the background, and even change the style of the letter
    :param style: Changes the style ({'clear' : 'Get everithing to normal'}, 'bold', 'underline', 'negative')
    :param text: Changes the colour of the text ('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'gray', 'white')
    :param back: Changes the colour of the background ('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'gray', 'white')
    :return: The code that changes to the respective colour
    """
    dicionary = {
    
        'text': {
            #Cores
            'null': '0',
            'black': '30',
            'red': '31',
            'green': '32',
            'yellow': '33',
            'blue': '34',
            'purple': '35',
            'cyan': '36',
            'gray': '37',
            'white': '97'
        },

        'back': {
            #Background
            'null': '0',
            'black': '40',
            'red': '41',
            'green': '42',
            'yellow': '43',
            'blue': '44',
            'purple': '45',
            'cyan': '46',
            'gray': '47',
            'white': '107'
        },

        'style': {
            #Estilo
            'null': '0',
            'bold': '1',
            'underline': '4',
            'negative': '7'
        }

    }

    if(style == 'clear'):
        if(ret == False):
            print('\x1b[m', end='')
        else:
            return('\x1b[m')
    else:
        defstyle = dicionary['style'][style]
        deftext = dicionary['text'][text]
        defback = dicionary['back'][back]

        if(ret == False):
            print(f'\x1b[{defstyle};{deftext};{defback}m', end='')
        else:
            return (f'\x1b[{defstyle};{deftext};{defback}m')


