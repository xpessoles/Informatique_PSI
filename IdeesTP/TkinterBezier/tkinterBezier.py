#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import math as m

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
        tags = self.canvas.gettags(tk.CURRENT) # tags contient le tag "node-B" et "current"
   
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
        
        tag = "poly-{}".format("poly")
        self.canvas.delete(tag)
        
        ligne = self.canvas.create_line(
                        self.ptA[1],self.ptA[2],
                        self.ptB[1],self.ptB[2],
                        self.ptC[1],self.ptC[2],
                        self.ptD[1],self.ptD[2]) 
        self.canvas.addtag_withtag(tag, ligne)
        
        
        
           
        
    def creation_points(self):
        pts = [self.ptA,self.ptB,self.ptC,self.ptD]
        
        # Polygone de contrôle
        tag = "poly-{}".format("poly")
        ligne = self.canvas.create_line(
                        self.ptA[1],self.ptA[2],
                        self.ptB[1],self.ptB[2],
                        self.ptC[1],self.ptC[2],
                        self.ptD[1],self.ptD[2]) 
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
        
            
    
 
fenetre = Tk()
fenetre.resizable(width=False, height=False)
interface = main_fen(fenetre)

interface.mainloop()

#interface.destroy()

