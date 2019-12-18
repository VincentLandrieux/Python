"""
Fonction qui retourne la première lettre de l'alphabet manquante dans une chaine de caractère
"""

"""Variable"""
phrase = "Portez ce vieux whisky au juge blond qui fume"

"""Fonction"""
def pangramme(chaine):
    lettres = ("a", "b", "c","d", "e", "f", "g", 
               "h", "i", "j", "k", "l", "m", "n", 
               "o", "p", "q", "r", "s", "t", "u", 
               "v", "w", "x", "y", "z")
    chaine = chaine.lower()
    
    l = ""
    flag = False
    i = 0
    while i < len(lettres):
        flag = False
        j = 0
        while j < len(chaine):
            if chaine[j] == lettres[i]:
                j = len(chaine)
                flag = True
            j += 1
        if not(flag):
            l = lettres[i]
            i = len(lettres)
        i += 1
        
    return flag , l

#exemple
print(pangramme(phrase))
print(pangramme("Monsieur Jack, vous dactylographiez bien mieux que votre ami Wolf"))
print(pangramme("Voix ambiguë d'un cœur qui, au zéphyr, préfère les jattes de kiwis"))
print(pangramme("Le vif zéphyr jubile sur les kumquats du clown gracieux"))

print(pangramme("bonjour"))
