# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'eleves')
import tris

import random as rd
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000000) # cette ligne permet de modifier le nombre
# de boucles récursives autorisées (normalement de 1000)


# Q1.1

def question_1 () :
    longueur = [n for n in range(0,1001,100)]
    moyenne_insert = []
    moyenne_rapide = []
    moyenne_fusion = []
    moyenne_sort = []
    for n in longueur :
        # n = longueur des listes que l'on va trier
        temps_insert = []
        temps_rapide = []
        temps_fusion = []
        temps_sort = []
        for m in range(10) :
            # on va trier 10 listes et faire la moyenne des temps de calcul
            M = [rd.randint(0,n) for i in range(n)] # liste aléatoire de
                        # n éléments entre 0 et n
                        
            L = M.copy()            
            temps=time.time()
            tris.tri_insertion(L)
            temps = time.time() - temps
            temps_insert.append(temps)

            L = M.copy()
            temps=time.time()
            tris.tri_fusion(L,0,n-1)
            temps = time.time() - temps
            temps_fusion.append(temps)
            
            L = M.copy()
            temps=time.time()
            tris.tri_quicksort(L,0,n-1)
            temps = time.time() - temps
            temps_rapide.append(temps)
            
            L = M.copy()
            temps=time.time()
            L.sort()
            temps = time.time() - temps
            temps_sort.append(temps)
            
        moyenne_insert.append(sum(temps_insert)/len(temps_insert))
        moyenne_rapide.append(sum(temps_rapide)/len(temps_rapide))
        moyenne_fusion.append(sum(temps_fusion)/len(temps_fusion))
        moyenne_sort.append(sum(temps_sort)/len(temps_sort))

    plt.clf()
    plt.grid()
    plt.xlabel('taille de la liste')
    plt.ylabel('temps de tri en seconde')
    plt.plot(longueur,moyenne_insert,label='insertion')
    plt.plot(longueur,moyenne_rapide,label='rapide')
    plt.plot(longueur,moyenne_fusion,label='fusion')
    plt.plot(longueur,moyenne_sort,label='sort')
    plt.legend(loc='upper left')
    plt.savefig("question_1.png")
        


# Q1.2
def question_2 () :
    # on commencera avec des listes de 10000 éléments, en allant
    # de 1000 en 1000, sinon le temps de calcul est trop long.
    longueur = [n for n in range(10000,20001,1000)]
    moyenne_rapide = []
    moyenne_fusion = []
    moyenne_sort = []
    for n in longueur :
        # n = longueur des listes que l'on va trier
        temps_insert = []
        temps_rapide = []
        temps_fusion = []
        temps_sort = []
        for m in range(10) :
            # on va trier 10 listes et faire la moyenne des temps de calcul
            M = [rd.randint(0,n) for i in range(n)] # liste aléatoire de
                        # n éléments entre 0 et n
                        

            L = M.copy()
            temps=time.time()
            tris.tri_fusion(L,0,n-1)
            temps = time.time() - temps
            temps_fusion.append(temps)
            
            L = M.copy()
            temps=time.time()
            tris.tri_quicksort(L,0,n-1)
            temps = time.time() - temps
            temps_rapide.append(temps)
            
            L = M.copy()
            temps=time.time()
            L.sort()
            temps = time.time() - temps
            temps_sort.append(temps)
            

        moyenne_rapide.append(sum(temps_rapide)/len(temps_rapide))
        moyenne_fusion.append(sum(temps_fusion)/len(temps_fusion))
        moyenne_sort.append(sum(temps_sort)/len(temps_sort))

    plt.clf()
    plt.grid()
    plt.xlabel('taille de la liste')
    plt.ylabel('temps de tri en seconde')
    plt.plot(longueur,moyenne_rapide,label='rapide')
    plt.plot(longueur,moyenne_fusion,label='fusion')
    plt.plot(longueur,moyenne_sort,label='sort')
    plt.legend(loc='upper left')
    plt.savefig("question_2.png")
    

# Q1.4

def question_4 () :
    n = 100000
    M = [rd.randint(0,n) for i in range(n)] # liste aléatoire
                                    # de n éléments entre 0 et n
    M.sort() # on trie L

    L = M.copy()                          
    temps=time.time()
    tris.tri_fusion(L,0,n-1)
    temps_fusion = time.time() - temps
            
    L = M.copy() 
    temps=time.time()
    tris.tri_quicksort(L,0,n-1)
    temps_rapide = time.time() - temps
            
    L = M.copy() 
    temps=time.time()
    L.sort()
    temps_sort = time.time() - temps

    return(temps_rapide,temps_fusion,temps_sort)

# Q2.1

def conversion (temps) :
    """ convertit une chaîne de caractères donnant un temps en
    heures, minutes, secondes, en un nombre de secondes."""
    L = temps.split()
    s = 3600*int(L[0][:len(L[0])-1])+60*int(L[1][:len(L[1])-1])\
    +int(L[2][:len(L[2])-2])
    return s
    
def charge_classement (fichier) :
    f = open(fichier, 'r')
    L = f.readlines()
    f.close()

    classement = []

    for l in L :
        m = l.split('\t')
        classement.append([m[1],m[2],conversion(m[4])])

    return classement

# Q2.2

LG=charge_classement('eleves/classement_general.txt')
L10=charge_classement('eleves/etape_10.txt')

def ajout_temps(L1,L2):
    """L1 est la classement de l'étape et L2 le classement général
    certains ont été disqualifiés ou ont abandonné"""
    L=[]
    for dossard in L1:
        L.append(dossard.copy()) # problèmes d'aliasing
        d=dossard[1]
        i=0
        while d != L2[i][1]: #attention certains n'ont pas fait
            # l'étape complètement et sont disqualifiés
            i += 1
        L[-1][-1] += L2[i][-1]
    return L

# Q3.1

f=open('eleves/films_martiniere.csv','r')
ligne1=f.readline()
fichier=f.readlines()
f.close()


L=[]
for ligne in fichier:
    ligne=ligne.replace('"','')#enlever les guillemets
    ligne=ligne.split(';')#création d'une liste en coupant au niveau des ;
    ligne[-1]=ligne[-1].rstrip('\n')
    ligne[-1]=int(ligne[-1])#remplacer la chaine de caractères par un entier
    ligne[1]=int(ligne[1])#remplacer la chaine de caractères par un entier
    L.append(ligne)

# Q3.2

M = sorted(L, key = lambda colonnes : colonnes[-1], reverse = True)

# Q3.3

def segmente_modifie_bis(tab,i,j):
    """
    Segmentation d'un tableau par rapport à un pivot.
    Keyword arguments: 
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la segmentation
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
        k (int) -- indice de la place du pivot
    """
    g =i+1
    d=j
    p=tab[i][0]
    while g<=d :
        while d>=0 and tab[d][0]>p:
            d=d-1
        while g<=j and tab[g][0]<=p:
            g=g+1
        if g<d :
            tab[g],tab[d]=tab[d],tab[g]
            d=d-1
            g=g+1
    k=d
    tab[i],tab[d]=tab[d],tab[i]
    return k
    
def tri_quicksort_modifie_bis(tab,i,j):
    """
    Tri d'une liste par l'utilisation du tri rapide (Quick sort).
    Keyword arguments:
    Entrées :
        tab (list) -- liste de nombres
        i,j (int) -- indices de fin et de début de la zone de tri
    Sorties :    
        tab (list) -- liste de nombres avec le pivot à sa place définitive
    """
    if i<j :
        k = segmente_modifie_bis(tab,i,j)
        tri_quicksort_modifie_bis(tab,i,k-1)
        tri_quicksort_modifie_bis(tab,k+1,j)

N = L.copy()
tri_quicksort_modifie_bis(N,0,len(N)-1)
