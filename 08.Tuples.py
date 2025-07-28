# 🎯 Les tuples en Python

# 1. Création d’un tuple
coordonnees = (10.5, 20.3)
print("Tuple de départ :", coordonnees)

# 2. Accès à un élément (par index)
print("Premier élément :", coordonnees[0])  # Affiche 10.5
print("Deuxième élément :", coordonnees[1])  # Affiche 20.3

# 3. Taille du tuple (nombre d’éléments)
print("Taille du tuple :", len(coordonnees))  # Affiche 2

# 4. Un tuple peut contenir différents types de données
infos_utilisateur = ("Alice", 30, True)
print("Tuple mixte :", infos_utilisateur)

# 5. Tuple avec un seul élément : attention à la virgule !
unique = ("seul",)  # La virgule est obligatoire pour créer un tuple
print("Tuple avec un seul élément :", unique)

# 6. Concaténation de tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
concat = tuple1 + tuple2
print("Concaténation :", concat)

# 7. Répéter un tuple
repetition = tuple1 * 3
print("Répétition :", repetition)

# 8. Vérifier la présence d’un élément
print("2 est dans tuple1 ?", 2 in tuple1)  # True
print("10 est dans tuple1 ?", 10 in tuple1)  # False