
"""
9: Compression de données -RLE

L’algorithme de compression **RLE** (Run Length Encoding) est un algorithme utilisé dans de nombreux formats de fichiers (BMP, TIFF,...).
Il est basé sur l’identification de la répétition consécutive de mêmes éléments.

Le principe consiste à parcourir la séquence de données à compresser et
de donner séquentiellement le nombre de répétitions consécutives d’un élément donné suivie de la description de cet élément.

La séquence de données `AAAAAACCCCAABAAAAAADDD` soumise à l’algorithme RLE identifie :
    "- une séquence de 6 caractères A → 6A,
    "- une séquence de 4 caractères C → 4C,
    "- une séquence de 2 caractères A → 2A,
    "- une séquence de 1 caractère B → 1B,
    "- une séquence de 6 caractères A → 6A,
    "- une séquence de 4 caractères D → 4D
    "et donne la séquence compressée suivante : `6A4C2A1B6A4D`.

    "Définissez une fonction `RLEcompress(tab)` admettant pour argument un tableau de caractères,
    et retournant la version compressée de ce tableau.

    "Proposez ensuite la fonction de décompression`RLEuncompress()`."
"""



"""Fonctions"""
def RLEcompress(tab):
    chars = ""
    if len(tab) > 0:
        letter = tab[0]
        c = 0
        i = 0
        while i < len(tab):
            if tab[i] == letter:
                c += 1
                i += 1
            else:
                chars += str(c)+letter
                letter = tab[i]
                c = 0
        chars += str(c)+letter

    return chars

def RLEuncompress(tab):
    chars = ""
    if len(tab) > 0:
        i = 0
        while i < len(tab):
            chars += int(tab[i]) * tab[i+1]
            i += 2

    return chars


#exemple
chars = "AAAAAACCCCAABAAAAAADDD"

print(chars)
print(RLEcompress(chars))
print(RLEuncompress(RLEcompress(chars)))
