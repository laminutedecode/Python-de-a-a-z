# 📚 Les fonctions en Python

# 🔹 Définir une fonction
# On utilise le mot-clé "def", suivi du nom de la fonction, des parenthèses (avec ou sans paramètres), puis deux points :
def dire_bonjour():
    print("Bonjour !")

# 🔹 Appeler une fonction
# Pour exécuter le code de la fonction, on l’appelle par son nom avec des parenthèses :
dire_bonjour()  # Affiche "Bonjour !"

# ------------------------------------
# 🔹 Les fonctions peuvent prendre des paramètres
def saluer(prenom):
    print(f"Bonjour {prenom} !")

saluer("Jonathan")  # Affiche "Bonjour Jonathan !"
saluer("Sarah")     # Affiche "Bonjour Sarah !"

# ------------------------------------
# 🔹 Les fonctions peuvent retourner une valeur avec "return"
def addition(a, b):
    return a + b

resultat = addition(5, 3)  # On stocke le résultat de la fonction
print(resultat)  # Affiche 8


# ------------------------------------
# 🔹 Une fonction peut avoir des valeurs par défaut
def saluer_utilisateur(nom="visiteur"):
    print(f"Bienvenue {nom} !")

saluer_utilisateur()           # Affiche "Bienvenue visiteur !"
saluer_utilisateur("Claire")  # Affiche "Bienvenue Claire !"
