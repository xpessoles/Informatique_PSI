#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange


# Question 1
def random_list(n,k):
    """
    Construction d'une liste de n entiers tirés au hasard dans l'intervalle range(k)
    Entrée : 
     * n,k : int
    Sortie :
     * list
    """
    return [randrange(k) for i in range(n)]
    
# Test de la fonction
l = random_list(10,4)


# Question 2
def counting_sort(k,t):
    """
    Fonction permettant de retourner une copie de la liste triée dans un tableau
    Entrée : 
     * k : int
     * t : liste d'entiers appartenant à range(k)
    Sortie :
     * res: list
    """
    u=k*[0]
    for el in t :
        u[el]+=1
    
    res=[]
    for i in range(k):
        res=res+u[i]*[i]
    return res
    
# Test de la fonction
l = [3, 2, 0, 2, 2, 1, 3, 3, 3, 1]
ll =  counting_sort(4,l)
print(l)
print(ll)


# Question 3
def f(k):
    if k==0:
        return 0
    else :
        return k-1

def bucket_sort(f,k,t):
    tt = [f(x) for x in t]
    return tt

l = [3, 2, 0, 2, 2, 1, 3, 3, 3, 1]
ll =  bucket_sort(f,4,l)
print(l)
print(ll)
    

# Question 4
def radix_sort (k,t) :
    """ Retourne une copie de t triée par ordre croissant. t doit contenir des entiers appartenant à range (k**2)"""
    def lp(x):
        return x // k
    def rp(x) :
        return x % k
    u = bucket_sort(rp,k,t)
    r = bucket_sort(lp,k,u)
    return
