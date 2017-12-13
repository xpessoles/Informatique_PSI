#! /usr/local/bin/python3.4
# -*- coding:utf-8 -*-

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([1, 2, 3, 4, 5, 6])
d = np.array([[1, 2, 3],
              [4, 5, 6]])
e = np.array([[1, 4],
              [2, 5],
              [3, 6]])

print("Pour a : ")
print(a)
print("ndim : {}".format(a.ndim))
print("shape : {}".format(a.shape))
print("dtype : {}".format(a.dtype))
print("size : {}".format(a.size))
# Pour a : 
# [1 2 3]
# ndim : 1
# shape : (3,)
# dtype : int64
# size : 3

print("Pour d : ")
print(d)
print("ndim : {}".format(d.ndim))
print("shape : {}".format(d.shape))
print("dtype : {}".format(d.dtype))
print("size : {}".format(d.size))
# Pour d : 
# [[1 2 3]
#  [4 5 6]]
# ndim : 2
# shape : (2, 3)
# dtype : int64
# size : 6

print("Pour e : ")
print(e)
print("ndim : {}".format(e.ndim))
print("shape : {}".format(e.shape))
print("dtype : {}".format(e.dtype))
print("size : {}".format(e.size))
# Pour e : 
# [[1 4]
#  [2 5]
#  [3 6]]
# ndim : 2
# shape : (3, 2)
# dtype : int64
# size : 6

f = np.concatenate((a,b),axis=0)
print(f)
# [1 2 3 4 5 6]
print(f==c)
# [ True  True  True  True  True  True]
print(np.equal(f,c))
# [ True  True  True  True  True  True]
print(np.array_equal(f,c))
# True

f.shape = (2,3)
print(f)
# [[1 2 3]
#  [4 5 6]]
print(np.array_equal(f,d))
# True

f = f.astype(float)
print(f)
# [[ 1.  2.  3.]
#  [ 4.  5.  6.]]
print(np.array_equal(f,d))
# True

a.shape = (3,1)
print(a)
# [[1]
#  [2]
#  [3]]
b.shape = (3,1)
g = np.concatenate((a,b), axis = 0)       # NON, ce n'est pas
print(g)                                  # selon le bon axe
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

g = np.concatenate((a,b), axis = 1)       # là, oui
print(g)
# [[1 4]
#  [2 5]
#  [3 6]]

z = np.zeros((3,2))                       # Attention ! flottants par défaut
print(z)
# [[ 0.  0.]
#  [ 0.  0.]
#  [ 0.  0.]]
h = np.concatenate((e,z), axis = 1)
print(h)
# [[ 1.  4.  0.  0.]
#  [ 2.  5.  0.  0.]
#  [ 3.  6.  0.  0.]]
# C'est un tableau de flottants que l'on obtient.
# Pour être correct, il faut commencer par construire un tableau de zéros int

z = np.zeros((3,2), dtype=np.int)
print(z)
# [[0 0]
#  [0 0]
#  [0 0]]
h = np.concatenate((e,z), axis = 1)
print(h)
# [[1 4 0 0]
#  [2 5 0 0]
#  [3 6 0 0]]

