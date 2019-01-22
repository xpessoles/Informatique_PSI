#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"
import numpy as np
import matplotlib.pyplot as plt

haut=5
larg = 2

def creer_pile(ht):
    """
    Crée et renvoie une pile de hauteur h : 
    Entrée : 
      * h(int)
    Sortie : 
      * (list)
    """
    return ht*['']

def empiler(pile):
    """
    On empile forcément des "*". On effectue cela en place. 
    """
    for i in range(len(pile)): 
        if pile[i] != "*" :
            pile[i] = "*"
            return None

def depiler(pile):
    """
    On empile forcément des "*". 
    """
    for i in range(len(pile)-1,-1,-1):
        if pile[i]=="*":
            pile[i]=""
            return "*"

def est_vide(pile):
    a=depiler(pile)
    if a=="*":
        empiler(pile)
        return a==""
    else : 
        return a==None

def taille_pile(pile,ht):
    pile_tmp = creer_pile(ht)
    cpt=0
    while not(est_vide(pile)):
        cpt+=1
        depiler(pile)
        empiler(pile_tmp)
    while not(est_vide(pile_tmp)):
        depiler(pile_tmp)
        empiler(pile)
    return cpt




def simulation_pile(ht,nb):
    pile = creer_pile(ht)
    simu = []
    simu.append(pile.copy())
    for i in range(nb):
        empiler(pile)
        simu.append(pile.copy())
    return simu
    

def circle(r,x,y):
    les_t = np.linspace(0,2*np.pi,100)
    les_x=(x+r*np.cos(les_t))
    les_y=(y+r*np.sin(les_t))
    return les_x,les_y
    
def trace_pile(pile):
    for i in range(len(pile)):
        if pile[i]=="*":
            x,y=circle(.4,0,i)
            plt.fill(x,y,"blue")
        if pile[i]=="":
            x,y=circle(.41,0,i)
            plt.fill(x,y,"white")
                
def trace_ecoulement(piles):
    plt.plot([-larg,larg,larg,-larg,-larg],[-1,-1,haut+1,haut+1,-1])
    plt.axis("equal")

    for pile in piles:
        trace_pile(pile)
        plt.pause(.2) # pause avec duree en secondes
    tmp =input("Presser une touche pour stopper...")
    plt.close()


piles = simulation_pile(5,8)
trace_ecoulement(piles)