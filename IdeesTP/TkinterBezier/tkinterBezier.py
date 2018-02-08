#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import math as m

def nouvelle_fenetre(ti,ht_fen,la_fen):
    global main_fen
    global ht_fen
    global la_fen
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
    
def convert_coord(x,y):
    """
    Retourne les coordonnées d'un point dans le système de coordonnées de tkinter.
    """
    # A MODIFIER
    return (x,y)

nouvelle_fenetre("Titre",100,100*m.sqrt(2))

# Démarrage de la boucle tkitnter
main_fen.mainloop()