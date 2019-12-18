"""
Fonction de conversion d'un chiffre binaire en décimal
"""

"""Fonctions"""
def BinToDec(nbi):
    """Renvoie la conversion d'un binaire en décimal
    @ENTREE:
        nbi <string>: binaire à convertir
    @SORTIE:
        nd <int>: nombre converti en décimal
	"""
    nd = 0
    for i in range(len(nbi)):
        nd += int(nbi[-i-1]) * (2**i)
        #print(nbi[-i-1], 2**i, nd)
    
    return nd


#exemple
print(BinToDec("1011"))