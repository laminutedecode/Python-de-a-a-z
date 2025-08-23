# 🔍 Les conditions permettent de prendre des décisions dans un programme
# On utilise if, elif (sinon si) et else (sinon)

# 🎯 Exemple 1 : simple condition
age = 20
if age >= 18:
    print("Tu es majeur.")  # Affiche ce message si l'âge est supérieur ou égal à 18

# 🧩 Exemple 2 : if + else
age = 16
if age >= 18:
    print("Majeur")
else:
    print("Mineur")  

note = 15
if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Échec")
