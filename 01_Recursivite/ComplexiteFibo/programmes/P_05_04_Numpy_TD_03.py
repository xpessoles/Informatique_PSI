#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Xavier Pessoles"


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

img = mpimg.imread("PhotoBD.png")


def affichage1(img1):
    """ Affichage d'une seule image"""
    plt.imshow(img1)
    plt.show()


def affichage2(img1,img2):
    """ Affichage de deux images"""
    f, ((ax1, ax2)) = plt.subplots(1, 2, sharex='col', sharey='row')
    ax1.imshow(img1)
    ax2.imshow(img2)
    plt.show()

def affichage3(img1,img2,img3):
    """ Affichage de trois images"""
    f, ((ax1, ax2,ax3)) = plt.subplots(1, 3, sharex='col', sharey='row')
    ax1.imshow(img1)
    ax2.imshow(img2)    
    ax3.imshow(img3)

    plt.show()

    


## Question 1 : affichage de l'image
# plt.imshow(img)
# plt.show()

## Question 2 : 
(h,l,p) = img.shape                 # Taille de l'image
print("Couleur du pixel 200x200 : ",img[300,300,:] )

print("Niveau de rouge mini et maxi : ",img[:,:,0].min(),"et",img[:,:,0].max())
print("Niveau de vert  mini et maxi : ",img[:,:,1].min(),"et",img[:,:,1].max())
print("Niveau de bleu  mini et maxi : ",img[:,:,2].min(),"et",img[:,:,2].max())


## Question 3 : [0,1] -> [0,255] et [0,255] -> [0,1] 
def conv_1_2_255(img):
    """ 
    Conversion des niveaux de couleurs de [0,1] -> [0,255]
     * Entrée :
      - img(numpy.ndarray) : image de shape (h,l,3) 
     * Sortie :
      - img(numpy.ndarray) : image de shape (h,l,3)
    """
    a = 255*img
    a = a.astype(int)
    return a

def conv_255_2_1(img):
    """ 
    Conversion des niveaux de couleurs de [0,1] -> [0,255]
     * Entrée :
      - img(numpy.ndarray) : image de shape (h,l,3) 
     * Sortie :
      - img(numpy.ndarray) : image de shape (h,l,3)
    """
    return (1/255)*img
    
    
## Question 4 : Histogramme des couleurs

def histogramme(img):
    """ Fonction permettant de tracer l'histogramme de chacune des couleurs
     * Entrée :
      - img(numpy.ndarray) : image de shape (h,l,3) (Codes couleurs comprises entre 0 et 1)
    """
 
    img = conv_1_2_255(img)
    histo = [[0 for j in range(256)]for j in range(3)]
    (l,h,p)=img.shape
    for i in range(l):
        for j in range (h):
            for k in range(3) :
                histo[k][img[i,j,k]]+=1
                
    plt.plot(histo[0],"r")
    plt.plot(histo[1],"g")
    plt.plot(histo[2],"b")
    plt.show()
    return histo
# histogramme(img)


## Question 5 Trame des couleurs
imgr=np.zeros(img.shape)
imgr[:,:,0]=img[:,:,0]

imgv=np.zeros(img.shape)
imgv[:,:,1]=img[:,:,1]

imgb=np.zeros(img.shape)
imgb[:,:,2]=img[:,:,2]

#affichage3(imgr,imgv,imgb)


## Question 6 : Images saturées

img_sr = img.copy()
img_sr[:,:,0]=1

img_sv = img.copy()
img_sv[:,:,1]=1

img_sb = img.copy()
img_sb[:,:,2]=1
#affichage3(img_sr,img_sv,img_sb)

## Question 7 : Images inversées

# img[:,:,:]=1-img[:,:,:]
img_inv= 1-img

#affichage2(img,img_inv)


## Question 8 : Transformation en noir et blanc
def convert_nb_moy(img,a,b,c):
    """
    Conversion d'une image en noir et blanc par pondération de chaque niveau de couleur
    """
    imgnb = np.zeros(img.shape)
    imgnb[:,:,0]=(a/(a+b+c)*img[:,:,0]+b/(a+b+c)*img[:,:,1]+c/(a+b+c)*img[:,:,2])#*(1/(a+b+c))
    imgnb[:,:,1]=imgnb[:,:,0]
    imgnb[:,:,2]=imgnb[:,:,0]
    return imgnb

imgnb1 = convert_nb_moy(img,1,1,1)
imgnb2 = convert_nb_moy(img,10,1,1)
imgnb3 = convert_nb_moy(img,1,2,1)
imgnb4 = convert_nb_moy(img,10,5,1)

"""
h1 = histogramme(imgnb1)
h2 = histogramme(imgnb2)
h3 = histogramme(imgnb3)
h4 = histogramme(imgnb4)

plt.plot(h1[0])
plt.plot(h2[0])
plt.plot(h3[0])
plt.plot(h4[0])
"""
#affichage3(img,imgnb1,imgnb2)
#affichage3(img,imgnb3,imgnb4)

## Question 9 : Transformation en noir et blanc

def convert_nb_2(img):
    imgnb = np.zeros(img.shape)
    (h,l,p) = img.shape
    for i in range(h):
        for j in range(l):
            for k in range(p):
                imgnb[i,j,k]=0.5*(max(img[i,j,:])+max(img[i,j,:]))
    return imgnb
        

# affichage2(img,convert_nb_2(img))       
        
## Question 10  tracer des fonctions
les_x = np.linspace(0,1,1000)

def f2(x):
    return 0.5+0.5*math.sin(math.pi*(x-0.5))

vf2 = np.vectorize(f2)

"""
plt.plot(les_x,np.sqrt(les_x))
plt.plot(les_x,vf2(les_x))
plt.show()
"""

## Question 11 tracer des fonctions

def contraste(img,f):
    imgc = np.zeros(img.shape)
    (h,l,p) = img.shape
    for i in range(h):
        for j in range(l):
            for k in range(p):
                imgc[i,j,k]=f(img[i,j,k])
                
    return imgc


imgnb = convert_nb_moy(img,1/3,1/3,1/3)
img1 = contraste(img,math.sqrt)
img2 = contraste(img,f2)

#affichage3(img,img1,img2)       

## Question 12


def convolution(img,M):
    imgc = np.zeros(img.shape)
    (h,l,p) = img.shape
    for i in range(1,h-1):
        for j in range(1,l-1):
            for k in range (p):
                imgc[i,j,k]=np.sum(M*img [i-1:i+2,j-1:j+2,k])
    return imgc
        
img_255 = conv_1_2_255(img)
M1 = [[1/8,1/8,1/8],[1/8,-1/8,1/8],[1/8,1/8,1/8]]
M2 = [[1,1,1],[1,-3,1],[1,1,1]]
img_cv1 = convolution(img_255,M1)
img_cv2 = convolution(img_255,M2)

img_11 = conv_255_2_1(img_cv1)
img_12 = conv_255_2_1(img_cv2)

#M=np.array(M)
affichage3(img,img_11,img_12)
