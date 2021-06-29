def line(txt:str, totallines:int = 0, upper:bool = False):
    if(totallines < (len(txt) + 2)):
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
            print('-' * (totallines))
            print(txt.upper().center(totallines))
            print('-' * (totallines))
        else:    
            print('-' * (totallines))
            print(txt.center(totallines))
            print('-' * (totallines))