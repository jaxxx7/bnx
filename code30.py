def fusion(tab1, tab2):
    tab_fusion = []
    i1 = 0
    i2 = 0
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_fusion.append(tab1[i1])
            i1 += 1
        else:
            tab_fusion.append(tab2[i2])
            i2 += 1

    if i1 == len(tab1):
        while i2 < len(tab2):
            tab_fusion.append(tab2[i2])
            i2 += 1
    else:
        while i1 < len(tab1):
            tab_fusion.append(tab1[i1])
            i1 += 1        

    return tab_fusion

Exercice 2:
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]