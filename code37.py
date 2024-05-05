def moyenne(tab):
    if tab == []:
        print('Le tableau donné est vide')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)
    
Exercice 2:
def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j = len(tab) - 1 # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = i + 1 
        else:
            valeur = tab[j] 
            tab[j] = tab[i] 
            tab[i] = valeur
            j = j -1