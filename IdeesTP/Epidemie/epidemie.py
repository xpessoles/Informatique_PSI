#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import random as rd
from copy import deepcopy

def trace_carre(x,y,c,col):
    """ 
    Tracer un carré depuis (x,y) jusqu'à (x+x,y+c)
    """
    # Sain = 0 : blanc, bord noir
    # Infecte = 1 : noir
    # Retabli = 2 : vert
    # Decede = 3 : rouge
    col_b = col
    if col == 0:
        col,col_b = "w","k"
    if col == 1:
        col,col_b = "k","k"
    if col == 2:
        col,col_b = "g","g"
    if col == 3:
        col,col_b = "r","r"

    les_x = [x,x+c,x+c,x]
    les_y = [y,y,y+c,y+c]
    plt.fill(les_x,les_y,col)
    #plt.plot(les_x,les_y,col_b)
    

def trace_matrice(A):
    #l,c = A.shape
    l,c = len(A),len(A[0])
    for i in range(l):
        for j in range(c):
            
            trace_carre(i,j,1,A[i][j])

def trace_matrices(AA):
    for A in AA:
        trace_matrice(A)
        plt.pause(0.005) # pause avec duree en secondes
 


def grille(n):
    " Création d'une grille d'individus sains de taille nxn"
    M=[]
    for i in range(n) :
        L=[]
        for j in range(n):
            L.append(0)
        M.append(L)
    return M
    
def init(n):
    """
    Initialisation d'une grille de taille nxn
    avec une case infectée
    """
    G = grille(n)
    i = rd.randrange(0,n)
    j = rd.randrange(0,n)
    G[i][j]=1
    return G

def compte(G):
    n0,n1,n2,n3 = 0,0,0,0
    for i in len(G):
        for j in len(G[0]):
            if G[i][j] == 0 : n0+=1
            if G[i][j] == 1 : n1+=1
            if G[i][j] == 2 : n2+=1
            if G[i][j] == 3 : n3+=1
    return [n0,n1,n2,n3]




def est_exposee(G, i, j):
    n = len(G)
    if i == 0 and j == 0:
        return (G[0][1]-1)*(G[1][1]-1)*(G[1][0]-1) == 0
    elif i == 0 and j == n-1:
        return (G[0][n-2]-1)*(G[1][n-2]-1)*(G[1][n-1]-1) == 0
    elif i == n-1 and j == 0:
        return (G[n-1][1]-1)*(G[n-2][1]-1)*(G[n-2][0]-1) == 0
    elif i == n-1 and j == n-1:
        return (G[n-1][n-2]-1)*(G[n-2][n-2]-1)*(G[n-2][n-1]-1) == 0
    elif i == 0:
        return (G[0][j-1]-1)*(G[0][j+1]-1)*(G[1][j-1]-1)*(G[1][j]-1)*(G[1][j+1]-1) == 0
    elif i == n-1:
        return (G[n-1][j-1]-1)*(G[n-2][j-1]-1)*(G[n-2][j]-1)*(G[n-2][j+1]-1)*(G[n-1][j+1]-1) == 0
    elif j == 0:
        return (G[i-1][0]-1)*(G[i-1][1]-1)*(G[i][1]-1)*(G[i+1][1]-1)*(G[i+1][0]-1) == 0
    elif j == n-1:
        return (G[i-1][n-1]-1)*(G[i-1][n-2]-1)*(G[i][n-2]-1)*(G[i+1][n-2]-1)*(G[i+1][n-1]-1) == 0
    else:
        # a completer
        return (G[i-1][j-1]-1)*(G[i-1][j]-1)*(G[i-1][j+1]-1)*(G[i][j-1]-1)*(G[i][j+1]-1)*(G[i+1][j-1]-1)*(G[i+1][j]-1)*(G[i+1][j+1]-1) == 0
 
def bernoulli(p):
    x = rd.random()
    if x <= p:
        return 1
    else:
        return 0



def suivant(G,p1,p2):
    n=len(G)
    H=grille(n)
    for i in range(n):
        for j in range(n):
            if G[i][j]==0 and est_exposee(G,i,j) and bernoulli(p2)==1: 
                H[i][j]=1 
            elif G[i][j]==1: 
                if bernoulli(p1)==1:
                    H[i][j]=3
                else :
                    H[i][j]=2
            elif G[i][j]==2 or G[i][j]==3:
                H[i][j]=G[i][j]
    return H

def simulation(n,p1,p2):
    res = []
    G=init(n)
    res.append(deepcopy(G))
    H=suivant(G,p1,p2)
    res.append(deepcopy(H))
    while G!=H:
        G=H
        H=suivant(G,p1,p2)
        res.append(deepcopy(H))
    
    return res
    
    #return [resu[i]/n**2 for i in range(4)]


a = simulation(30,0.5,0.3)




plt.show()
plt.axis("equal")
trace_matrice(a[0])

trace_matrices(a)


#trace_carre(0,0,1,0)
plt.axis("equal")
plt.show()

#A = np.random.randint(4, size=(2,3))
