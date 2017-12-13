def combinaisons(n):
    if n==1:
        return(0)
    elif n==2 or n==3:
        return(1)
    else:
        return(combinaisons(n-2)+combinaisons(n-3))