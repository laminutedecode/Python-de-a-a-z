# 🛑 Le mot-clé break permet d'interrompre complètement une boucle en cours
# ⏭️ Le mot-clé continue permet de passer à l'itération suivante sans exécuter le reste du bloc

print("Exemple avec break :")

for i in range(1, 10):
    if i == 5:
        print("On arrête la boucle à i =", i)
        break  # Sort de la boucle immédiatement
    print(i)

print("\nExemple avec continue :")

for i in range(1, 6):
    if i == 3:
        print("On saute l’itération où i =", i)
        continue  # Passe à l'itération suivante sans exécuter print(i)
    print(i)

