

def NbPairImpair(tab):
    """Renvoie le nombre d’élément(s) pair(s) et le nombre d’élément(s) impair(s) 
    @ENTREE:
        tab <list>: tableau de valeur
    @SORTIE:
        np <int>: nombre d'éléments pair
        mip <int>: nombre d'éléments impair
	"""
    np = 0
    nip = 0
    for i in tab:
        if(i%2 == 0):
            np += 1
        else:
            nip += 1
    
    return np,nip
    

#exemple
tab1 = [1,2,3,4,5]

print("Il y a", NbPairImpair(tab1)[0], "nombre(s) pair(s)")
print("Il y a", NbPairImpair(tab1)[1], "nombre(s) impair(s)")