# 🔢 La fonction range() sert à générer une suite de nombres, souvent utilisée dans les boucles for.

for i in range(5):
    print(i)  # Affiche 0, 1, 2, 3, 4


# range(stop) : génère de 0 jusqu'à stop-1
# range(start, stop) : génère de start jusqu'à stop-1
# range(start, stop, step) : génère en sautant step à chaque fois

print("Exemple avec start et stop :")
for i in range(2, 6):
    print(i)  # Affiche 2, 3, 4, 5

print("Exemple avec step (pas) :")
for i in range(1, 10, 2):
    print(i)  # Affiche 1, 3, 5, 7, 9


fruits = ["pomme", "banane", "cerise"]

for i in range(len(fruits)):
    print(f"Fruit numéro {i} : {fruits[i]}")
