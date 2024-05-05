def recherche_indices_classement(elt, tab):
    ind_inf = []
    ind_egal = []
    ind_sup = [] 
    for i in range(len(tab)):
        if tab[i] < elt:
            ind_inf.append(i)
        elif tab[i] > elt:
            ind_sup.append(i)
        else:
            ind_egal.append(i)
    return (ind_inf, ind_egal, ind_sup)

Exercice 2:
def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats: 
        notes = resultats[nom]
        if notes == {}: # pas de notes 
            return 0
        total_points = 0 
        total_coefficients = 0 
        for valeurs in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + note * coefficient 
            total_coefficients = total_coefficients + coefficient 
        return round( total_points / total_coefficients, 1 ) 
    else:
        return None