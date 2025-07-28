# 📚 Les dictionnaires en Python

# Exemple simple de dictionnaire :
personne = {
    "nom": "Alice",
    "âge": 30,
    "ville": "Paris"
}

# 1. Afficher le dictionnaire complet
print(personne)  # {'nom': 'Alice', 'âge': 30, 'ville': 'Paris'}

# 2. Accéder à une valeur via sa clé
print(personne["nom"])  # "Alice"

# 3. Modifier une valeur
personne["âge"] = 31
print(personne["âge"])  # 31

# 4. Ajouter une nouvelle paire clé/valeur
personne["profession"] = "Développeuse"
print(personne)

# 5. Supprimer une paire clé/valeur
del personne["ville"]
print(personne)

# 6. Vérifier si une clé existe dans le dictionnaire
print("nom" in personne)       # True
print("ville" in personne)     # False

# 7. Obtenir toutes les clés, valeurs ou paires items
print(personne.keys())    # dict_keys(['nom', 'âge', 'profession'])
print(personne.values())  # dict_values(['Alice', 31, 'Développeuse'])
print(personne.items())   # dict_items([('nom', 'Alice'), ('âge', 31), ('profession', 'Développeuse')])

# 8. Utiliser la méthode get() pour accéder à une valeur sans générer d'erreur
print(personne.get("ville"))             # None (au lieu d’erreur si la clé n’existe pas)
print(personne.get("ville", "Inconnue"))  # "Inconnue" si la clé n’existe pas

# 9. Vider le dictionnaire
personne.clear()
print(personne)  # {}

# 10. copy() : crée une copie indépendante du dictionnaire
personne = {
    "nom": "Alice",
    "âge": 31,
    "profession": "Développeuse"
}
copie = personne.copy()
print(copie)

# 11. update() : met à jour le dictionnaire avec un autre dictionnaire ou des paires clé-valeur
personne.update({"ville": "Lyon", "âge": 32})
print(personne)

# 12. pop() : supprime une clé et retourne sa valeur
age = personne.pop("âge")
print(f"Âge supprimé : {age}")
print(personne)

# 13. popitem() : supprime et retourne la dernière paire clé-valeur (Python 3.7+)
dernier = personne.popitem()
print(f"Dernière paire supprimée : {dernier}")
print(personne)
