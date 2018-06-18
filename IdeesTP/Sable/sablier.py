#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"


import numpy as np
import matplotlib.pyplot as plt
import copy
import random

# Largeur du sablier
larg = 5#11

# Hauteur du sablier
haut = 5#8

# Colonne de chute 
col = 1#5

nb_grain=8

def creation_sablier(larg,haut):
    sablier=[]
    for i in range (larg):
        sablier.append(haut*[""])
        
    return sablier

def empiler(sablier,col):
    # On empile une * sur la colonne col
    for i in range(len(sablier[col])):
        if sablier[col][i]!="*":
            sablier[col][i]="*"
            return None

def depiler(sablier,col):
    # On dépile une * sur la colonne col
    for i in range(len(sablier[col])-1,-1,-1):
        if sablier[col][i]=="*":
            sablier[col][i]=""
            return None

def taille(sablier,col):
    i = 0
    while sablier[col][i]=="*":
        i=i+1
    return i
    
def chute_libre_grain(sablier,col,simu):
    ht = len(sablier[col])
    if sablier[col][ht-1]=="*":
        print("Colonne pleine")
        return None
    
    i=ht-1
    # Pour décrire la chute d'un grain ou ajoute puis on enlève * à chaque étage. 
    while sablier[col][i]!="*" and i>=0:
        sablier[col][i]="*"
        simu.append(copy.deepcopy(sablier))
        sablier[col][i]=""
        i=i-1
    sablier[col][i+1]="*"
        
        
def chute_grain(sablier,col,simu):
    
    #Recherche du sens
    # Cas du premier grain
    if taille(sablier,col)==1 and taille(sablier,col-1)==0 and taille(sablier,col+1)==0:
        return None
    
    col_ch = col   # Colonne de chute
    col_g = col-1  # Colonne de gauche
    col_d = col+1  # Colonne de droite
    
    sens=0
    # Sens alaéatoire
    tcol_g = taille(sablier,col_g)
    tcol_d = taille(sablier,col_d)
    tcol = taille(sablier,col)
    
    # SENS A REVOIR ???
    
    print(col,tcol_g,tcol_d,taille(sablier,col_ch))
    if tcol_g == tcol_d and (taille(sablier,col_ch)>tcol_g or  taille(sablier,col_ch)>tcol_d):
        sens = random.choice([-1,1])
    if sens == 0 :  
        sens = random.choice([-1,1])
    #sens=1
    print(str("sens"),sens)    
    print(str("col"),col)    
    #if col+sens!=0 or col+sens!= len(sablier) : #-1 ?
    
    # On continue l'évolution tant que
    # le grain n'a pas atteint le bord gauche
    
    # Conditions d'arrêt : bord gauche, bord droit, taille colonne nulle, 
    #                      fin d'évolution natureuue
    while col!=0 and (col != len(sablier)-1) and taille(sablier,col)!=0 and not(taille(sablier,col+sens)==taille(sablier,col)-1): #and taille(sablier,col+sens+sens)!=taille(sablier,col)-1 :
        # On supprime le grain en haut de la colonne, et on l'ajoute a coté
        depiler(sablier,col)
        #simu.append(copy.deepcopy(sablier))
        empiler(sablier,col+sens)
        simu.append(copy.deepcopy(sablier))
        col=col+sens
        print(len(sablier),col,sens)

def simulation(nb_grain,larg,haut):
    sablier = creation_sablier(larg,haut)
    simu = []
    simu.append(copy.deepcopy(sablier))
    col = larg//2
    while nb_grain>0:
        # Chute libre du grain
        chute_libre_grain(sablier,col,simu)
        chute_grain(sablier,col,simu)
        nb_grain = nb_grain-1
    return simu


def circle(r,x,y):
    les_t = np.linspace(0,2*np.pi,100)
    les_x=(x+r*np.cos(les_t))
    les_y=(y+r*np.sin(les_t))
    return les_x,les_y

def trace_tas(tas):
    for i in range(len(tas)):
        for j in range(len(tas[i])):
            if tas[i][j]=="*":
                x,y=circle(.4,i,j)
                plt.fill(x,y,"blue")
            if tas[i][j]=="":
                x,y=circle(.41,i,j)
                plt.fill(x,y,"white")
#draw_tas(tas)


def trace_ecoulement(tas):
    for t in tas:
        trace_tas(tas)
        plt.pause(0.01) # pause avec duree en secondes
        
        

simu = simulation(nb_grain,larg,haut)


"""
# Chute d'un grain
chute_libre_grain(sablier,col,simu)
chute_libre_grain(sablier,col,simu)
chute_libre_grain(sablier,col,simu)
chute_libre_grain(sablier,col,simu)
"""
#trace_ecoulement(simu)


plt.plot([-1,larg,larg,-1,-1],[-1,-1,haut+1,haut+1,-1])
plt.axis("equal")


for t in simu:
    trace_tas(t)
    plt.pause(0.5)


plt.show()
