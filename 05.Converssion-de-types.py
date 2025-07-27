# 🔄 Conversion de types en Python (type casting)
# On peut changer le type d'une valeur grâce à des fonctions comme int(), float(), str(), bool()

# 🧪 Exemple 1 : convertir une chaîne de caractères (texte) en entier
texte = "123"
print(texte)          # Affiche "123"
print(type(texte))    # Affiche <class 'str'>

# Conversion en entier
nombre = int(texte)
print(nombre)         # Affiche 123
print(type(nombre))   # Affiche <class 'int'>

# ➗ Exemple 2 : convertir un texte en float (nombre à virgule)
texte_decimal = "3.14"
nombre_decimal = float(texte_decimal)
print(nombre_decimal)       # Affiche 3.14
print(type(nombre_decimal)) # Affiche <class 'float'>

# 📝 Exemple 3 : convertir un nombre en texte
entier = 42
texte_converti = str(entier)
print(texte_converti)       # Affiche "42"
print(type(texte_converti)) # Affiche <class 'str'>

# 🟢 Exemple 4 : convertir en booléen (valeur logique)
# Règle : vide → False, sinon → True
print(bool("salut"))  # True (non vide)
print(bool(""))       # False (vide)
print(bool(0))        # False
print(bool(1))        # True

# 📌 Fonctions utiles :
# int()   → transforme en entier
# float() → transforme en nombre à virgule
# str()   → transforme en texte
# bool()  → transforme en booléen (True/False)
