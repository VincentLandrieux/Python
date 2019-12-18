"""
Fonction de conversion d'un chiffre décimal en binaire
"""

def DecToBin(nd):
    """Renvoie une chaîne de caractères contenant la représentation binaire
    @ENTREE:
        nd <int>: nombre à convertir
    @SORTIE:
        nbi <string>: nombre converti en binaire
	"""
    nbi = ""
    while (nd >= 1):
        nbi = str(nd%2) + nbi
        nd //= 2
        #print(nbi, nd)
    
    return nbi

#exemple
print(DecToBin(11))