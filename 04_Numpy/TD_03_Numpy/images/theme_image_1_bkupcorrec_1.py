#! /usr/local/bin/python3.4
# -*- coding:utf-8 -*-
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm    

img = mpimg.imread('./playmobil.png')  

print(img.shape)
# (564, 1000, 3)
 
print(img.dtype)
# float32

# print(img)

print(img.max())
print(img.min())
# 1.0
# 0.0





playmobil = mpimg.imread('./playmobil.png')  
montagne = mpimg.imread('./montagne.png')  

reference = playmobil[300,300,:]
mask = np.sqrt((playmobil[:,:,0] - reference[0])**2
               +(playmobil[:,:,1] - reference[1])**2
               +(playmobil[:,:,2] - reference[2])**2) < .30
mask.shape = (564, 1000, 1)
masque = np.concatenate((mask, mask, mask), axis=2)
fake = montagne*masque + playmobil*(1-masque)
plt.imshow(fake)
plt.show()


