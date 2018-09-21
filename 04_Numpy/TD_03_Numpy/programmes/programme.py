#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

img = mpimg.imread("PhotoBD.png")

def affichage1(img1):
    imshow(img1)
    plt.show()


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
        

M=[[1/8,1/8,1/8],[1/8,1/8,1/8],[1/8,1/8,1/8]]
M=[[1,1,1],[1,8,1],[1,1,1]]
#M=np.array(M)
#affichage2(img,convolution(img,M))

### Histogramme

def hist_nb(img):
    """ Fonction convertissant une image en noir et blanc, puis traçant son histogramme de couleurs"""
    imgnb1 = convert_nb(img,1/3,1/3,1/3)
    img_histo = np.floor(255*imgnb1[:,:,1])

    #histo=256*[0]
    #(l,h)=img_histo.shape
    #for i in range(l):
    #    for j in range (h):
    #        a = int(img_histo[i,j])
    #        histo[a]+=1
    
    histo=[]
    (l,h)=img_histo.shape
    for i in range(l):
        for j in range (h):
            histo.append(img_histo[i,j])
    
    
    plt.hist(img_histo)
    plt.show()

### Image en noir et blanc

#def gristonb(img):
img_gris1 = convert_nb(img,1/3,1/3,1/3)
img_gris1[0:100,0:100,:]=0
img_gris = convert_nb(img,1/3,1/3,1/3)
#img_noir = img_gris<0.5
#img_bl = img_gris>0.5
img_nb=img_noir+img_bl
(l,h,p)=img_gris.shape
img_nb=np.zeros(img_gris.shape)
img_nb_2=np.zeros(img_gris.shape)

"""for i in range(l):
    for j in range (h):
        if img_gris[i,j,0]<0.5:
            img_nb[i,j,:]=0
        else :
            img_nb[i,j,:]=1
"""
for i in range(l-1):
    for j in range (h-1):
        img_nb_2[i,j,:]=1
        delta = img_gris[i,j,0]-0.5
        img_gris[i,j+1,:]=img_gris[i,j,:]+delta/2
        img_gris[i+1,j,:]=img_gris[i,j,:]+delta/4
        img_gris[i+1,j+1,:]=img_gris[i,j,:]+delta/4
        
        
 
plt.imshow(img_gris)
plt.show()       

#affichage3(img_gris1,img_nb,img_nb_2)
"""
plt.imshow(convert_nb_2(img))
plt.show()
"""