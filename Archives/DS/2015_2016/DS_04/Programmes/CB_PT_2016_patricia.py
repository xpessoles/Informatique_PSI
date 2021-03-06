### DS4 PT concours blanc epreuve CCP-PC transferts thermiques
# temperature en Kevin T(°C)+273,15
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(3000)

### définitions des constantes
N=100

alpha=2150*1000/1.65
delta_t=10 #toutes les 10s pour un pas de temps plus grand le résultat diverge
delta_x=0.4/(N+1)
r=delta_t/(alpha*(delta_x**2))

T_0=np.zeros((N+2,1))
Text1=10+273.15
Tint=20+273.15
for i in range(N+2):
    T_0[i,0]=((Text1-Tint)*i/(N+1)+Tint)


### définitions des matrices pour euler explicite
V=np.zeros((N+2,1))
V[0,0]=20+273.15
V[N+1,0]=-10+273.15
M=np.zeros((N+2,N+2))
M[0,0]=1-2*r
M[0,1]=r
for i in range(1,N+1):
    M[i,i]=1-2*r
    M[i,i-1]=r
    M[i,i+1]=r
M[N+1,N+1]=1-2*r
M[N+1,N]=r

# print (M)
# [[-0.9571686  0.9785843  0.        ...,  0.         0.         0.       ]
#  [ 0.9785843 -0.9571686  0.9785843 ...,  0.         0.         0.       ]
#  [ 0.         0.9785843 -0.9571686 ...,  0.         0.         0.       ]
#  ..., 
#  [ 0.         0.         0.        ..., -0.9571686  0.9785843  0.       ]
#  [ 0.         0.         0.        ...,  0.9785843 -0.9571686  0.9785843]
#  [ 0.         0.         0.        ...,  0.         0.9785843 -0.9571686]]


# print (M)
# [[ 0.90214157  0.04892922  0.         ...,  0.          0.          0.        ]
#  [ 0.04892922  0.90214157  0.04892922 ...,  0.          0.          0.        ]
#  [ 0.          0.04892922  0.90214157 ...,  0.          0.          0.        ]
#  ..., 
#  [ 0.          0.          0.         ...,  0.90214157  0.04892922  0.        ]
#  [ 0.          0.          0.         ...,  0.04892922  0.90214157
#    0.04892922]
#  [ 0.          0.          0.         ...,  0.          0.04892922
#    0.90214157]]




### q15 euler_explicite
def euler_explicite(M,T_0,r,V,k):
    if k==1:
        return np.dot(M,T_0)+r*V
    else:
        T=euler_explicite(M,T_0,r,V,k-1)
        return np.dot(M,T)+r*V
        
        
### tracés
les_X=[i*0.4/(N+1) for i in range(N+2)]
plt.plot(les_X,T_0)
plt.plot(les_X,np.dot(M,T_0)+r*V)
for k in [10,40,80,200,400,600,800,1000,2000]:
    plt.plot(les_X,euler_explicite(M,T_0,r,V,k))
plt.show()



d=np.array([[ 5.],
 [ 6.],
 [ 7.],
 [ 8.]])
 
M2=np.array([[ 3. , 2. , 0. , 0.],
 [ 2. , 3.,  2.,  0.],
 [ 0.,  2. , 3. , 2.],
 [ 0. , 0. , 2.,  3.]])

def CalcTkp1(M,d):
    N=d.shape[0]
    c=[M[0,1]/M[0,0]]
    d_prime=[d[0,0]/M[0,0]]
    u=np.zeros((N,1))
    for i in range(1,N-1):
        c.append(M[i,i+1]/(M[i,i]-M[i,i-1]*c[i-1]))
        d_prime.append((d[i,0]-M[i,i-1]*d_prime[-1])/(M[i,i]-M[i,i-1]*c[i-1]))
    d_prime.append((d[N-1,0]-M[N-1,N-2]*d_prime[-1])/(M[N-1,N-1]-M[N-1,N-2]*c[-1]))
    u[N-1,0]=d_prime[-1]
    for j in range(2,N):
        u[N-j,0]=d_prime[N-j]-c[N-j]*u[N-j+1,0]
    return u
    
### complexite O(n)

### q19
def calc_norme(v):
    s=0
    fir i in range(v.shape[0]):
        s=s+v[i,0]**2
    return np.sqrt(s)
    
### q22
def temp_init(Tint,Text,N):
    T_zero=np.zeros((N,1))
    for i in range(N):
        T_zero[i,0]=((Text-Tint)*i/(N-1)+Tint) #si il y a N points on a divisé l'intervalle en N-1
    return T_zero
    
    
### q23
T_tous_k=np.zeros((N,N))
T_zero=temp_init(Tint,Text,N)
for i in range(N):
    T_tous_k[i,0]=T_zero[i,0]
    
### q24
V_implicite=np.zeros((N+2,1))
V_implicite[0,0]=20+273.15
V_implicite[N+1,0]=-10+273.15
M_implicite=np.zeros((N+2,N+2))
M_implicite[0,0]=1+2*r
M_implicite[0,1]=-r
for i in range(1,N+1):
    M_implicite[i,i]=1+2*r
    M_implicite[i,i-1]=-r
    M_implicite[i,i+1]=-r
M_implicite[N+1,N+1]=1+2*r
M_implicite[N+1,N]=-r

### q25
def schema_implicite(M,V,T_0,r,k):
    '''M =np.array(NxN) à inverser
    V vecteur température int ext
    T_0 vecteur température en chaque point à t=0
    on renvoie un vecteur des températures en chaque point au bout de k*delta_t'''
    return ()
    
T=schema_implicite(M,V,T_0,r,1)
for i in range(T.shape[0]):
    T_tous_k[i,0]=T[i,0]
    
### q26
v=np.zeros((T_tous_k.shape[0],1))
for i in range(T_tous_k.shape[0]):
    v[i,0]=T_tous_k[i,1]-T_tous_k[i,0]
k=1
while calc_norme(v)>10**(-2) and k!=ItMax:
    k=k+1
    T=schema_implicite(M,V,T_0,r,k)
    for i in range(T_tous_k.shape[0]):
        T_tous_k[i,k]=T[i,0]
        v[i,0]=T_tous_k[i,k]-T_tous_k[i,k-1]
        
### q27 ????


### q28
k=[0,360,720,1080,1440,1800,2160]
les_X=[i*0.4/(N+1) for i in range(N+2)]
for i in k:
    plt.plot(les_X,T_tous_k[:,i]
plt.show()
    


