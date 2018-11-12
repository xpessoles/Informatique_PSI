#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

img = mpimg.imread("PhotoBD.png")

def affichage2(img1,img2):
    f, ((ax1, ax2)) = plt.subplots(1, 2, sharex='col', sharey='row')
    ax1.imshow(img1)
    ax2.imshow(img2)
    ax1.axis("equal")
    ax2.axis("equal")
    plt.show()

def affichage3(img1,img2,img3):
    f, ((ax1, ax2,ax3)) = plt.subplots(1, 3, sharex='col', sharey='row')
    ax1.imshow(img1)
    ax2.imshow(img2)    
    ax3.imshow(img3)

    ax1.axis("equal")
    ax2.axis("equal")
    plt.show()

    

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
imgnb3 = convert_nb(img,1,2,1)
imgnb4 = convert_nb(img,10,5,1)

def convert_nb_2(img):
    imgnb = np.zeros(img.shape)
    (h,l,p) = img.shape
    for i in range(h):
        for j in range(l):
            for k in range(p):
                imgnb[i,j,k]=0.5*(max(img[i,j,:])+max(img[i,j,:]))
    return imgnb
        
def contraste(img,f):
    imgc = np.zeros(img.shape)
    (h,l,p) = img.shape
    for i in range(h):
        for j in range(l):
            for k in range(p):
                imgc[i,j,k]=f(img[i,j,k])
                
    return imgc

def f2(x):
    return 0.5+0.5*math.sin(math.pi*(x-0.5))
"""
imgnb = convert_nb(img,1/3,1/3,1/3)
img1 = contraste(img,math.sqrt)
img2 = contraste(img,f2)
"""

def convolution(img,M):
    imgc = np.zeros(img.shape)
    (h,l,p) = img.shape
    for i in range(1,h-1):
        for j in range(1,l-1):
                imgc[i,j]=np.sum(M*img [i-1:i+2,j-1:j+2])
    return imgc
        

M=[[1/8,1/8,1/8],[1/8,0,1/8],[1/8,1/8,1/8]]
M=[[1,1,1],[1,-8,1],[1,1,1]]
M=(1/16)*np.array(M)
affichage2(img,convolution(img,M))


"""
plt.imshow(convert_nb_2(img))
plt.show()
"""