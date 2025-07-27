# 🍎 Une liste, c’est comme une boîte dans laquelle tu ranges plusieurs objets (valeurs)
# Tu peux y mettre ce que tu veux : des chaînes, des nombres, d’autres listes, etc.
# Ici, on crée une liste de fruits :
fruits = ["pomme", "banane", "kiwi", "orange", "fraise"]

# 1. Accéder à un élément par son index (position, début à 0)
print(fruits[0])  # "pomme" (premier élément)
print(fruits[3])  # "orange" (quatrième élément)

# 2. Accéder au dernier élément avec un index négatif
print(fruits[-1])  # "fraise" (dernier élément)
print(fruits[-2])  # "orange" (avant-dernier élément)

# 3. Accéder à une tranche (slice) de la liste : fruits[start:stop]
# Renvoie une nouvelle liste contenant les éléments de l'index start à stop-1
print(fruits[1:4])  # ['banane', 'kiwi', 'orange'] (indices 1,2,3)

# 4. Sauter des éléments dans une tranche : fruits[start:stop:step]
print(fruits[0:5:2])  # ['pomme', 'kiwi', 'fraise'] (indices 0,2,4)

# 5. Modifier un élément (affectation par index)
fruits[2] = "melon"
print(fruits)  # ['pomme', 'banane', 'melon', 'orange', 'fraise']

# 6. Modifier une tranche (remplacer plusieurs éléments)
fruits[1:3] = ["cerise", "mangue"]
print(fruits)  # ['pomme', 'cerise', 'mangue', 'orange', 'fraise']

# 7. Ajouter un élément à la fin (append)
fruits.append("abricot")
print(fruits)  # ['pomme', 'cerise', 'mangue', 'orange', 'fraise', 'abricot']

# 8. Insérer un élément à une position donnée (insert)
fruits.insert(2, "ananas")  # Ajoute "ananas" à l'index 2
print(fruits)  # ['pomme', 'cerise', 'ananas', 'mangue', 'orange', 'fraise', 'abricot']

# 9. Supprimer un élément par sa valeur (remove)
fruits.remove("orange")
print(fruits)  # ['pomme', 'cerise', 'ananas', 'mangue', 'fraise', 'abricot']

# 10. Supprimer un élément par son index (del)
del fruits[0]
print(fruits)  # ['cerise', 'ananas', 'mangue', 'fraise', 'abricot']

# 11. Obtenir la longueur de la liste (nombre d'éléments)
print(len(fruits))  # 5

# 12. Parcourir la liste avec une boucle for
for fruit in fruits:
    print(fruit)

# 13. pop() : supprime et retourne un élément (par défaut le dernier)
dernier = fruits.pop()
print("Élément retiré avec pop():", dernier)
print("Liste après pop():", fruits)

# 14. pop(index) : supprime et retourne l'élément à l'index donné
deuxieme = fruits.pop(1)
print("Élément retiré avec pop(1):", deuxieme)
print("Liste après pop(1):", fruits)

# 15. extend(iterable) : ajoute plusieurs éléments à la fin
fruits.extend(["pasteque", "melon"])
print("Liste après extend(['pasteque', 'melon']):", fruits)

# 16. index(element) : retourne l'index de la première occurrence de l'élément
pos = fruits.index("melon")
print("Position de 'melon' dans la liste:", pos)

# 17. count(element) : compte combien de fois l'élément apparaît
nb_cerise = fruits.count("cerise")
print("Nombre d'occurrences de 'cerise':", nb_cerise)

# 18. sort() : trie la liste (modifie la liste en place)
fruits.sort()
print("Liste après sort():", fruits)

# 19. sort(reverse=True) : trie en ordre décroissant
fruits.sort(reverse=True)
print("Liste après sort(reverse=True):", fruits)

# 20. reverse() : inverse l'ordre des éléments (modifie la liste en place)
fruits.reverse()
print("Liste après reverse():", fruits)

# 21. clear() : vide la liste
fruits.clear()
print("Liste après clear():", fruits)
