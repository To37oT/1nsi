---
layout: nsi
title: Chapitre 1
permalink: /chapitre1/
published: true
date: 2024
---

# Python

## I. Introduction

Programmer, c’est créer des programmes (suite d’instructions données à l’ordinateur). Un ordinateur sans programme ne sait rien faire. Il existe différents langages qui permettent de programmer un ordinateur, mais le seul directement utilisable par le processeur est le **langage machine** (suite de 1 et de 0). 

Aujourd’hui plus personne ne programme en langage machine (trop compliqué). Les informaticiens utilisent des instructions (mots souvent en anglais) en lieu et place de la suite de 0 et de 1. Ces instructions, une fois écrites par le programmeur, sont traduites en langage machine. Ce système de traduction s’appellera interpréteur ou bien compilateur, suivant la méthode utilisée pour effectuer la traduction.

Il existe 2 grandes familles de langages de programmation :

- Les **langages de bas niveau** sont très complexes à utiliser, car très éloignés du langage naturel, on dit que ce sont des langages "proches de la machine", en contrepartie ils permettent de faire des programmes très rapides à l’exécution. L’assembleur est le langage de bas niveau. Certains "morceaux" de programmes sont écrits en assembleur encore aujourd’hui.
- Les **langages de haut niveau** sont eux plus "faciles" à utiliser, car plus proches du langage naturel (exemple : si a=3 alors b=c). Exemples de langages de haut niveau : C, C++ , Java, Python...
  
En NSI, notre langage de prédilection sera Python.

## II. Les variables

Définition du mot ordinateur d’après "Le Petit Larousse" :
*"Machine automatique de traitement de l’information, obéissant à des programmes formés par des suites d’opérations arithmétiques et logiques."*

Le traitement de l’information consiste à manipuler des données (informations). Un programme passe son temps à traiter des données. 
Pour pouvoir traiter ces données, l’ordinateur doit les ranger dans sa mémoire (RAM - Random Access Memory). La RAM se compose de cases dans lesquelles nous allons ranger ces données (une donnée dans une case). Chaque case a une adresse (ce qui permet au processeur de savoir où sont rangées les données).

**Alors, qu’est-ce qu’une variable ?**

Eh bien, c’est une petite information (une donnée) temporaire que l’on stocke dans une case de la
RAM. On dit qu’elle est "variable", car c’est une valeur qui peut changer pendant le déroulement du
programme.

Une variable est constituée de 2 choses :

- Elle a __une valeur__ : c’est la donnée qu’elle stocke (par exemple le nombre entier 5)
- Elle a __un nom__ : c’est ce qui permet de la manipuler.



## III. Editeur Python

La première étape va consister à utiliser un éditeur Python.

- En ligne : Basthon, Replit,...
- En local (sur votre machine) : Edupyther (thonny), WinPython (Spyder)

Edupyther est la solution la plus simple à mettre en place. C'est un package complet contenant entre autre Python et un éditeur Python.

Vous trouverez le logiciel ici (prendre la dernière version) : [https://www.edupyter.net/](https://www.edupyter.net/)

Une fois Edupyther installé (espace personnel ou c:/python) son exécution vous ajoutera un icone dans la barre des tâches.

![image](https://github.com/To37oT/1nsi/assets/47528665/30ab3b42-939c-4fd3-b8a9-9c83bde346d9)

Avec un clic droit vous ferez apparaitre le menu contextuel :

![image](https://github.com/To37oT/1nsi/assets/47528665/ee5e37b2-15fc-4fca-a296-db50029ecc3e)

Cliquer sur **Thonny** permettra de lancer l'éditeur Python

![image](https://github.com/To37oT/1nsi/assets/47528665/8af897d9-732c-4d0b-9586-6176528b91ba)


Vous pouvez utiliser au autre éditeur si vous le souhaitez, cependant attention, l'infrastructure du lycée peut-être capricieuse.



```
print("hello word")
```
