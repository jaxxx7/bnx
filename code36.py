def occurrences(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme += 1
    return somme

Exercice 2:
valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)