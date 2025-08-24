# 🔁 La boucle for en Python

# 1. Parcourir une liste
fruits = ["pomme", "banane", "kiwi"]

for fruit in fruits:
    print(fruit)

# 2. Parcourir une chaîne de caractères
mot = "Python"
for lettre in mot:
    print(lettre)

# 3. Parcourir un tuple
coordonnees = (10, 20)
for valeur in coordonnees:
    print(valeur)

# 4. Parcourir un set (attention : l’ordre n’est pas garanti)
animaux = {"chat", "chien", "lapin"}
for animal in animaux:
    print(animal)

# 5. Parcourir un dictionnaire (clés uniquement)
utilisateur = {"nom": "Alice", "age": 30}
for cle in utilisateur:
    print(cle)

# 6. Parcourir les clés **et** les valeurs d’un dictionnaire
for cle, valeur in utilisateur.items():
    print(cle, ":", valeur)

# 7. Boucle avec index et élément (avec enumerate)
for index, fruit in enumerate(fruits):
    print(f"Index {index} : {fruit}")
    # f : permet de formater la chaîne avec des variables

# 8. Boucle avec condition interne
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)
