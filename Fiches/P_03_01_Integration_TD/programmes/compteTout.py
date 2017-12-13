def compteTout(toutesLesCombinaisonsLigne,hauteur):
    nbCombi=len(toutesLesCombinaisonsLigne)
    somme=0
    i=0
    while i<nbCombi:
        temp=compteRangee(toutesLesCombinaisonsLigne,toutesLesCombinaisonsLigne[i],hauteur)
        somme+=temp
        i+=1
    return(somme)