def tri_insertion_01(tab):
    """ 
    Trie une liste de nombre en utilisant la méthode du tri par insertion.
    Keyword arguments:
        tab -- liste de nombres
    """
    for i in range (1,len(tab)):
        x=tab[i]
        j=0
        print("i :",i)
        while j<=i-1 and tab[j]<x:
            j = j+1
        for k in range(i-1,j-1,-1):
            print("  ",tab)
            tab[k+1]=tab[k]
            print("  ",tab)
        tab[j]=x
        print(t)
        print("Fin de boucle \n")
        
t = [5,8,3,2,9]

tri_insertion_01(t)
