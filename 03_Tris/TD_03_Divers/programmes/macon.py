#!/usr/bin/env python
# -*- coding: utf-8 -*-

def compteRangee(toutesLesCombinaisonsLigne,r,hauteur):
    if hauteur==1:
        return(1)
    else:
        nbCombi=len(toutesLesCombinaisonsLigne)
        somme=0
        i=0
        while i<nbCombi:
            if sontCompatibles(r,toutesLesCombinaisonsLigne[i]):
                somme+=compteRangee(toutesLesCombinaisonsLigne,toutesLesCombinaisonsLigne[i],hauteur-1)
            i+=1
        return(somme)