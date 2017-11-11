from random import randrange

# Qu. 1

def random_list (n, k) :
    t = [] # crée un tableau vide
    for i in range (n) : # rajoute n fois un élémént à t
        t.append( randrange (k) )   # cet élément est pris au hasard
                                    # entre 0 et k-1
    return (t)

# Qu. 2

def comptage (k, t) :
    """ si t est un tableau à valeurs dans range(k), comptage renvoie
    un tableau u de longueur k tel que pour tout i, u[i] vaut le nombre
    d'occurences de i dans t """
    u = [0]*k
    for i in t : # on parcourt t
        u[i] += 1 # on ajoute 1 à u[i], car on a trouvé une occurence
                 # supplémentaire de i
    return (u)

def counting_sort (k, t) :
    u = comptage (k,t)
    b = [] # b contiendra le tableau trié
    for i in range (k) : # k est la longueur de u
        b += [i] * u[i] # l'élément i est ajouté u[i] fois
    return b

# autre méthode en utilisant comptage_cumulé, je vous laisse finir

def comptage_cumule (k, t) :
    """ si t est un tableau à valeurs dans range(k), comptage_cumule renvoie
    un tableau u de longueur k tel que pour tout i, u[i] vaut le nombre
    d'occurences d'éléments inférieurs ou égaux à i dans t """
    u = comptage (k, t)
    for i in range(1,k) : # invariant : pour j de 0 à i, u[j] vaut le nombre
                # d'occurences d'éléments inférieurs ou égaux à j dans t
        u[i] = u[i] + u[i-1] 
    return (u)

# Qu. 3

def bucket_sort (f,k,t) :
    baquets = [None]*k # on crée un tableau à k éléments bidons
    for i in range(k) :
        baquets[i] = [] # on crée k baquets vides
    for x in t :
        baquets[f(x)] += [x] # on ajoute l'élément x dans le baquet f(x)
                # on remarque que les éléments d'un même baquet sont dans
                # le même ordre que dans t
    b = [] # b sera le tableau trié
    for baquet in baquets :
        b += baquet # on rajoute les éléments des baquets les uns
                    # après les autres
    return b # b contient les éléments de t, triés suivantleur image
        # et deux éléments de même image sont dans le même ordre que
        # dans t

# test

k = 10
n = 16
# créons une fonction aléatoire f de range(k) dans range(k)
T = random_list (k,k) # ce tableau T contient les images de notre
    # future f dans l'ordre : T = [f(0),f(1),...,f(k-1)]
def f (x) :
    return T[x] # il suffit d'envoyer x sur T[x]

t = random_list (n,k)
print(T)
print(t)
print(bucket_sort (f,k,t))

# Qu. 4

def radix_sort(k, t):
    """Retourne une copie de t triée par ordre croissant.
    t doit contenir des entiers appartenant à range(k**2)
    """
    def lp(x):
        return x // k
    def rp(x):
        return x % k
    u = bucket_sort(rp, k, t)
    r = bucket_sort(lp, k, u)
    return r



