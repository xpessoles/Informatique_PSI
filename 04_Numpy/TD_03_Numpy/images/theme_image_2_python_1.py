#! /usr/local/bin/python3.4
# -*- coding:utf-8 -*-
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image
import scipy.misc

########################################################
####         insertion d'un message secret
########################################################

# question (a)
img = scipy.misc.imread('./theme_image_2_sagrada_familia.png')

# plt.figure(1)
# plt.imshow(img)
# plt.show()

# question (b)
print(img.shape)
# (640, 480, 3)

print(img.dtype)
# uint8

print(img[300,300,:])
# [127 118 109]

# on voit déjà par le pixel (300,300) que toutes les valeurs ne sont pas paires.

# question (c)
img1 = np.copy(img)
img1 -= (img1 % 2)

print(img1[300,300,:])
# [126 118 108]

# On a construit une copie du tableau img.
# img1 % 2 construit le tableau des restes
# dans la division euclidienne terme à terme par 2 des éléments de img1
# et on retire terme à terme ces valeurs.
# Bref, si la valeur est paire, on la garde
# si elle est impaire, on lui retranche 1 pour la rendre paire.

# plt.figure(2)
# plt.imshow(img1) 
# plt.show()

# Il n'est pas possible de distinguer la différence à l'œil nu
# avec l'image initiale

# question (d)
def codebinaire(c):
    """Pour un caractère, renvoie son code binaire sur 8 bits
    sous la forme d'un tableau numpy de zéros et uns de longueur 8"""
    # conversion du caractère en son code ascii entier
    x = ord(c)                   # formé comme 97 (dans le cas de la lettre 'a')
    # conversion de l'entier en binaire
    y = bin(x)                   # formé comme '0b1100001'
    # suppression des deux premiers caractères
    z = y[2:]                    # formé comme '1100001'
    # ajouts de zéros en début
    t = '0'*(8 - len(z)) + z     # formé comme '01100001'
    
    return np.array([int(b) for b in t])

print(codebinaire('a'))
# [0 1 1 0 0 0 0 1]

message = """Le danger réel n'est pas que les ordinateurs commencent à penser comme les humains,
mais que les humains commencent à penser comme des ordinateurs.
(Sydney Harris)"""

n, p, q = img1.shape
# (640, 480, 3)
img1.shape = (-1, )                       # on aplatit l'image

N = len(message)
for i in range(N):
    img1[8*i:8*(i+1)] += codebinaire(message[i])

img1.shape = (n, p, q)

# plt.figure(3)    
# plt.imshow(img1)  
# plt.show()
# Ici encore, il est impossible de distinguer la différence

scipy.misc.imsave("theme_image_2_sagrada_familia_avec_message.png", img1)

# question (e)
# on peut cacher un bit par élément du tableau, et il faut 8 bits pour coder une lettre
# On peut donc cacher un message de 640*480*3/8 lettres.
print(640*480*3//8)
# 115200 caractères
########################################################
####         décodage d'un message secret
########################################################

# question (f)
img = scipy.misc.imread('./theme_image_2_traboule_avec_message.png')

# plt.figure(4)
# plt.imshow(img)
# plt.show()

# question (g)
print(img.shape)
# (640, 480, 3)

print(img.dtype)
# uint8

print(img[300,300,:])
# [64 54 46]

# question (h)
# commençons par définir une fonction réciproque à codebinaire
def decodebinaire(a):
    """pour un tableau numpy de longueur 8 constitué de zéros et uns,
    renvoie le caractère correspondant au codage ascii
    du nombre écrit en binaire dans a"""
    n = 0
    p = 1
    for i in range(len(a)-1,-1,-1):
        # p est 2^i et n est a[7]*2^0 + a[6]*2^1 + ... + a[i+1]*2^{i+1}
        n += a[i] * p
        p *= 2
    return(chr(n))

print(decodebinaire(np.array([0,1,1,0,0,0,1,0])))
# b

# on aplatit l'image
img.shape=(-1,)
# on ne garde que le reste dans la division euclidienne par 2
img %= 2
# on regroupe les valeurs par 8, et on fait la liste des caractères correspondants

message = ""
for i in range(img.size//8):
    c = decodebinaire(img[8*i: 8*(i+1)])
    message = message + c

print(message)
# Ins[...]oges
# pour connaître cette définition complète, il faut découvrir le message ! 

# question (i)

# Avantages :
# codage et décodage très faciles à mettre en œuvre.
# altération minime de l'image
# on peut cacher un message assez long dans une image relativement petite
# il est quasi indécelable qu'un message est caché dans l'image
# (quitte à rallonger le message, avec, par exemple, du lorem ipsum de façon
# à ce que les bits de poids faible soient uniformément des 0 et des 1)

# Inconvénients :
# ce codage ne supporte aucune manipulation de l'image :
# pas de compression avec perte de l'image,
# pas de redimensionnement,
# pas de traitement des couleurs.
# pas d'impression suivi d'un numérisation. 
