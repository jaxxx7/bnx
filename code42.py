def moyenne(tab):
    somme = 0
    for elt in tab:
        somme += elt
    return somme / len(tab)

Exercice 2:
def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab) - 1 
    while debut <= fin:
        m = (debut + fin) // 2 
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1 
        else:
            fin = m - 1 
    return False