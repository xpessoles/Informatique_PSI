#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"


import numpy as np
import matplotlib.pyplot as plt
import copy

# Largeur du sablier
larg = 11

# Hauteur du sablier
haut = 8

# Colonne de chute 
col = 5

def creation_sablier(larg,haut):
    pile = haut*[""]
    sablier = larg*[pile]
    return sablier

def empiler(sablier,col):
    # On empile une * sur la colonne col
    for i in range(sablier[col]):
        if sablier[col][i]!="*":
            sablier[col][i]="*"
            return None

def taille(sablier,col):
    i = 0
    while sablier[i][col]=="*":
        i=i+1
    return i
    
def chute_libre_grain(sablier,col,simu):
    ht = len(sablier[col])
    if sablier[ht-1][col]=="*":
        return None
    
    i=ht-1
    while sablier[i][col]!="*" and i>=0:
        sablier[i][col]="*"
        simu.append(copy.deepcopy(sablier))
        sablier[i][col]=""
        i=i-1
        
        
        
    
    
    


tas=[]

pile1=["","","","","","","",""]
pile2=pile1
pile3=pile1
pile4=pile1
pile5=pile1
pile7=pile1
pile8=pile1
pile9=pile1
pile10=pile1
pile11=pile1

pile6=["","","","","","","",""]
tas_tmp=[pile1,pile2,pile3,pile4,pile5,pile6,pile7,pile8,pile9,pile10,pile11]
tas.append(tas_tmp)

pile6=["*","","","","","","",""]
tas_tmp=[pile1,pile2,pile3,pile4,pile5,pile6,pile7,pile8,pile9,pile10,pile11]
tas.append(tas_tmp)

pile6=["*","*","","","","","",""]
tas_tmp=[pile1,pile2,pile3,pile4,pile5,pile6,pile7,pile8,pile9,pile10,pile11]
tas.append(tas_tmp)

pile6=["*","*","*","","","","",""]
tas_tmp=[pile1,pile2,pile3,pile4,pile5,pile6,pile7,pile8,pile9,pile10,pile11]
tas.append(tas_tmp)

pile6=["*","*","*","*","","","",""]
tas_tmp=[pile1,pile2,pile3,pile4,pile5,pile6,pile7,pile8,pile9,pile10,pile11]
tas.append(tas_tmp)


# Représentation d'une pile de piles


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

#draw_tas(tas)


def trace_ecoulement(tas):
    for t in tas:
        
        print('ii')
        trace_tas(tas)
        plt.pause(0.01) # pause avec duree en secondes
        
        


# On crée le sablier
sablier = creation_sablier(larg,haut)
simu = []
simu.append(copy.deepcopy(sablier))
chute_libre_grain(sablier,col,simu)
trace_ecoulement(simu)


"""
for t in tas:
    print('ii')
    trace_tas(tas)
    plt.pause(0.01) # pause avec duree en secondes
"""
"""
plt.plot([0,len(tas[0]),len(tas[0]),0,0],[-1,-1,len(tas[0][0]),len(tas[0][0]),-1],"white")
plt.axis("equal")
trace_tas(tas[1])
plt.pause(0.01)
trace_tas(tas[2])
plt.pause(0.01)
trace_tas(tas[3])
plt.pause(0.01)
trace_tas(tas[4])
plt.pause(0.01)

#trace_ecoulement(tas)
"""
plt.show()
