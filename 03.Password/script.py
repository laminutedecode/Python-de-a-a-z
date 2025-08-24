while True:
    mdp = input("Entre un mot de passe (min 8 caractères, au moins 1 chiffre) : ")
    
    contient_chiffre = any(char.isdigit() for char in mdp)

    if longueur_ok and contient_chiffre:
        print("Mot de passe valide.")
        break
       
    else:
        print("Mot de passe invalide. Il doit contenir au moins 8 caractères et un chiffre.")
