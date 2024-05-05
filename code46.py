def recherche(tab, n):
    ind_debut = 0
    ind_fin = len(tab) - 1
    while ind_debut <= ind_fin:
        ind_milieu = (ind_debut + ind_fin) // 2
        if tab[ind_milieu] == n:
            return ind_milieu
        elif tab[ind_milieu] < n:
            ind_debut = ind_milieu + 1
        else:
            ind_fin = ind_milieu - 1
    return None

Exercice 2:
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c 
    return resultat