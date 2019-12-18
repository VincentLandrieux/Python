
"""Fonctions"""
def Fibonacci(n):
    """Renvoie le nième terme de la suite de fibonacci
    @ENTREE:
        n <int>: index de la suite
    @SORTIE:
        n <int>: terme
	"""

    if(n > 1):
        n = Fibonacci(n-1) + Fibonacci(n-2)
        
    return n

"""Entrer"""
print("Entrer un entier")
n = int(input())

"""Affichage"""
print("resultat",Fibonacci(n))