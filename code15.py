def moyenne(tab):
    somme = 0
    for val in tab:
        somme += val
    return somme / len(tab)

Exercice 2:

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0' 
    bin_a = '' 
    while a != 0 : 
        bin_a = str(a % 2) + bin_a 
        a = a // 2
    return bin_a