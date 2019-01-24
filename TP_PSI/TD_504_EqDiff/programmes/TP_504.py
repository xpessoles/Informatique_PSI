import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# On définit les constantes physiques 
# ====================================
e = 0.40                # m
Tint = 20 + 273.15      # Kelvin
Text1 = 10 + 273.15     # Kelvin
Text2 = -10 + 273.15    # Kelvin
cp = 1000               # J kg-1 K-1
lambd = 1.65            # W m-1 K-1
rho = 2150              # kg m-3


# Paramètres de la simulation
Tps_simu = 30000      # Temps de simulation (s)
Nech_tps = 100000        # Nombre d'échantillons (en temps)
Nech_e = 60             # Nombre d'échantillons (en espace)
ItMax_k = 2000          # ??
dt = Tps_simu/(Nech_tps+1)  #25 # pas de temps s# ??
dx = e / (Nech_e +1)    # ?? 

N=Nech_e
alpha = rho*cp/lambd
r = dt/(alpha *dx**2)


def matrice_M(N_ech_e,r):
    M=np.zeros((N_ech_e+1,N_ech_e+1))
    for i in range(1,N_ech_e):
        M[i][i]=1-2*r
        M[i][i+1]=r
        M[i][i-1]=r
    M[0][0]=1-2*r
    M[N_ech_e][N_ech_e]=1-2*r
    M[0][1]=r
    M[N_ech_e][N_ech_e-1]=r
    return M

def matrice_T0(Ti,Tf,Nech_e):
    tt =  np.zeros((Nech_e+1,1))
    for i in range(Nech_e+1):
        tt[i] = ((Tf-Ti)/(Nech_e))*i+Ti
    return tt


def matrice_V(Ti,Tf,Nech_e):
    tt =  np.zeros((Nech_e+1,1))
    for i in range(Nech_e+1):
        tt[i] = ((Tf-Ti)/(Nech_e))*i+Ti
    return tt
    
def euler_explicite(M,T0,V,Nech_tps,r):
    dt = Tps_simu/(Nech_tps+1)
    les_T=[T0]
    for i in range (Nech_tps):
        les_T.append(np.dot(M,les_T[-1])+r*V)
        
        
    return les_T

M = matrice_M(Nech_e,r)
T0 = matrice_T0(Tint,Text1,Nech_e)
V = matrice_V(Text1,Text2,Nech_e)
les_T = euler_explicite(M,T0,V,Nech_tps,r)

les_x = np.linspace(0,e,Nech_e+1)
    
for i in range(0,len(les_T),1000):
    plt.plot(les_x,les_T[i])
plt.show()










def calc_norme(v):
    res = 0
    for i in range(len(v)):
        res = res+v[i]**2
    return sqrt(res)        


def T0(Ti,Tf,N):
    tt =  np.zeros((N,1))
    for i in range(N):
        tt[i] = ((Tf-Ti)/(N-1))*i+Ti
    return tt



"""
t0 = T0(Tint,Text1,N)    


M = np.zeros((N,N))
M[0][0]=1-2*r
M[0][1]=r

M[N-1][N-1]=1-2*r
M[N-1][N-2]=r
for i in range(1,N-1):
    M[i][i]=1-2*r
    M[i][i+1]=r
    M[i][i-1]=r

V = np.zeros((N,1))
V[0][0]=Tint
V[N-1][0]=Text2

T_tous_k = []
T_tous_k.append(t0)

#print(M,T_tous_k[0],r,V)

Tk =  np.dot(M,t0)+r*V
T_tous_k.append(Tk)


while calc_norme(T_tous_k[-1]-T_tous_k[-2])>0.00001 and len(T_tous_k)<ItMax_k:
#while len(T_tous_k)<ItMax_k:
#for i in range(3):
    T_tous_k.append(np.dot(M,T_tous_k[-1])+r*V)

x = [i*(e/(Nech_e-1)) for i in range(Nech_e)]
for i in range(len(T_tous_k)):
    if i%2 == 0 :
        
        plt.plot(x,T_tous_k[i],label = str(i*dt))


x = [i*(e/(Nech_e-1)) for i in range(Nech_e)]
t0 = T0(Tint,Text1,N)    
tf = T0(Tint,Text2,N)    
plt.plot(x,t0)
plt.plot(x,tf)
#plt.plot(x,Tk)
plt.legend()
plt.show()
print(len(T_tous_k)*dt/3600)

"""