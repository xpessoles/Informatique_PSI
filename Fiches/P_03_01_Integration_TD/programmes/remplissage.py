def remplissage(w,r,tailleMax):
    if w==tailleMax:
        toutesLesCombis.append(r)
    elif w<tailleMax:
        remplissage(w+2,r+'10',tailleMax)
        remplissage(w+3,r+'100',tailleMax)
        
global toutesLesCombis
toutesLesCombis=[]

tailleMax=9
        
remplissage(2,'0',tailleMax)
remplissage(3,'00',tailleMax)