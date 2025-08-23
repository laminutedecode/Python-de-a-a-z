# 🧪 Les fonctions lambda (ou anonymes) en Python

# ------------------------------------
# 🔹 Exemple 1 : addition simple
addition = lambda x, y: x + y
print(addition(4, 6))  # Affiche 10

# ------------------------------------
# 🔹 Exemple 4 : avec filter (garder uniquement les nombres pairs)
nombres = [1, 2, 3, 4, 5, 6]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # Affiche [2, 4, 6]

