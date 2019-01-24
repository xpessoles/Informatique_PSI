## Corrige modelisation physique CCP PC 2015
##
## Resolution numerique de l'equation de la chaleur
##
#####################################################

## Importation des modules
###########################

import numpy as np
import matplotlib.pyplot as plt

## Definition des fonctions
############################

def schema_explicite(T0, ItMax, Dt, N, e = 40e-2, Lambda = 1.65, Rho = 2150, \
                     c = 1000, T_int = 293, T_ext = 263, epsilon = 1e-2):
    '''renvoie le nombre d'iterations effectuees et une matrice de N lignes
contenant les temperatures a l'instant k en chaque point declare de la paroi,
par la methode des differences finies en utilisant un schema explicite.'''
    Alpha = Rho * c / Lambda
    Dx = e / (N + 1)
    r = Dt / (Alpha * pow(Dx, 2))

    if r >= 0.5 :
        raise Exception('''r = Dt / ( (rho * c / lambda) * Dx^2 ) doit etre
inferieur à 0.5.''')

    T_tous_k = np.zeros((N, ItMax))

    for i in range(N):
        T_tous_k[i, 0] = T0[i, 0]

    T_tous_k[0, 1] = r * T_int + (1 - 2 * r) * T_tous_k[0, 0] + \
                     r * T_tous_k[1, 0]
    for indice in range(1, N - 1):
        T_tous_k[indice, 1] = r * T_tous_k[indice - 1, 0] + \
                              (1 - 2 * r) * T_tous_k[indice, 0] + \
                              r * T_tous_k[indice + 1, 0]
    T_tous_k[N - 1, 1] = r * T_tous_k[N - 2, 0] + \
                         (1 - 2 * r) * T_tous_k[N - 1, 0] + \
                         r * T_ext

    k = 2
    condition = True

    while condition and k < ItMax - 1 :
        T_tous_k[0, k] = r * T_int + (1 - 2 * r) * T_tous_k[0, k - 1] + \
                     r * T_tous_k[1, k - 1]
        for indice in range(1, N - 1):
            T_tous_k[indice, k] = r * T_tous_k[indice - 1, k - 1] + \
                                  (1 - 2 * r) * T_tous_k[indice, k - 1] + \
                                  r * T_tous_k[indice + 1, k - 1]
        T_tous_k[N - 1, k] = r * T_tous_k[N - 2, k - 1] + \
                             (1 - 2 * r) * T_tous_k[N - 1, k - 1] + \
                             r * T_ext
        if calc_norme(T_tous_k[:, k] - T_tous_k[:, k - 1]) < epsilon :
            condition = False
        k += 1

    return (k - 1, T_tous_k)
        

def calc_norme(V):
    '''renvoie la norme 2 du vecteur V de type array. La norme 2 vaut
sqr ( somme (i de 1 a N) Vi^2 ).'''
    return( pow( sum( [pow(vi, 2) for vi in V] ), 0.5 ) )

def CalcTkp1 (M, d) :
    '''renvoie le vecteur u tel que M.u = d selon l'algorithme de Thomas.
M est une matrice tridiagonale de type array,
d est un vecteur colonne de type array.
Le vecteur u renvoye est aussi un vecteur colonne de type array.'''
    N = len(d)   # Nombre de lignes de d, donc sa dimension
    cprime = np.zeros(N - 1)
    cprime[0] = M[0, 1] / M[0,0]   # Attention c'1 = cprime[0]
    for i in range(1, N - 1):   # coherence avec les i - 1 du sujet
        cprime[i] = M[i, i + 1] / (M[i, i] - \
                                     M[i, i - 1] * cprime[i - 1])
    dprime = np.zeros(N)
    dprime[0] = d[0, 0] / M[0,0]   # Attention d'1 = dprime[0]
    for i in range(1, N):
        dprime[i] = (d[i, 0] - M[i, i - 1] * dprime[i - 1]) / \
                        (M[i, i] - M[i, i - 1] * cprime[i - 1])

    u = np.zeros((N, 1))    # u est un vecteur ligne avec u1 = u[0]
    u[N - 1, 0] = dprime[N - 1] # le rang N - 1 correspond au rang N du sujet
    for i in range(N - 2, - 1, -1):   # decroissance de i
        u[i, 0] = dprime[i] - cprime[i] * u[i + 1, 0]

    return (u)


def schema_implicite(T0, ItMax, Dt, N, e = 40e-2, Lambda = 1.65, Rho = 2150, \
                     c = 1000, T_int = 293, T_ext = 263, epsilon = 1e-2):
    '''renvoie le nombre d'iterations effectuees et une matrice de N lignes
contenant les temperatures a l'instant k en chaque point declare de la paroi,
par la methode des differences finies en utilisant un schema implicite.'''
    Alpha = Rho * c / Lambda
    Dx = e / (N + 1)
    r = Dt / (Alpha * pow(Dx, 2))

    if r >= 0.5 :
        raise Exception('''r = Dt / ( (rho * c / lambda) * Dx^2 ) doit etre
inferieur à 0.5.''')

    T_tous_k = np.zeros((N, ItMax))

    for i in range(N):
        T_tous_k[i, 0] = T0[i, 0]

    # Definition de M
    M = np.zeros((N, N))

    M[0, 0], M[0, 1] = 1. + 2. * r, -r
    for ligne in range(1, N - 1) :
        M[ligne, ligne - 1], M[ligne, ligne], M[ligne, ligne + 1] = \
                 -r, 1. + 2. * r, -r
    M[-1, -2], M[-1, -1] = -r, 1. + 2. * r

    # Definition de v
    v = np.zeros((N, 1))

    v[0, 0], v[-1, 0] = T_int, T_ext

    # Calcul de T^1
    d = T0 + r * v
    res = CalcTkp1(M, d)
    for i in range(N):
        T_tous_k[i, 1] = res[i]

    # Calcul des T^k
    k = 2
    condition = True

    while condition and k < ItMax - 1 :
        D = np.zeros((N, 1))
        for i in range(N):
            D[i] = T_tous_k[i, k - 1] + r * v[i]
        res = CalcTkp1(M, D)
        for i in range(N):
            T_tous_k[i, k] = res[i]
        
        if calc_norme(T_tous_k[:, k] - T_tous_k[:, k - 1]) < epsilon :
            condition = False
        k += 1

    return (k - 1, T_tous_k)

## Definition des constantes
#############################

ItMax = 2000

epais = 40e-2
conduc = 1.65
rho = 2150
Cp = 1000
Tint = 293
Text1 = 283
Text2 = 263
epsilon = 1e-2
N = 60
Dt = 25

a = (Text1 - Tint) / epais
b = Tint

Dx = epais / (N + 1)
x = np.arange(Dx, epais - Dx / 2, Dx)

T0 = np.zeros((N, 1))
for i in range(N):
    T0[i, 0] = a * x[i] + b

alpha = rho * Cp / conduc
r = Dt / (alpha * pow(Dx, 2))


## Test des fonctions
######################

M = np.array([[1, 4, 0, 0, 0], \
              [1, -1, 1, 0, 0], \
              [0, -1, 1, 1, 0], \
              [0, 0, 2, 1, 0], \
              [0, 0, 0, -1, 4]])

D = np.array([[1], [3], [3], [5], [-5]])



## Programme principal
#######################

fonctions = [schema_implicite, schema_explicite]

ind_fcts = int(input('''Choix du schema numerique :
0 : schema implicite
1 : schema explicite
'''))

nbIter, T = fonctions[ind_fcts](T0, ItMax, Dt, N, epais, conduc, rho, \
                                Cp, Tint, Text2, 1e-2)
for i in range(0, nbIter, 100):
    plt.plot(x, T[:, i])

plt.title(str(fonctions[ind_fcts])[9:26])

plt.show()

print('La durée au bout duquel le régime permanent est établi est de', \
      Dt * nbIter / 3600, 'heures')


## Figure de la page d'accueil
###############################

plt.figure("Résolution numérique de l'équation de la chaleur", \
           figsize = (12, 5))

plt.subplot(1, 2, 1)
nbIter, T = fonctions[0](T0, ItMax, Dt, N, epais, conduc, rho, \
                                Cp, Tint, Text2, 1e-2)
for i in range(0, nbIter, 100):
    plt.plot(x, T[:, i])

plt.title('schéma implicite')

plt.subplot(1, 2, 2)
nbIter, T = fonctions[1](T0, ItMax, Dt, N, epais, conduc, rho, \
                                Cp, Tint, Text2, 1e-2)
for i in range(0, nbIter, 100):
    plt.plot(x, T[:, i])

plt.title('schéma explicite')

plt.savefig('Figure_page_accueil')
