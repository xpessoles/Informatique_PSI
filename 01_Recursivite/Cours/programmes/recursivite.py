def fonction_recursive():
    return fonction_recursive()
#fonction_recursive()

def P2_iterative(n):
    """
    Entrée : n(int)
    Sorite : 2^n
    """
    res = 1
    if n==0:
        return res
    else : 
        while n>0:
            res=2*res
            n=n-1
        return res
        
print(P2_iterative(0))
print(P2_iterative(1))
print(P2_iterative(2))

def P2_rapide(n):
    if n == 0:
        return 1
    if n%2 == 0 :
        tmp = P2_rapide(n/2)
        return tmp*tmp
    else : 
       return (2*P2_rapide(n-1))


