# 🔄 La fonction input() en Python
# Elle permet de demander une saisie (une entrée) à l'utilisateur via le clavier.

# Exemple simple : demander le prénom
prenom = input("Quel est ton prénom ? ")

# Afficher ce que l'utilisateur a saisi
print("Bonjour", prenom + "!")

# ------------------------------------
# Remarque importante :
# La fonction input() retourne toujours une chaîne de caractères (string).

age_str = input("Quel âge as-tu ? ")
age = int(age_str)  

print(f"Tu as {age} ans.")

# ------------------------------------
# Attention aux erreurs !
# Si l'utilisateur entre autre chose qu'un nombre, la conversion avec int() plantera.

try:
    age = int(input("Quel âge as-tu ? "))
    print(f"Tu as {age} ans.")
except ValueError:
    print("Tu n'as pas entré un nombre valide.")
