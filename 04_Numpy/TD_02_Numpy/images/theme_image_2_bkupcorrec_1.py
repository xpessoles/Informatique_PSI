#! /usr/local/bin/python3.4
# -*- coding:utf-8 -*-
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image
import matplotlib.cm as cm
import scipy.misc
import os


img = scipy.misc.imread('./sagrada_familia.png')  
print(img.shape)
# (640, 480, 3)

print(img.dtype)
# uint8

img1 = np.copy(img)
# quitte à retirer 1, on fait en sorte que toutes les valeurs soient paires.
print(img1)
img1 -= (img1 % 2)
print(img1)
# plt.imshow(img1)  # impossible de distinguer la différence
# plt.show()

message = """Le danger réel n'est pas que les ordinateurs commencent à penser comme les humains, mais que les humains commencent à penser comme des ordinateurs.
(Sydney Harris)"""


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

img2 = np.copy(img1)

n, p, q = img2.shape
# (640, 480, 3)
img2.shape = (-1, )                       # on applatit l'image

N = len(message)
for i in range(N):
    img2[8*i:8*(i+1)] += codebinaire(message[i])

img2.shape = (n, p, q)
    
# plt.imshow(img2)  # impossible de distinguer la différence
# plt.show()
scipy.misc.imsave("sagrada_familia_avec_message.png", img2)




img = scipy.misc.imread('./traboule.png')  
print(img.shape)
# (640, 480, 3)

print(img.dtype)
# uint8

img1 = np.copy(img)
# quitte à retirer 1, on fait en sorte que toutes les valeurs soient paires.
print(img1)
img1 -= (img1 % 2)
print(img1)
# plt.imshow(img1)  # impossible de distinguer la différence
# plt.show()


message = """Insecte n, m. , du latin insectus, sous le tabouret. Ainsi le mot insecte désigne-t-il un animal si petit qu'il peut (à l'aise) passer sous un tabouret sans ramper, alors que le python, si. Les insectes sont des invertébrés de l'embranchement des articulés. Il n'y a pas de quoi se vanter. Leur corps, généralement peu sensible à la caresse, est entouré d'une peau à chitine d'aspect volontiers dégueulasse. Il se compose de trois parties : 1. La tête, avec deux antennes que l'enfant aime à couper au ciseau pour tromper son ennui à la fin des vacances, deux gros yeux composés à facettes et peu expressifs au-delà du raisonnable, et une bouche très dure garnie d'un faisceau redoutable de sécateurs baveux dont la vue n'appelle pas le baiser. 2. Le thorax, lisse et brillant, affublé d'un nombre invraisemblable de pattes et le plus souvent garni de deux paires d'ailes dont la finesse des nervures ne manque pas de surprendre, chez un être aussi fruste. C'est grâce à ses ailes que l'insecte peut vombrir, signalant ainsi sa présence au creux de l'oreille interne de l'employé de banque assoupi. 3. L'abdomen, divisé en gros anneaux mous et veloutés et percé sur les côtés de maints trous faisant également office de trachées pulmonaires. ( Ce qui est étrange, chez la libellule, c'est qu'elle respire par où elle pète, MAURICE GENEVOIX, HUMUS. ) Il existe plusieurs millions d'espèces d'insectes. Certains vivent en Seine-et-Marne, au Kenya, ou sur un grand pied, tel le cafard landais qui, comme le berger du même nom, vit juché sur des échasses pour dominer fièrement les ordures ménagères dont il est friand. Certains insectes, comme la mouche des plafonds, possèdent des ventouses sous les pattes qui leur permettent de se coller aux ptères.
Dictionnaire superflu à l'usage de l'élite et des bien nantis de Pierre Desproges
"""

# ascii = [ord(c) for c in message]
# print(max(ascii))
# # 249

def codebinaire(c):
    """pour un caractère, renvoie son code binaire sur 8 bits
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

img2 = np.copy(img1)

n, p, q = img2.shape
# (640, 480, 3)
img2.shape = (-1, )                       # on applatit l'image

N = len(message)
shift = 64                                # pour que le message ne commence pas
                                          # tout de suite dans l'image.
for i in range(N):
    img2[shift+8*i:shift+8*(i+1)] += codebinaire(message[i])

img2.shape = (n, p, q)
    
# plt.imshow(img2)  # impossible de distinguer la différence
# plt.show()
scipy.misc.imsave("traboule_avec_message.png", img2)


img = scipy.misc.imread('./traboule_avec_message.png')
# on aplatit l'image
img.shape=(-1,)
# on ne garde que le reste dans la division euclidienne par 2
img %= 2
# on regroupe les valeurs par 8, et on fait la liste des caractères correspondants

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

message = ""
for i in range(img.size//8):
    c = decodebinaire(img[8*i: 8*(i+1)])
    message = message + c

print(message)


