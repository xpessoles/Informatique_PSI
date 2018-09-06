#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("PhotoBD.png")

# Affichage de l'image
# plt.imshow(img)
# plt.show()

(h,l,p) = img.shape

# Saturation en bleu : 
#img[:,:,2]=1


# Inversion des couleurs
# img[:,:,:]=1-img[:,:,:]
# img=1-img

"""for i in range(h):
    for j in range(l):
        img[i,j,0]=1-img[i,j,0]
        img[i,j,1]=1-img[i,j,1]
        img[i,j,2]=1-img[i,j,2]
"""

# Séparation des couleurs
imgr=np.zeros(img.shape)
imgr[:,:,0]=img[:,:,0]

imgv=np.zeros(img.shape)
imgv[:,:,1]=img[:,:,1]

imgb=np.zeros(img.shape)
imgb[:,:,2]=img[:,:,2]

"""
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
ax1.imshow(img)
ax2.imshow(imgr)
ax3.imshow(imgv)
ax4.imshow(imgb)
plt.show()
"""

# Transformation en noir et blanc
def convert_nb(img,a,b,c):
    imgnb = np.zeros(img.shape)
    imgnb[:,:,0]=(a*img[:,:,0]+b*img[:,:,1]+c*img[:,:,2])#*(1/(a+b+c))
    imgnb[:,:,1]=imgnb[:,:,0]
    imgnb[:,:,2]=imgnb[:,:,0]
    return imgnb

imgnb1 = convert_nb(img,1/3,1/3,1/3)
imgnb2 = convert_nb(img,.21,.71,.07)
imgnb3 = convert_nb(img,100,50,1)
imgnb4 = convert_nb(img,1000,100,1)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
ax1.imshow(imgnb1)
ax2.imshow(imgnb2)
ax3.imshow(imgnb3)
ax4.imshow(imgnb4)
plt.show()


"""
plt.imshow(imgnb)
plt.show()
"""