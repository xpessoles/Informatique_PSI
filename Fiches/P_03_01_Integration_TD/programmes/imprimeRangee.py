def imprimeRangee(rangee):
    '''rangee est une liste de 2 et de 3'''
    c=''
    for element in rangee:
        if element==2:
            c+='01'
        else:
            c+='001'
    return c[:-1]