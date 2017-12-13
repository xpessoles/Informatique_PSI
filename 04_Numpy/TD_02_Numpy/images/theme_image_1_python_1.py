#! /usr/local/bin/python3.4
# -*- coding:utf-8 -*-
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# question (a)
img = mpimg.imread('./theme_image_1_playmobil.png')  

# plt.figure(1)
# plt.imshow(img)
# plt.show()

# question (b)

print(img.shape)
# (564, 1000, 3)
# il y a 564 pixels en hauteur et 1000 en largeur,
# et 3 composantes couleur pour chaque pixel.
 
print(img.dtype)
# float32

print(img[300,300,:])
# [ 0.11764706  0.24705882  0.41568628]

print(img.max())
print(img.min())
# 1.0
# 0.0

# question (c)
# En observant l'image, quitte à zoomer, on voit que le fond n'est pas uniforme.
# Pour répondre précisément à la question, dénombrons les valeurs différentes
# dans la zone en haut à gauche (strictement) du pixel (300,300)
zone = img[0:300,0:300,:]
# couleurs = []
# for i in range(300):
#     for j in range(300):
#         if list(zone[i,j,:]) not in couleurs:
#             couleurs.append(list(zone[i,j,:]))
# print(len(couleurs))
# 3734
# Il y a 3734 couleurs différentes sur les 90 000 pixels considérés.
# Le fond n'est donc clairement pas uniforme,
# même si, à l'œil, il peut sembler uniforme.

# question (d)

playmobil = mpimg.imread('./theme_image_1_playmobil.png')  
montagne = mpimg.imread('./theme_image_1_montagne.png')

# on choisit un pixel bleu de référence
reference_bleue = playmobil[300,300,:]

# pour décider de la valeur du seuil, correspondant à une distance "faible",
# on fait des essais. 
seuil = .30

# Une première version sans utiliser toutes les fonctionnalités de numpy

# les pixels qui ont une couleur proche du pixel de référence sont remplacés
# par les pixels de montagne correspondants
# les autres pixels (qui correspondent donc aux playmobils) ne sont pas modifiés
n,p,q = img2.shape
for i in range(n):
    for j in range(p):
        if np.sqrt((playmobil[i,j,0]-pixel_ref[0])**2 + (playmobil[i,j,1]-pixel_ref[1])**2
                   + (playmobil[i,j,2]-pixel_ref[2])**2)< seuil :
            playmobil[i,j,:] = img1[i,j,:]

# plt.figure()
# plt.imshow(playmobil)
# plt.show()

# Une deuxième version en utilisant les opérations terme à terme de numpy

# on sélectionne les pixels à une distance inférieure au seuil
# en utilisant un masque
mask = np.sqrt( (playmobil[:,:,0] - reference_bleue[0])**2
               +(playmobil[:,:,1] - reference_bleue[1])**2
               +(playmobil[:,:,2] - reference_bleue[2])**2) < seuil
print(mask.shape)
# (564, 1000)
mask.shape = (564, 1000, 1)
masque_complet = np.concatenate((mask, mask, mask), axis=2)

playmobil_sans_bleu = playmobil * (1 - masque_complet)
# plt.figure(2)
# plt.imshow(playmobil_sans_bleu)
# plt.show()

montagne_decoupee = montagne * masque_complet
# plt.figure(3)
# plt.imshow(montagne_decoupee)
# plt.show()

images_superposees = playmobil_sans_bleu + montagne_decoupee
# plt.figure(4)
# plt.imshow(images_superposees)
# plt.show()

# question (e)
mpimg.imsave("theme_image_1_fake.png", images_superposees)


