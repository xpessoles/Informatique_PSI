#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"
import numpy as np
import matplotlib.pyplot as plt

haut = 5
larg = 2


    

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

