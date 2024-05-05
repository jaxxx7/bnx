def indices_maxi(tab):
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
    for i in range(len(tab)):
        if tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)

Exercice 2:
def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse 


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = [] 
    while pile != []:
        elt = pile.pop() 
        if elt >= 0: 
            pile_positifs.append(elt)
    return renverse(pile_positifs)