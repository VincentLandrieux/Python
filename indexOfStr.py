"""
Fonction qui retourne l'index d'une sous chaine de caractère ou -1 si inexistant
"""

"""Fonction"""
def indexOfStr(chaine, sChaine):
    index = -1
    for i in range(len(chaine)-len(sChaine)):
        if chaine[i : i+len(sChaine)] == sChaine:
            index = i
            break
    
    return index

#exemple
chaine = "il fait beau ici ; n'est ce pas ? oui c’est vrai"
    
print(indexOfStr(chaine, "bea"))
print(indexOfStr(chaine, "aeb"))