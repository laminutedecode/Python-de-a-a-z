# 🔁 La boucle while permet de répéter un bloc de code tant qu'une condition est vraie.

compteur = 1  # On commence à 1

while compteur <= 5:
    print(f"Tour numéro {compteur}")
    compteur += 1  

mot_de_passe_correct = "python123"
tentative = ""

while tentative != mot_de_passe_correct:
    tentative = input("Entre le mot de passe : ")
    if tentative != mot_de_passe_correct:
        print("Mot de passe incorrect. Essaie encore.")

print("✅ Accès autorisé !")

