# ⚖️ Les opérateurs de comparaison permettent de comparer deux valeurs.
# Ils retournent toujours un booléen : True ou False

a = 10
b = 5

print(a == b)   # False → égalité (est-ce que a est égal à b ?)
print(a != b)   # True → différence (est-ce que a est différent de b ?)
print(a > b)    # True → supérieur
print(a < b)    # False → inférieur
print(a >= 10)  # True → supérieur ou égal
print(b <= 5)   # True → inférieur ou égal

# 🔗 Les opérateurs logiques permettent de combiner plusieurs conditions

age = 20
abonnement = True

# AND : toutes les conditions doivent être vraies
if age >= 18 and abonnement:
    print("Tu peux accéder au contenu réservé.")  # Les deux conditions sont vraies

# NOT : inverse une condition
majeur = age >= 18
print(not majeur)  # Affiche False car l'utilisateur est majeur

if age < 18 or not abonnement:
    print("Accès restreint.")  # Si l'âge est < 18 OU si pas d'abonnement
