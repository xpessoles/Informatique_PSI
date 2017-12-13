def briques(n):
    if n==1:
        return(0)
    elif n==2 or n==3:
        return(1)
    else:
        return(briques(n-2)+briques(n-3))
 
nbIt=60       

temps=[]
listeN=list(range(2,nbIt))



def ajoutDeux(r):
    #r.append(1)
    #r.append(0)
    return(r+'10')

def ajoutTrois(r):
    #r.append(1)
    #r.append(0)
    #r.append(0)
    return(r+'100')

def remplissage(w,r,tailleMax):
    if w==tailleMax:
        #rows.insert(0,r)
        toutesLesCombis.append(r)
        #print('toutpile: ',rows)

    elif w<tailleMax:
        #print("w+2" ,w,r)
        remplissage(w+2,ajoutDeux(r),tailleMax)
        #print("w+3" ,w,r)
        remplissage(w+3,ajoutTrois(r),tailleMax)
        
global toutesLesCombis
toutesLesCombis=[]

tailleMax=9
        
remplissage(2,'0',tailleMax)
remplissage(3,'00',tailleMax)
    
print(toutesLesCombis)

# from time import clock
# 
# for i in range(2,nbIt):
#     t1=clock()
#     briques(i)
#     t2=clock()
#     temps.append(t2-t1)
# 
# import matplotlib.pyplot as plt
# plt.figure()
# plt.plot(listeN,temps)
    
    
# complexité expoenentielle

###

# tailleMax=7
# rangee1=[0,1,0,0,1,0,0]
# rangee2=[0,0,1,0,1,0,0]
# rangee3=[0,0,1,0,0,1,0]

def imprimeRangee(rangee):
    for i in range(len(rangee)):
        print(rangee[i],end="")
        
def sontCompatibles(r1,r2,tailleMax):
    for i in range(tailleMax-1):
        if r1[i]=='1' and r2[i]=='1':
            return(False)
    return(True)
    
def briques(taille):
    if taille<=1:
        return(0)
    elif taille==2 or taille==3:
        return(1)
    else:
        return(briques(taille-2)+briques(taille-3))

# complexité de l'algo -> exp

# tests élémentaires
LL5=[[0,1,0,0],[0,0,1,0]]
LL7=[[0,1,0,0,1,0],[0,1,0,1,0,0],[0,0,1,0,1,0]]
LL8=[[0,1,0,1,0,1,0],[0,1,0,0,1,0,0],[0,0,1,0,1,0,0],[0,0,1,0,0,1,0]]

    
def compteRangee(toutesLesLignes,r,hauteur):
    if hauteur==1:
        return(1)
    else:
        nbCombi,dim=len(toutesLesLignes),len(toutesLesLignes[0])
        somme=0
        i=0
        while i<nbCombi:
            if sontCompatibles(r,toutesLesLignes[i],dim):
                somme+=compteRangee(toutesLesLignes,toutesLesLignes[i],hauteur-1)
            i+=1
        return(somme)


def compteTout(toutesLesLignes,hauteur):
    nbCombi=len(toutesLesLignes)
    somme=0
    i=0
    while i<nbCombi:
        temp=compteRangee(toutesLesLignes,toutesLesLignes[i],hauteur)
        somme+=temp
        i+=1
    return(somme)
        
    
print("Le nombre de murs possibles vaut : ", compteTout(toutesLesCombis,3))

