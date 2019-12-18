
"""
Fonction de construction de chaine de caractère à partir d'un tableau
"""

"""Fonction"""
def implodeStrToken(tokens, sep):
    ch = ""
    sep = str(sep)
    for i in range(len(tokens)):
        ch += tokens[i] + sep
    
    return ch



#exemple
tabTokens = ["il", "fait", "beau", "ici", "n’est", "ce", "pas", "oui", "c’est", "vrai"]

print(implodeStrToken(tabTokens," ")) #"il;fait;beau;ici;n’est;ce;pas;oui;c’est;vrai"
print(implodeStrToken([],";")) #
print(implodeStrToken(tabTokens,12)) #il12fait12beau12ici12n’est12ce12pas12oui12c’est12vrai12