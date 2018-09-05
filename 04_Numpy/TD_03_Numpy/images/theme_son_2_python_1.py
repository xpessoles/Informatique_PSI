#! /usr/local/bin/python3.4
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile

# (a)
# Pour stocker 10 minutes de musique sur un CD : 
# 2 voies (stéréo), 16 bits, 44100Hz
# donc 10*60*44100*16*2 = 846720000 bits
# soit 105840000 octets
# soit 103359 kO
# soit 100.94 MO

# (b)
for filename in ["seagull.wav", "sea.wav", "horn.wav"]:
    rate, data = scipy.io.wavfile.read(filename)
    print("Pour {} : ".format(filename))
    print("nombre de voies : data.ndim = {} donc le son est mono".format(data.ndim))
    print("fréquence : rate = {} Hz".format(rate))
    print("résolution : data.dtype = {} donc la résolution est 16 bits".format(data.dtype))
    print("durée : {} secondes".format(len(data)/rate))
    print("=====")

# Pour seagull.wav : 
# nombre de voies : data.ndim = 1 donc le son est mono
# fréquence : rate = 22050 Hz
# résolution : data.dtype = int16 donc la résolution est 16 bits
# durée : 12.345714285714285 secondes
# =====
# Pour sea.wav : 
# nombre de voies : data.ndim = 1 donc le son est mono
# fréquence : rate = 22050 Hz
# résolution : data.dtype = int16 donc la résolution est 16 bits
# durée : 37.53356009070295 secondes
# =====
# Pour horn.wav : 
# nombre de voies : data.ndim = 1 donc le son est mono
# fréquence : rate = 22050 Hz
# résolution : data.dtype = int16 donc la résolution est 16 bits
# durée : 1.1014512471655329 secondes
# =====
    
# (c)
def affiche(filename):
    """filename désigne un fichier .wav
    représente graphiquement la première voie du signal sur un graphique"""
    rate, data = scipy.io.wavfile.read(filename)
    # on commence par ne conserver que la première voie si le son est stéréo
    if data.ndim > 1:
        data = data[:,0]
    x = np.arange(len(data))
    y = data
    plt.plot(x,y)
    plt.show()        

# affiche("seagull.wav")    

# On peut aller un peu plus loin, et avoir en abscisse des temps
# et en ordonnées des valeurs entre -1 et 1, en fonction de la résolution

def affiche(filename):
    """filename désigne un fichier .wav
    représente graphiquement la première voie du signal sur un graphique"""
    rate, data = scipy.io.wavfile.read(filename)
    # on commence par ne conserver que la première voie si le son est stéréo
    if data.ndim > 1:
        data = data[:,0]
    duree_du_son = len(data)/rate         # durée du son en secondes
    x = np.arange(0, duree_du_son, 1/rate)# les valeurs de temps,
                                          # espacées de 1/fréquence
    resolution = str(data.dtype)          # on regarde la résolution 
    if resolution[-1:] == "8":            # dans le dtype
        y = data / 2**8
    else:
        y = data / 2**(int(resolution[-2:]))
    plt.figure()
    plt.plot(x,y)
    plt.grid()
    plt.title("Représentation du son de {}".format(filename))
    # plt.show()
    plt.savefig(filename[:-4]+".pdf")

# affiche("seagull.wav")
# $\includegraphics[width=.5\textwidth]{../input_exos_python/theme_son_2_fig_5.pdf}$
# affiche("horn.wav")    
# $\includegraphics[width=.5\textwidth]{../input_exos_python/theme_son_2_fig_6.pdf}$
# affiche("sea.wav")    
    
# (d)
def ajoute_silence (data, rate, duree_ms, debut=True ):
    """ Renvoie un tableau de son mono identique à data
    où un silence de durée duree_ms a été ajout au début (à la fin)"""
    assert data.ndim == 1, "attention, le son proposé n'est pas mono"
    silence = np.zeros(((duree_ms/1000)*rate,), dtype=data.dtype)
    if debut:
        b = np.concatenate((silence, data), axis=0)
    else:
        b = np.concatenate((data, silence), axis=0)
    return b

rate, data = scipy.io.wavfile.read("sea.wav")
silence_sea = ajoute_silence(data, rate, 1000, True)
print("data.dtype = {}".format(silence_sea.dtype))
# data.dtype = int16
print("durée : {} secondes".format(len(silence_sea)/rate))
# durée : 38.53356009070295 secondes

scipy.io.wavfile.write("silence_sea.wav", rate, silence_sea)
# affiche("silence_sea.wav")
# $\includegraphics[width=.5\textwidth]{../input_exos_python/theme_son_2_fig_7.pdf}$
sea_silence = ajoute_silence(data, rate, 1000, False)
scipy.io.wavfile.write("sea_silence.wav", rate, sea_silence)
# affiche("sea_silence.wav")

# (e)
def mono_to_stereo(data, rate, duree_ms = 20):
    """Convertit un son mono en stéréo
    selon la méthode proposée"""
    assert data.ndim == 1, "attention, le son proposé n'est pas mono"
    voie1 = ajoute_silence(data, rate, duree_ms, True)
    voie2 = ajoute_silence(data, rate, duree_ms, False)
    n = len(voie1)
    voie1.shape = (n, 1)
    voie2.shape = (n, 1)
    data_stereo = np.concatenate((voie1, voie2), axis = 1)
    # print("Création d'un tableau de son de shape {}".format(data_stereo.shape))
    return data_stereo

rate, data = scipy.io.wavfile.read("sea.wav")
data_stereo = mono_to_stereo(data, rate)
# Création d'un tableau de son de shape (828056, 2)
scipy.io.wavfile.write("sea_stereo.wav", rate, data_stereo)

# (f)
def mixage(data, sound, rate, time, voie=0):
    """Ajoute à data le son sound à partir de l'instant time en secondes"""
    assert data.ndim == 2, "attention, le son proposé n'est pas stéréo"
    debut = time*rate
    data_mixee = np.copy(data)
    data_mixee[debut:debut+len(sound),voie] += sound
    return data_mixee

# (g)
rate, data = scipy.io.wavfile.read("sea.wav")
_, mouette = scipy.io.wavfile.read("seagull.wav")
_, klaxon = scipy.io.wavfile.read("horn.wav")
data_stereo = mono_to_stereo(data, rate)
data1 = mixage(data_stereo, mouette, rate, 4, 0)
data2 = mixage(data1, mouette, rate, 12, 1)
data3 = mixage(data2, 1.8*klaxon, rate, 20, 0)   # je force un peu le son 
data4 = mixage(data3, 1.8*klaxon, rate, 20, 1)   # de la sirène de bateau

scipy.io.wavfile.write("son_mixe.wav", rate, data4)

# (h)
# D'une part, il faut rééchantillonner le signal.
# Comme les fréquences ne sont pas multiples l'une de l'autre,
# on peut supprimer régulièrement des valeurs, mais la qualité
# sonore est alors très altérée.
# On calcule donc plutôt une moyenne pondérée des valeurs
# encadrant l'instant théorique du rééchantillonnage.
# $\includegraphics[width=\textwidth]{../input_exos_python/theme_son_2_fig_4}$
# Peut-on éviter une boucle ici, je ne pense pas. 

def reechantillonnage(filename, newfilename, newrate):
    """Convertit le fichier filename, échantillonné avec une fréquence donnée
    en le fichier newfilename, échantillonné avec une fréquence newrate"""
    rate, data = scipy.io.wavfile.read(filename)
    newdata = np.zeros( (len(data)*newrate//rate,) , dtype=np.int16)

    for i in range(len(newdata)):
        t = i / newrate
        j = t * rate
        k = np.floor(j)

        newdata[i] =  (j-k)*data[k] + (k+1-j)*data[k+1]

    scipy.io.wavfile.write(newfilename, newrate, newdata)
    return None

reechantillonnage("seagull.wav", "seagull_2.wav", 8000)

# D'autre part, il faut réduire la résolution du signal, pour passer en int8
# Mais attention, en lisant la doc de wavfile.write, on voit qu'il faut
# passer en uint8 et pas en int8

def reduction_resolution(filename, newfilename):
    """Réduit la résolution int16 du son du fichier filename
    en int8, dans le fichier newfilename"""
    rate, data = scipy.io.wavfile.read(filename)
    newdata=(128+(data/2**16)*2**8).astype(np.uint8)
    print(newdata.dtype)
    print(newdata.max(),newdata.min())

    scipy.io.wavfile.write(newfilename, rate, newdata)
    return None

reduction_resolution("seagull_2.wav", "seagull_3.wav")
