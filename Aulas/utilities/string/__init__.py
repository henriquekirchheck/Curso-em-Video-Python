def line(txt, totalcaracters:int = 0, upper:bool = False):

    """
    Makes a line before and after the text you write
    :param txt: The text that you will be passing through
    :param totalcaracters: The number of caracters that it will be ocuping (Default = 0)
    :param upper: If the caracters will be on upper case
    """
    
    if(totalcaracters < (len(txt) + 2)):
        if(upper == True):
            print('-' * (len(txt) + 2))
            print(txt.upper().center(len(txt) + 2))
            print('-' * (len(txt) + 2))
        else:    
            print('-' * (len(txt) + 2))
            print(txt.center(len(txt) + 2))
            print('-' * (len(txt) + 2))
    else:
        if(upper == True):
            print('-' * (totalcaracters))
            print(txt.upper().center(totalcaracters))
            print('-' * (totalcaracters))
        else:    
            print('-' * (totalcaracters))
            print(txt.center(totalcaracters))
            print('-' * (totalcaracters))