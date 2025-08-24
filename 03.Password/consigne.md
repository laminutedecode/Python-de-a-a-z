🔐 Exercice : Mot de passe sécurisé
Crée un programme interactif qui demande à l’utilisateur de saisir un mot de passe. 
Celui-ci doit respecter deux règles essentielles de sécurité :
contenir au moins 8 caractères
contenir au moins un chiffre

📝 Consigne pas à pas :
Demander à l’utilisateur de saisir un mot de passe avec input().
Vérifier que le mot de passe fait au moins 8 caractères (len(mdp) >= 8).
Vérifier qu’il contient au moins un chiffre (any(char.isdigit() for char in mdp)).
Si le mot de passe respecte les deux critères :
afficher ✅ "Mot de passe valide."
et sortir de la boucle.

Sinon :
afficher ❌ "Mot de passe invalide. Il doit contenir au moins 8 caractères et un chiffre."
et redemander la saisie.

💡 Le programme doit continuer à demander un mot de passe tant qu’il n’est pas valide. Utilisez une boucle while pour cela.

