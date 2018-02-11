#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import math as m


def horner(L,t):
    if(len(L))==0:
        return 0
    else : 
        return horner(L[0:len(L)-1],t)*t+L[len(L)-1]
        
def deCasteljau(P, i, j, t):
    """
    Retourne l'abscisse(ou l'ordonnées) d'un point de la courbe de Bézier pour un paramètre donné.
    Entrées : 
     * P (list) : listes des abscisses (ou des ordonnéees) des poles
     * i,j (int) : poles considérés
     * t (float) : paramètre compris entre O et 1
    Sortie : 
     * float : abscisse ou ordonnée d'un point de la courbe 
    """

    if j == 0:
        return P[i]
    else : 
        return deCasteljau(P,i,j-1,t)*(1-t)+deCasteljau(P,i+1,j-1,t)*t


def fact(n):
    """
    Calcul de n! = 1 x 2 x ... x (n-1) x n
    Par convention, 0! = 1
    n doit être un int
    """
    if n==0 :
        return 1
    else : 
        return n*fact(n-1)


def coef_binom(i,n):
    """
    Retourne le coefficient binomial : 
    C_n^i = n! / (i! (n-i)!)
    """
    res = fact(n)/(fact(i)*fact(n-i))
    return res

def calculPointCourbe(poles,u):
    """ 
    Retourne le point de la courbe de Bézier pour un paramètre donné.
    Entrées :
        * poles (list): liste des coordonnées des poles [[x1,y1],[x2,y2],...]
        * u (float) : paramètre appartenant à [0,1]
    Sortie :
        * pointM (list): point appartenant à la courbe de Bézier au paramètre u
    """
    px,py = [],[]
    for i in range(len(poles)):
        px.append(poles[i][0])
        py.append(poles[i][1])
    
    pointM = [fonctionBernstein(px,u),fonctionBernstein(py,u)]
    return pointM

    
def fonctionBernstein(p,u):
    """
    Calcul d'une des coordonnées d'un point appartenant à une courbe de Bézier.
        Entrées :
            * p (list): tableau contenant l'abscisse des poles
            * u (float): paramètre
        Sortie :
            * x (float) : une des coordonnées (suivant x ou y) d'un point de la courbe
    """
    n = len(p)
    x=0
    for i in range(n):
        x=x+coef_binom(i,n-1)*pow(u,i)*pow((1-u),n-i-1)*p[i]
    return x



def tkdeCaseljau(poles,nb):
    """
    Génération de points en utilisant l'algorithme de casteljau
    """
    les_u = [u/nb for u in range(nb+1)]
    poles_x = [e[0] for e in poles]
    poles_y = [e[1] for e in poles]
    res = []
    for t in les_u:
        res.append(deCasteljau(poles_x,0,3,t))
        res.append(deCasteljau(poles_y,0,3,t))
    return res

def tkBezier(poles,nb):
    """
    Génération de points en utilisant l'algorithme de casteljau
    """
    les_u = [u/nb for u in range(nb+1)]
    poles_x = [e[0] for e in poles]
    poles_y = [e[1] for e in poles]
    res = []
    for t in les_u:
        pt = calculPointCourbe(poles,t)
        res.append(pt[0])
        res.append(pt[1])
    return res

    

class main_fen(Frame):
    """
    Classe associée à la fenêtre principale de l'application.
    
    """
    def __init__ (self,parent):
        super().__init__(parent)
        self.pack(fill='both', expand=1)
        self.width = 600
        self.height = 450
        self.ptA = ("A",100,100)
        self.ptB = ("B",100,400)
        self.ptC = ("C",500,400)
        self.ptD = ("D",500,100)
        self.generate_poles()
        
        self.canvas = Canvas(self, width=self.width, height=self.height, background="#e8e8e8")
        self.canvas.pack(padx=2, pady=2) 
        
        # Création des points
        self.creation_points()
        
    def move(self, event):
        def node_center(tag):
            """ Renvoie le centre du noeud étant donné
                son rectangle englobant
            """
            x1, y1, x2, y2 = self.canvas.coords(tag)
            return (x1 + x2) // 2, (y1 + y2) // 2
        # ---------------------------------------------------------------------
        x, y = event.x, event.y # Coordonnées cliquées
        tags = self.canvas.gettags(CURRENT) # tags contient le tag "node-B" et "current"
   
        for tag in tags:
            if not tag.startswith("node"):
                continue
            # Ceci est normalement effectué pour un seul tag (par ex "node-B").
            # Comme deux objets ont ce tag, les deux sont déplacés simultanément
            # par self.canvas.move...
            x1, y1 = node_center(tag)
            if "A" in tag:
                self.ptA = ("A",x1,y1)
            if "B" in tag:
                self.ptB = ("B",x1,y1)
            if "C" in tag:
                self.ptC = ("C",x1,y1)
            if "D" in tag:
                self.ptD = ("D",x1,y1)
            self.canvas.move(tag, x-x1, y-y1)
        
        x1, y1 = node_center(tag)
        
        
        # Génération à la volée du polygone de contrôle
        tag = "poly-{}".format("poly")
        self.canvas.delete(tag)
        ligne = self.canvas.create_line(
                        self.ptA[1],self.ptA[2],
                        self.ptB[1],self.ptB[2],
                        self.ptC[1],self.ptC[2],
                        self.ptD[1],self.ptD[2]) 
        self.canvas.addtag_withtag(tag, ligne)
        # Fin de la génération du polygone de contrôle
        
        # Génération à la volée de la courbe de Bezier en utilisant l'algo de Casteljau
        tag = "bez-{}".format("bez")
        self.canvas.delete(tag)
        self.generate_poles()
        ligne = self.canvas.create_line(tkdeCaseljau(self.poles,100)) 
        self.canvas.addtag_withtag(tag, ligne)
        # Fin de la génération en utilisant l'algo de casteljau
        
        # Génération à la volée de la courbe de Bezier en utilisant bezier
        tag = "bern-{}".format("bern")
        self.canvas.delete(tag)
        self.generate_poles()
        ligne = self.canvas.create_line(tkBezier(self.poles,100)) 
        self.canvas.addtag_withtag(tag, ligne)
        # Fin de la génération en utilisant bezier
        
    def creation_points(self):
        pts = [self.ptA,self.ptB,self.ptC,self.ptD]
        
        # Polygone de contrôle
        tag = "poly-{}".format("poly")
        """ligne = self.canvas.create_line(
                        self.ptA[1],self.ptA[2],
                        self.ptB[1],self.ptB[2],
                        self.ptC[1],self.ptC[2],
                        self.ptD[1],self.ptD[2])""" 
        ligne = self.canvas.create_line([self.ptA[1],self.ptA[2],
                        self.ptB[1],self.ptB[2],
                        self.ptC[1],self.ptC[2],
                        self.ptD[1],self.ptD[2]])
        self.canvas.addtag_withtag(tag, ligne)
        
        rayon = 4
        for pt,x,y in pts:
            x1,x2 = x-rayon, x+rayon
            y1,y2 = y-rayon, y+rayon
            point = self.canvas.create_oval(x1,y1,x2,y2, fill="#fe9494", outline="#FF0101")
            
            tag = "node-{}".format(pt)
            # Création des points avec un tag
            self.canvas.addtag_withtag(tag, point)
            
            # Pour créer un événement
            self.canvas.tag_bind(point, '<B1-Motion>', self.move)
            
    def generate_poles(self):
        self.poles=[[self.ptA[1],self.ptA[2]],
                    [self.ptB[1],self.ptB[2]],
                    [self.ptC[1],self.ptC[2]],
                    [self.ptD[1],self.ptD[2]]]
    
 
fenetre = Tk()
fenetre.resizable(width=False, height=False)
interface = main_fen(fenetre)

interface.mainloop()

#interface.destroy()




"""
poles = [[0,0],[0,20],[40,20],[40,0]]
les_u = np.linspace(0,1,100)

les_x_bern = []
les_y_bern = []
for t in les_u:
    pt = calculPointCourbe(poles,t)
    les_x_bern.append(pt[0])
    les_y_bern.append(pt[1])

les_u = np.linspace(0,1,11)
les_x_cast = []
les_y_cast = []

les_u = np.linspace(0,1,100)
poles_x = [e[0] for e in poles]
poles_y = [e[1] for e in poles]
for t in les_u:
    les_x_cast.append(deCasteljau(poles_x,0,3,t))
    les_y_cast.append(deCasteljau(poles_y,0,3,t))


#plt.plot(les_x_bern,les_y_bern,"b.")
#plt.plot(les_x_cast,les_y_cast,"r*")
#plt.axis('equal')
#plt.show()



#print(deCasteljau(poles_x,0,2,0.5))


        
print(horner([3,2,1],0.5))
print(deCasteljau([0,0,40,40],0,3,0.5))
"""