
"""Fonctions"""
def Puissance(n,p):
    """Renvoie la puissance de n par p
    @ENTREE:
        n <int>: nombre
        p <int>: puissance
    @SORTIE:
        n <int>: resultat
	"""
    if(p > 1):
        n *= Puissance(n,p-1)
    
    return n


#exemple
print(Puissance(3,3))