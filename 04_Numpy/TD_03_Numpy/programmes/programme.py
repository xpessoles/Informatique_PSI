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
img=1-img

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


plt.imshow(img)
plt.show()