---
layout: default
title: Chapitre 3
permalink: /chapitre3/
published: true
date: 2024
---

# I) Les dictionnaires

## A)  Présentation des dictionnaires

Comme les listes, les dictionnaires permettent de "stocker" des données. Chaque élément d'un dictionnaire est composé de 2 parties, on parle de paires **clé/valeur**. 

Voici un exemple de dictionnaire :

```
mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}
```

Nous utilisons des accolades **{ }** pour définir le début et la fin du dictionnaire (alors que nous utilisons des crochets [] pour les listes et les parenthèses pour les tuples). <br>
Dans le dictionnaire ci-dessus, "nom", "prenom" et "date de naissance" sont des **clés** et "Durand", "Christophe" et "29/02/1981" sont des **valeurs**.<br>
La clé "nom" est associée à la valeur "Durand", la clé "prenom" est associée à la valeur "Christophe" et la clé "date de naissance" est associée à la valeur "29/02/1981". 
- Les clés sont des chaînes de caractères ou des nombres. 
- Les valeurs peuvent être des chaînes de caractères, des nombres, des booléens...

Pour créer un dictionnaire, il est possible de procéder comme suit :

```
mon_dico = {}
mon_dico["nom"] = "Durand"
mon_dico["prenom"] = "Christophe"
mon_dico["date de naissance"] = "29/02/1981"
```

À noter qu'il est aussi possible d'écrire :

```
mon_dico = dict()
mon_dico["nom"] = "Durand"
mon_dico["prenom"] = "Christophe"
mon_dico["date de naissance"] = "29/02/1981"
```

Il est possible d'obtenir la valeur associée à une clé :

```
mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}

val = mon_dico['nom']
```

Dans le programme ci-dessus, la variable **val** aura pour valeur **Durand**.

Il est facile d'ajouter un élément à un dictionnaire (les dictionnaires sont mutables)

```
mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}

mon_dico['lieu de naissance'] = 'Paris'
```
La  deuxième ligne du programme ci-dessus  a permis  d'ajouter la clé **lieu de naissance** au dictionnaire **mon_dico**. Cette clé a pour valeur **Paris**

L'instruction **del** permet du supprimer une paire "clé/valeur"

Soit le dictionnaire suivant :

```
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}
```
si on exécute la ligne :

```
del mes_fruits["pomme"]
```
le dictionnaire **mes_fruits** n'aura plus  que 2 clés : **poire** et **orange**

Il est possible de modifier la valeur d'une clé :

```
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}
mes_fruits["pomme"] = mes_fruits["pomme"] - 1
```

Après l'exécution de ce programme, la clé **pomme*** aura pour valeur 3

##### Exercice dictionnaire 1

> Tapez la ligne suivante :
> 
>      mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}
> 
> Qu'affiche la variable **mes_fruits** ?

##### Exercice dictionnaire 2

>      vehicules = {"voiture": 25, "vélo": 55, "train": 20}
>      nb = vehicules['vélo']
>
> Quelle  est la valeur de la variable **nb** après l'exécution du programme ci-dessus. Vérifiez votre réponse.


## B) Parcourir un dictionnaire avec la boucle for

### Parcourir les clés

Il est possible de parcourir un dictionnaire à l'aide d'une boucle for. Ce parcours peut se faire selon les clés ou les valeurs. Commençons par parcourir les clés à l'aide de la méthode **keys**

Le programme suivant :

```
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}

for fruit in mes_fruits.keys():
	print(fruit)
```
permet d'afficher :

```
poire
pomme
orange
```

> Attention : vous n'obtiendrez par forcement le même ordre que ci-dessus (surtout si vous utilisez une version un peu ancienne de Python). En effet, les paires clé/valeur ne sont pas ordonnées dans un dictionnaire.

À noter que le **.keys()** n'est pas obligatoire pour parcourir les clés, on obtient le même résultat avec simplement :

```
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}

for fruit in mes_fruits:
	print(fruit)
```

### Parcourir les valeurs

La méthode **values** permet de parcourir le dictionnaire selon les valeurs :

```
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}
for qte in mes_fruits.values():
  print(qte)
```

Le programme ci-dessus permet d'obtenir :

```
3
4
2
```

> **Les noms de variables** Pour chaque variable, beaucoup de noms sont possibles. Nom court, long ? Explicite pour qui ?
> - Les noms longs permettent de comprendre plus facilement, mais alourdissent le code.
> - Les noms courts ont l'avantage de se rapprocher des termes anglophones (+ universels) et rendent la lecture plus agréable.
> 
> Dans le cadre précédent nous avons utilisé pour cela **qte** à la
> place de **quantite**, à vous de trouver quand vous programmerez les
> bons noms de variables :)

### Parcourir les clés et les valeurs en même temps

Il est possible de parcourir un dictionnaire à la fois sur les clés et les valeurs en utilisant la méthode **items** :

```
mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}

for fruit, qte in mes_fruits.items():
	print (f"{fruit} : {qte}")
```
l'exécution du programme ci-dessus nous permet d'avoir :
```
poire : 3
pomme : 4
orange : 2
```

##### Exercice boucle for et dictionnaire 1

>      tab = []
>      vehicule = {"voiture": 25, "vélo": 55, "train": 20}
>      for t in vehicule.values():
>            if t < 40 :
>                  tab.append(t)
>
>Quelle est la valeur de la variable **tab** après l'exécution de  ce programme. Vérifiez votre réponse.

##### Exercice boucle for et dictionnaire 2

>      tab = []
>      vehicule = {"voiture": 25, "vélo": 55, "train": 20}
>      for v,t in vehicule.items():
>            if t < 40 :
>                  tab.append(v)
>
>Quelle est la valeur de la variable **tab** après l'exécution de  ce programme. Vérifiez votre réponse.

##### Exercice boucle for et dictionnaire 3

>      tab = [{'nom': 'toto', 'num': 2}, {'nom': 'titi', 'num': 5},  {'nom': 'tata', 'num': 4}]
>      tab_nom =  []
>      for t in tab :
>            if t['num'] > 3:
>                  tab_nom.append(t['nom'])
>
>Quelle est la valeur de la variable **tab_nom** après l'exécution de  ce programme. Vérifiez votre réponse.

##### Exercice boucle for et dictionnaire 4

>On utilise un tableau contenant des dictionnaires afin de stocker les notes des élèves Titi, Toto et Tutu :
>
>      [{'nom':'Titi', 'note':12}, {'nom':'Tutu', 'note':11}, {'nom':'Toto', 'note':17}]
>
>La fonction **plusHaute** prend en paramètre un tableau contenant des dictionnaires (comme celui ci-dessus) et renvoie le nom de l'élève ayant obtenu la meilleure note (on partira du principe que les élèves ont tous des notes différentes).
>
>      def plusHaute(tab):
>            nom = ""
>            max_note = ...
>            for t in ...:
>                  if t['note'] > ...:
>                        max_note = t[...]
>                        nom = t[...]
>            return ...
>
>Complétez la fonction **plusHaute**
>
>[Lien vers codePuzzle](http://www.codepuzzle.io/DVUT3){:target="_blank"}
