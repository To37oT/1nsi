---
layout: default
title: Projet 1
permalink: /projet1/
published: true
date: 2024
---

# Projet 1 : Répertoire téléphonique Python

## 1) la fonction input

la fonction **input** va permettre aux utilisateurs de saisir des données au clavier.

##### Préparation 1
>
>Testez ce programme dans Thonny :
>
>
>     age=input("Quel est votre âge ? ")
>		
>Quel est la valeur de la variable **age** après avoir exécuté le programme ci-dessus ? <br>
>Quel est le type de la variable **age** ?
>

Comme vous avez pu le constater, la valeur saisie par l'utilisateur sera toujours de type "string".


##### Préparation 2
>
>Testez ce programme à l'aide de Thonny :
>
>     val=input("Entrez un nombre")
>     val=val+1

Comme vous l'avez remarqué, nous avons une erreur puisque la deuxième ligne **val=val+1** contient un entier avec **1** et une chaîne de caractères avec la variable **val**, séparés par un signe **+**. Python n'est pas capable de gérer le problème (le signe + peut correspondre à une concaténation ou à une addition), nous avons donc une erreur.

Pour éviter ce genre de problème, il peut être nécessaire de transformer notre chaîne de caractères en entier :

##### Préparation 3
>
>Testez ce programme à l'aide de Thonny :
>
>     val=input("Entrez un nombre")
>     val=int(val)
>     val=val+1

## 2) Écrire et lire dans un fichier externe

Il est possible de lire ou d'écrire des données dans un fichier extérieur avec python.

La première des choses à faire est d'ouvrir notre fichier texte dans votre code. Pour ce faire nous utiliserons la méthode **open**.

     with open('nomDuFichier', 'r') as f :

Nous utilisons ici une structure particulière que nous n'avons encore jamais rencontrée : le **with**.

**La méthode open prend 2 paramètres : le nom du fichier et le mode d'ouverture du fichier**

Il existe 3 modes d'ouverture pour un fichier :

- 'r ' : ouverture en lecture
- 'w' : ouverture en écriture. Le contenu du fichier est écrasé. Si le fichier n'existe pas, il est créé.
- 'a' : ouverture en écriture en mode ajout. On écrit à la fin du fichier sans écraser l'ancien contenu du fichier. Si le fichier n'existe pas, il est créé.

Une fois le fichier ouvert, il est possible d'écrire dedans (à l'aide de *write*) ou de lire son contenu (à l'aide de *read*).

##### Préparation 4
>
>Étudiez et testez le programme suivant :
>
>     nom=input('Entrez un mot')
>     with open('fichier.txt','a') as f :
>          f.write(nom)
>		
>Le répertoire courant (où votre document python s'execute) devrait maintenant contenir aussi un fichier **fichier.txt**. Ouvrez ce fichier (avec un éditeur de texte) et vérifiez qu'il contient bien le mot >entré par l'utilisateur.

##### Préparation 5
>
>Étudiez et testez le programme suivant :
>
>     with open('fichier.txt','r') as f :
>          ligne=f.read()
>
>Quelle va être la valeur de la variable **ligne** après l'exécution de ce programme ? Vérifiez votre réponse.

##### Préparation 6
>
>Écrivez un programme permettant à l'utilisateur de sauvegarder 5 noms dans un fichier texte **fichier.txt**
>
>Vérifiez que votre programme est correct en ouvrant le fichier txt à l'aide d'un éditeur de texte.
>
>Votre fichier texte devrait être peu lisible (les mots s'enchaînent sans aucun espace ou saut à la ligne). Il est tout à fait possible de forcer le saut de ligne en utilisant la suite de caractères suivante: **\n** (l'enchaînement des caractères **\** et **n** entraîne un retour à la ligne).
>
>**Exemple :**
>
>     print('hello \n world')
>
>n'affiche pas : 
>
>     hello \n world
>
>mais :
>
>     hello
>     world
>
>Nous avons bien un saut de ligne. Le caractère \n n'est pas affiché.

##### Préparation 7
>
>Modifier votre programme de la préparation 7 afin d'avoir un nom par ligne dans le fichier texte.

##### Préparation 8
>
>Voici un programme permettant de lire le fichier texte et de ranger les différents noms entrés par l'utilisateur dans une liste, testez ce programme :
>
>
>     noms=[]
>     with open('fichier.txt','r') as f :
>          for ligne in f:
>               ligne=ligne.replace("\n","")
>               noms.append(ligne)
>
>NB : la ligne **ligne=ligne.replace("\n","")** permet d'enlever la suite de caractères \n, car même si \n n'est pas visible dans le fichier texte, elle est tout de même présente.

## 3) Commenter son code

Afin de rendre votre programme plus clair, il est nécessaire, dès que votre code dépasse une dizaine de lignes, d'introduire des commentaires. Bien sûr cela peut permettre à une personne qui n'a pas écrit le programme de comprendre ce que vous avez voulu faire, mais cela peut aussi vous permettre, quelques mois après avoir terminé d'écrire votre code, de vous aider lors de modifications.

En Python, toute ligne commençant par le caractère dièse (#) sera considérée comme un commentaire par le système interpréteur/compilateur.

Voici un exemple de programme commenté :

>     # la fonction monMessage permet d'afficher un message
>     #****************début de la fonction monMessage******************
>     def monMessage(nom):
>          return f"Bonjour {nom}"
>     #****************fin de la fonction monMessage********************
>     # interrogation de l'utilisateur
>     monNom=input("Quel est votre nom ? ")
>     # appel de la fonction monMessage
>     msg=monMessage(monNom)

Attention, dans l'exemple ci-dessus le programme est volontairement alourdi avec des commentaires inutiles.

Vous avez aussi la possibilité de créer des commentaires multilignes avec **"""** en début et fin de bloc.

>     """Ceci est un programme permettant d'empiler des blocs
>     de différentes natures.
>     Date de création : 01/01/1970
>     Création : Jay Thoubont
>     """

POUR TOUT VOS PROJETS IL EST ATTENDU :
- Un commentaire de début de programme (présentation/objectif, date de création, créateur, dernière mise à jour,...)
- Avant chaque fonction, une présentation de son rôle, de ses paramètres.
- Et si un bloc de code (boucle, condition,...) n'est pas intuitif, une petite aide pour le comprendre.

Demandez-vous ce qui vous aiderait à la comprendre si vous retombiez sur ce programme dans 6 mois
  
## 4) projet
>
>En utilisant les connaissances acquises jusqu'à présent, vous allez écrire un programme de gestion de répertoire téléphonique.

##### CONSIGNES PROJETS
>
>Ce programme devra proposer le menu suivant à l'utilisateur :
>
>     0-quitter
>     1-écrire dans le répertoire
>     2-rechercher dans le répertoire
>     Votre choix ?
>
>Si le choix est 0 : Le programme sera stoppé.
>
>Si le choix est 1 :
>L'utilisateur devra saisir un nom ou 0 s'il veut terminer la saisie (" Nom (0 pour terminer) : ") :
>- L'utilisateur entre 0 => le programme devra le renvoyer vers le menu
>- L'utilisateur entre un nom => le programme devra lui demander de saisir le numéro de téléphone correspondant au nom. Une fois le numéro saisi, le programme devra lui proposer d'entrer un nouveau nom (ou 0 pour terminer)...
>
>Exemple de saisie d'un utilisateur (toto) :
>
>![pr1_1](https://github.com/user-attachments/assets/158b22b6-4fcf-4086-bb54-c78838d8f191)
>
>Si le choix est 2 :
>
>L'utilisateur devra saisir le nom recherché ("Entrer un nom :").
>
>- Si le nom recherché est présent dans le répertoire, le programme devra afficher " Le numéro recherché est : " suivi du numéro de téléphone correspondant au nom saisi.
>
>- Si le nom recherché est absent du répertoire, le programme devra afficher " Inconnu ".
>
>L'utilisateur est ensuite redirigé vers le menu principal.
>
>recherche des utilisateurs (toto et titi) :
>
>![pr1_2](https://github.com/user-attachments/assets/87c3d28e-56b1-4b43-aa4c-73b58c0ea612){:target="_blank"}
>
>Voici une démonstration en vidéo : [https://www.youtube.com/watch?v=itSlzuGZHe8](https://www.youtube.com/watch?v=itSlzuGZHe8)
>
>Les noms et numéros de téléphone devront être stockés dans un fichier texte.
>
>Votre programme devra être composé au minimum de 3 fonctions : une fonction **menu**, une fonction **lecture** et une fonction **ecriture**.
