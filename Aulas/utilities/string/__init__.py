def line(txt, totalcaracters:int = 0, upper:bool = False):

    """
    Makes a line before and after the text you write
    :param txt: The text that you will be passing through
    :param totalcaracters: The number of caracters that it will be ocuping (Default = 0)
    :param upper: If the caracters will be on upper case
    """

    if(totalcaracters < (len(txt) + 2)):
        if(upper == True):
            text = ('-' * (len(txt) + 2), '\n', txt.upper().center(len(txt) + 2), '\n', '-' * (len(txt) + 2))
        else:    
            text = ('-' * (len(txt) + 2), '\n', txt.center(len(txt) + 2), '\n', '-' * (len(txt) + 2))
    else:
        if(upper == True):
            text = ('-' * (totalcaracters), '\n', txt.upper().center(totalcaracters), '\n', '-' * (totalcaracters))
        else:    
            text = ('-' * (totalcaracters), '\n', txt.center(totalcaracters), '\n', '-' * (totalcaracters))
    
    return text