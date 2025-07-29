# 🌳 Les ensembles (set) en Python
# Il ne peut pas contenir de doublons, et l'ordre des éléments n'est pas garanti.

# Création d'un set
fruits = {"pomme", "banane", "kiwi", "orange", "fraise"}
print("Set de départ :", fruits)

# 1. Ajouter un élément (add)
fruits.add("abricot")
print("Après add('abricot') :", fruits)

# 2. Ajouter plusieurs éléments (update)
fruits.update(["cerise", "melon", "banane"])  # "banane" est déjà présent, pas ajouté en doublon
print("Après update(['cerise', 'melon', 'banane']) :", fruits)

# 3. Supprimer un élément (remove)
fruits.remove("kiwi")  # Supprime "kiwi", génère une erreur si l'élément n'existe pas
print("Après remove('kiwi') :", fruits)

# 4. Supprimer un élément sans erreur (discard)
fruits.discard("ananas")  # Ne fait rien si l'élément n'existe pas, pas d'erreur
print("Après discard('ananas') :", fruits)

# 5. Supprimer et retourner un élément arbitraire (pop)
element = fruits.pop()
print("Élément retiré avec pop() :", element)
print("Set après pop() :", fruits)

# 6. Vider un set (clear)
fruits.clear()
print("Set après clear() :", fruits)

set_a = {"pomme", "banane", "cerise"}
set_b = {"banane", "cerise", "orange", "melon"}

# 7. Union : tous les éléments de set_a et set_b
union = set_a.union(set_b)
print("Union :", union)

# 8. Intersection : éléments communs aux deux sets
intersection = set_a.intersection(set_b)
print("Intersection :", intersection)

# 9. Différence : éléments de set_a qui ne sont pas dans set_b
difference = set_a.difference(set_b)
print("Différence (set_a - set_b) :", difference)

# 10. Différence symétrique : éléments présents dans un set mais pas dans l'autre
diff_sym = set_a.symmetric_difference(set_b)
print("Différence symétrique :", diff_sym)

# 11. Vérifier si un élément est dans un set
print("'pomme' dans set_a ?", "pomme" in set_a)
print("'melon' dans set_a ?", "melon" in set_a)
