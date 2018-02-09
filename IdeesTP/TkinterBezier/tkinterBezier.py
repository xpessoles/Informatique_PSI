#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import math as m

def nouvelle_fenetre(ti):
    global main_fen
    global ht_fen
    global la_fen
    global dessin
    """
    Creation d'une nouvelle fenetre.
    Entrées : 
     * ti(str) : titre de la fenêtre
     * ht(int) : hauteur de la fenêtre (mm)
     * la(int) : largeur de la fenêtre (mm)
    """
    
    # Création de la fenêtre principale
    main_fen = tk.Tk()
    
    # Titre de la fenêtre
    main_fen.title(ti)
    
    # Taille de fenêtre non modifiable
    main_fen.resizable(width=False, height=False)
    
    # Ajout d'une zone de dessin en mm.
    #dessin = tk.Canvas(width = str(la+"m"), height = str(ht+"m"), bg="e8e8e8")
    dessin = tk.Canvas(width = str(la_fen)+"m", height = str(ht_fen)+"m", bg="#e8e8e8")
    dessin.pack()
    
    

ht_fen=100
la_fen=m.sqrt(2)*ht_fen
nouvelle_fenetre("Titre")

def tracer_point(x,y):
    """
    Tracer un point de coordonnées (x,y) (en mm).
    Entrée : 
     * x,y(flt) 
     
    """
    global dessin,ht_fen,la_fen
    rayon = 2 #en mm
    x1,x2 = str(x-rayon)+"m", str(x+rayon)+"m"
    y=-y+ht_fen # Changement de repère (vers le reper tkinter)
    y1,y2 = str(y-rayon)+"m", str(y+rayon)+"m"
    dessin.create_oval(x1,y1,x2,y2, fill="red", width=0)

tracer_point(10,10)



# Démarrage de la boucle tkitnter
main_fen.mainloop()