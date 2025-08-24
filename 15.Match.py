# 🆕 Le mot-clé "match" permet de comparer une variable à plusieurs cas différents

def jour_de_la_semaine(jour):
    # On "matche" la valeur de la variable "jour"
    match jour:
        case 1:
            print("Lundi")  # Si jour vaut 1, on affiche "Lundi"
        case 2:
            print("Mardi")  # Si jour vaut 2, on affiche "Mardi"
        case 3:
            print("Mercredi")
        case 4:
            print("Jeudi")
        case 5:
            print("Vendredi")
        case 6:
            print("Samedi")
        case 7:
            print("Dimanche")
        case _:  # Le caractère underscore signifie "tout autre cas"
            print("Jour inconnu")  # Ce bloc s'exécute si aucun case ne correspond



jour_de_la_semaine(3)   # Affiche "Mercredi"
jour_de_la_semaine(7)   # Affiche "Dimanche"
jour_de_la_semaine(10)  # Affiche "Jour inconnu"

