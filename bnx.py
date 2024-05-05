def printe(numero):
    nom_fichier = f"code{numero}.py"
    try:
        with open(nom_fichier, "r") as fichier:
            contenu = fichier.read()
            print(f"Contenu du code {numero} :")
            print(contenu)
    except FileNotFoundError:
        print(f"Le code {numero} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

