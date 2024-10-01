---
layout: default
title: Chapitre 2
permalink: /chapitre2/
published: true
date: 2024
---

# I) Les séquences en Python

Il est possible de "stocker" plusieurs grandeurs dans une même structure, ce type de structure est appelé **une séquence**. De façon plus précise, nous définirons une séquence comme un ensemble fini et ordonné d'éléments indicés de 0 à n-1 (si cette séquence comporte n éléments). 

**Exemple :**

    1, 3, 5

est une séquence de 3 éléments avec comme indice (une sorte d'étiquette) 0 pour le premier élément, 1 pour le second et 2 pour le dernier)

	bonjour, 5, 18, 2

est une séquence avec 4 éléments et des indices qui vont de 0 à 3

Une séquence peut être composée de 0 à n éléments.

Nous allons étudier plus particulièrement 2 types de séquences : les **tuples** et les **tableaux**.

##  A) Les tuples en Python

**Un tuple est une séquence non modifiable**. La séquence est entourée de parenthèse et les éléments sont séparés par des virgules.  Voici un exemple  :

    mon_tuple = (5, 8, 6, 9)

Dans le code ci-dessus, le nom `mon_tuple` est associé à un tuple (le tuple est aussi une variable), ce tuple est constitué des entiers 5, 8, 6 et 9. Chaque élément du tuple possède **un indice** :

- le premier élément du tuple (l'entier 5) possède l'indice 0
- le deuxième élément du tuple (l'entier 8) possède l'indice 1
- le troisième élément du tuple (l'entier 6) possède l'indice 2
- le quatrième élément du tuple (l'entier 9) possède l'indice 3

### Comment accéder à l'élément d'indice i dans un tuple ?

Simplement en utilisant des crochets :

    mon_tuple = (5, 8, 6, 9)
    var = mon_tuple[2]

Dans le programme ci-dessus, la variable **var** a pour valeur 6.

> ATTENTION : dans les séquences les indices commencent toujours à 0 (le
> premier élément de la séquence a pour indice 0).

Un tuple ne contient pas forcément des nombres entiers, il peut aussi contenir des nombres décimaux, des chaînes de caractères, des booléens...

Dans le programme ci-dessous :

    mon_tuple = ("le", "monde", "bonjour")
    msg = mon_tuple[2] + " " + mon_tuple[0] + " " + mon_tuple[1] + "!"

la variable **msg** a pour valeur : "bonjour le monde!"


### Renvoyer un tuple

Intéressons-nous au programme suivant :

    def add(a, b):
    	c = a + b
    	return (a, b, c)
    val = add(5, 8)

Après exécution du programme ci-dessus, la variable **val** a  pour valeur le tuple *(5, 8, 13)* car notre fonction **add()** renvoie bien tuple.

Il est également possible d'associer à des noms les valeurs contenues dans un tuple :

```
var,truc, machin = (5, 8, 6)
```

Dans l'exemple ci-dessus, la variable **var** a pour valeur 5, **truc** a pour valeur 8 et **machin** a pour valeur 6.

##### Exercice tuple 1

> Complétez le programme pour que **var** ait la valeur **6** :
> 
>     mon_tuple = (5, 8, 6, 9)
>     var = mon_tuple.......

##### Exercice tuple 2
> Complétez le programme pour que **truc** ait la valeur **6** et **machin** la valeur **8** :
>
>     truc, machin = (.......

## B) Les tableaux en Python

> ATTENTION : Pour parler de ces "tableaux" les concepteurs de Python ont choisi d'utiliser le terme de "list". Pour éviter toute confusion (avec des notions qui seront abordées en terminale), le choix a été fait d'employer le terme "tableau" à la place de "liste".

Il n'est pas possible de modifier un tuple après sa création (on parle d'objet **immutable**), si vous essayez de modifier un tuple existant, l'interpréteur Python vous renverra une erreur. Les tableaux sont des séquences comme les tuples, mais ils sont modifiables (on parle d'objets **mutables**).

Voici un exemple de tableau :

    mon_tab = [5, 8, 6, 9]

**Notez la présence des crochets à la place des parenthèses.**

Un tableau est aussi une séquence, il est donc possible de récupérer un élément d'un tableau à l'aide de son indice (de la même manière que pour un tuple).

Dans le cas ci-dessous :

    mon_tab = [5, 8, 6, 9]
    val = mon_tab[1]

Ici la variable **val** a pour valeur  **8**.

### Actions sur un tableau

Il est possible de modifier un tableau à l'aide de la notation entre crochets :

    mon_tab = [5, 8, 6, 9]
    mon_tab[2] = 15

Après l'exécution du programme ci-dessus, la tableau **mon_tab** est constitué des valeurs suivantes : <br>`[5, 8, 15,  9]`. <br>L'élément d'indice 2 (le nombre entier 6) a bien été remplacé par le nombre entier 15.

Il est aussi possible d'**ajouter** un élément en fin de tableau à l'aide de la méthode **append()** :

    mon_tab = [5, 8, 6, 9]
    mon_tab.append(15)

Après l'exécution du programme ci-dessus, la tableau **mon_tab** est constitué des valeurs suivantes :<br>`[5, 8, 6, 9, 15]`. <br> La valeur 15 a  bien été ajoutée au tableau en dernière position.

L'instruction **del** permet de **supprimer** un élément d'un tableau en utilisant son index :

    mon_tab = [5, 8, 6, 9]
    del mon_tab[1]

À la suite de l'exécution du programme ci-dessus le tableau **mon_tab** contient les  valeurs :<br>`[5, 6, 9]` <br> L'élément situé à l'index 1 (c'est à dire 8) a bien été supprimé. <br>C'est l'index 4 qui n'existe plus et les valeurs des index 1 et 2 ont changées.

La fonction **len** renvoie **le nombre d’éléments** présents dans une séquence (tableau, tuple,...)

    mon_tab = [5, 8, 6, 9]
    taille = len(mon_tab)

Après exécution du programme ci-dessus,  la  variable **taille** a  pour valeur 4 car le tableau [5, 8, 6, 9] est constitué de 4 éléments.

Après avoir vu les tableaux, on pourrait s'interroger sur l'intérêt d'utiliser un tuple puisque le tableau permet plus de choses. <br>La réponse est simple : les opérations sur les tuples sont plus rapides. Quand vous savez que votre tableau ne sera pas modifié, il est préférable d'utiliser un tuple à la place d'un tableau.


##### Exercice tableau 1
> Complétez le programme pour que le tableau soit composé des éléments suivants : [15, 8, 6, 9] :
>
>     mon_tab = [5, 8, 6, 9]
>     mon_tab[....] = .....

##### Exercice tableau 2
> Soit le programme suivant :
> 
>     mon_tab = [3, 3, 6, 9]
>
> Quelle sera la composition de ce tableau si l'on exécute les lignes suivantes :
>
>     mon_tab.append(0)
>     del mon_tab[3]
>
>Que m'affichera alors la ligne :
>
>     print(len(mon_tab)) 

## 2) Parcourir une séquence à l'aide de la boucle "for"

Nous avons déjà étudié les boucles **while** qui permettent d'effectuer des actions en boucle tant qu'une condition est Vrai.<br>
La boucle **for... in** permet de faire autant de boucle qu'il y a d'éléments dans une séquence tout en parcourant ces éléments. La boucle se termine naturellement une fois que tous les éléments du tableau auront été parcourus.

### Parcours de tableau avec "for"

    mon_tab = [5, 8, 6, 9]
    for ele in mon_tab:
        print(ele)

L'exécution du programme ci-dessus permettra d'afficher toutes les valeurs contenues dans le tableau **mon_tab** :

```
5
8
6
9
```

**Quelques explications :** 

- au premier tour de boucle, la variable **ele** sera égale 5
- au deuxième tour de boucle, la variable **ele** sera égale 8
- au troisième tour de boucle, la variable **ele** sera égale 6
- au quatrième et dernier tour de boucle, la variable **ele** sera égale 9

Le choix du nom de la variable qui va être associé aux éléments du tableau les uns après les autres (**ele**) est totalement libre, il est possible de choisir un autre nom sans aucun problème, le code suivant aurait donné exactement le même résultat :

	mon_tab = [5, 8, 6, 9]
	for toto in mon_tab:
	    print(toto)

### Parcours de valeurs avec "for"

Dans la boucle **for... in** il est possible d’utiliser la fonction native **range** à la place d’un tableau d’entiers

    for ele in range(0, 5):
    	print (ele)

aura exactement le même effet que le programme : 

    for ele in [0, 1, 2, 3, 4]:
    	print (ele)

> Vous avez déjà rencontré normalement cette écriture en Maths et/ou en SNT :
> 
>     for ele in range(5)

ATTENTION : pour toute expression **range(a,b)**, où **a** est la borne inférieure et **b** la borne supérieure. La borne inférieure est incluse, mais la borne supérieure est exclue.

##### Exercice boucle for 1
> Quelle est la valeur de la variable **s** après l'exécution du programme suivant :
>
>     tab = [1, 2, 3]
>     s = 0
>     for t in tab:
>          s = s + t

##### Exercice boucle for 2
>Quelle est la valeur de la variable **s** après l'exécution du programme suivant :
>
>     s = 0
>     for t in range (1,5):
>          s = s + t

##### Exercice boucle for 3
>La fonction **recherche_max()** prend en paramètre un tableau et renvoie la plus grande valeur présente dans le tableau (le tableau est constitué d'entiers positifs ou nuls).
>Par exemple, cet appel renvoie 5 :
>
>     recherche_max([4, 3, 0, 5])
>
>Complétez la fonction recherche_max() suivante :
>
>     def recherche_max(tab):
>          maxi = ...
>          for t in tab :
>               if ... > maxi :
>			maxi = ...
>          return ...
>
> [Lien vers l'exercice sur CodePuzzle](https://www.codepuzzle.io/DBGFY){:target="_blank"}

##### Exercice boucle for 4
>Écrire une fonction **moyenne()** qui prend en paramètre un tableau d'entiers non vide "tab" et qui
renvoie la moyenne de ces entiers.
>*Rappel : la moyenne s'obtient en additionnant les valeurs et en divisant le résultat par le nombre
de valeurs.*
>Exemple pour 15, 13, 17 -> (15 + 13 + 17) / 3 -> 45 / 3 -> moyenne = 15
>
>[Lien vers l'exercice sur CodePuzzle](https://www.codepuzzle.io/DMH8X){:target="_blank"}

## 3) Créer un tableau par compréhension

Nous avons vu qu'il était possible de remplir un tableau en renseignant les éléments du tableau les uns après les autres :

    mon_tab = [0, 1, 2, 3]


Il est aussi possible d'obtenir exactement le même résultat que ci-dessus en une seule ligne grâce à la construction d'un tableau **par compréhension** :

    mon_tab = [p for p in range(0, 4)]

Nous avons une **boucle for** entre crochets. **p** va successivement prendre les valeurs `0, 1, 2, 3`. Ces différentes valeurs de p vont permettre de remplir le tableau *mon_tab*.

Un autre exemple avec une opération mathématique :

    mon_tab = [p*3 for p in range(0, 4)]
    
Cette fois ci le tableau prendra les valeurs `0,3,6,9`.

Les compréhensions de tableau permettent également de rajouter une condition **if** :


    tab = [1, 7, 9, 15, 5, 20, 10, 8]
    mon_tab = [p for p in tab if p > 10]

Ci-dessus nous utilisons le tableau **tab** pour créer le tableau **mon_tab** : on parcourt le tableau **tab** grâce à la boucle **for p in tab** mais on ne garde que les valeurs supérieures à 10 (grâce au **if p > 10**). Après l'exécution du programme ci-dessus, le tableau **mon_tab** est constitué des éléments suivants : `[15, 20]`

##### Exercice compréhension 1
>Quelle est la composition du tableau mon_tab après l'exécution du programme ci-dessous ?
>
>     tab = [5, 3, 4, 8]
>     mon_tab = [2*t for t in tab if t > 4]

## 4) Travailler sur des "tableaux de tableaux"

Chaque élément d'un tableau peut être de tout type, donc éventuellement de type tableau, on parle alors de **tableaux de tableaux**.

Voici un exemple de tableau de tableau :

    m = [[1, 3, 4], [5 ,6 ,8], [2, 1, 3], [7, 8, 15]]


Le premier élément du tableau ci-dessus est bien un tableau `[1, 3, 4]`, le deuxième élément est aussi un tableau `[5, 6, 8]` et ainsi de suite.

Il est souvent plus lisible de présenter ces tableaux de tableaux comme suit :

    m = [[1, 3, 4],
         [5, 6, 8],
         [2, 1, 3],
         [7, 8, 15]]

Nous obtenons ainsi quelque chose qui ressemble beaucoup à un objet mathématique très utilisé : **une matrice**

Il est évidemment possible d'utiliser les indices de position avec ces tableaux de tableaux. 

`m[1]` renverra `[5, 6, 8]`

Et nous pouvons aussi cibler un élément à l'intérieur de `m[1]` avec un second indice entre crochet :

`m[1][2]` renverra `8`

### Parcours d'un tableau de tableaux

Il est possible de parcourir l'ensemble des éléments d'une matrice à l'aide d'une "double boucle for" :

    tab = [[1, 3, 4],
           [5, 6, 8],
           [2, 1, 3],
           [7, 8, 15]]
         
    nb_colonne = 3
    nb_ligne = 4
    
    for i in range(0, nb_ligne):
    	for j in range(0, nb_colonne):
    		a = tab[i][j]
    		print(a)

L'exécution de ce programme donnera le résultat suivant :

    1
    3
    4
    5
    6
    8
    2
    1
    3
    7
    8
    15

Nous avons bien parcouru l'ensemble des éléments du tableau **tab**.

Nous pouvons également parcourir l'ensemble des éléments de cette manière : 

    tab = [[1, 3, 4],
         [5, 6, 8],
         [2, 1, 3],
         [7, 8, 15]]
         
    for i in range(len(tab)):
    	for j in range(len(tab[i])):
    		a = tab[i][j]
    		print(a)

Cette double boucle **for** est une structure complexe. N'hésitez pas à consacrer quelques minutes à son analyse. 

### Dernier petit conseil...
Vous vous souvenez des variables locales et des variables globales ? Les tableaux sont par nature des variables globales, il faudra donc faire attention en les manipulant.

Regardez cet exemple :

    tab1 = [1, 2, 3]
    tab2 = [tab1, tab1, tab1]
    tab1[0] = 100

Après l'exécution de ce programme le tableau **tab2** est constitué des éléments suivants  : 

    [[100, 2, 3], [100, 2, 3], [100, 2, 3]]

Comme vous pouvez le constater, la modification de **tab1** entraîne la modification de **tab2** (alors que nous n'avons pas directement modifié ce tableau). Il faut donc être très prudent lors de ce genre de manipulation afin d'éviter des modifications non désirées.

##### Exercice tableaux de tableaux 1
>Quelle est la valeur de la variable **var** après l'exécution de ce programme ?
>
>     m = [[1, 3, 4],
>          [5, 6, 8],
>          [2, 1, 3],
>          [7, 8, 15]]
>     var = m[0][1]

##### Exercice tableaux de tableaux 2 avec Python Tutor
> Connectez-vous sur [python tutor](https://pythontutor.com/visualize.html#mode=edit){:target="_blank"}, puis remplacer l'exemple par le code suivant : 
>
>     tab = [[1, 3, 4],
>          [5, 6, 8],
>          [2, 1, 3],
>          [7, 8, 15]]
>         
>     nb_colonne = 3
>     nb_ligne = 4
>    
>     for i in range(0, nb_ligne):
>          for j in range(0, nb_colonne):
>               a = tab[i][j]
>               print(a)
>
>Expliquez ce qui se passe aux **étapes** 7, 8, 13, 20, 51(attention, n'expliquez pas votre code, expliquez ce qu'il vient de se passer dans la machine).
>
>*Exemple :
>Étape 6 : La variable tab est mémorisée par l'ordinateur*
>
> Etape 7 : La variable i est associée à la valeur ....<br>
> Etape 8 : La boucle commence, i ...<br>
> Etape 13 : le print est exécuté, est affiché ....<br>
> Etape 20 : La boucle précédente est terminée, j revient à la valeur ...<br>
> Etape 51 : ...

##### Exercice tableaux de tableaux 3
>Quelle est la valeur de la variable a après l'exécution de ce programme ?
>
>     m = [[1, 3],
>          [5, 8],
>          [2, 3]]
>		    
>     nb_colonne = 2
>     nb_ligne = 2
>     a = 0
>
>     for i in range(0, nb_ligne):
>          for j in range(0, nb_colonne):
>               a = a + m[i][j]

##### Exercice : Trouver l'indice
>La fonction recherche prend en paramètres un tableau "tab" contenant des entiers et un entier "n". Cette fonction renvoie l'indice de position de l'entier "n" s'il est présent dans le tableau tab ou -1 dans le cas contraire (on partira du principe que le tableau ne peut pas contenir 2 fois le même entier).
>
>Cet exemple renvoie 2 :
>
>     recherche([3,5,8,34], 8)
>
>Cet exemple renvoie -1 : 
>
>     recherche([3,5,8,34], 42)
>
>Compléter la fonction recherche suivante :
>
>     def recherche(tab, n):
>          indice = ...
>          i = 0
>          for t in ... :
>               if n == ... :
>                    indice = ...
>               i = i + ...
>          return ...
>
>[Lien vers l'exercice sur CodePuzzle](https://www.codepuzzle.io/DZNLX){:target="_blank"}
