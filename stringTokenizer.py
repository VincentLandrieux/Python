"""
Fonction de découpage de chaine de caractère en tableau
"""

"""Variable"""
chaine = "Le printemps;est pour bientôt mais : il faut attendre l’hiver"

"""Fonction"""
def stringTokenizer(chaine, sep):
    tokens = []
    if len(chaine) > 0:
        d = 0
        for i in range(len(chaine)):
            for j in range(len(sep)):
                if chaine[i] == sep[j]:
                    tokens.append(chaine[d:i])
                    d = i+1
                    break
        tokens.append(chaine[d:i+1])
    
    return tokens

"""Affichage"""
print(stringTokenizer(chaine, "*:;"))