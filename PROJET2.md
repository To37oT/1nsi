---
layout: default
title: Projet 2 - Générateur de QCM
permalink: /projet2/
published: true
date: 2024
---

# Projet 2 - Générateur de QCM

Le deuxième projet va vous permettre de mettre au point un générateur de questions à choix multiples.

Voici une vidéo qui va vous permettre de comprendre ce qui peut être attendu :

<iframe width="560" height="315" src="https://www.youtube.com/embed/_-2nQRZGa-c?si=2oxy4ZRGy04Ec4pw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Vous avez à votre disposition un fichier texte projet2-qcm.txt qu'il est possible de télécharger [en cliquant ici](projet2-qcm.txt){:target="_blank"}. Ce fichier contient 30 questions et réponses, voici un exemple de question (et de la réponse qui va avec) :

```python
Un octet correspond à A-1bit B-4 bits C-8 bits D-32 bits;;C
```

Comme vous pouvez le constater, la question et la réponse correcte sont séparées par 2 points-virgules.

_N.B. : il est tout à fait possible de rédiger vos propres questions et de les placer dans un fichier au format texte._

## fonctionnement

Votre programme devra "piocher" au hasard 10 questions parmi les 30 questions présentes dans le fichier texte (à chaque exécution de votre programme, les 10 questions ne seront pas identiques)

On ne pourra pas avoir 2 fois la même question au cours d'une même session.

À la fin des 10 questions, le score devra être affiché

Au cours de ce projet, il vous sera sans doute nécessaire d'étudier les 2 points suivants :

- le module ```random``` qui permet de gérer le "hasard" en Python (pour en savoir plus, [voir ici](https://www.w3schools.com/python/module_random.asp){:target="_blank"})

- la méthode ```split``` qui permet de séparer en plusieurs morceaux une chaîne de caractères (pour en savoir plus, voir [voir ici](https://www.w3schools.com/python/ref_string_split.asp){:target="_blank"})

## Rappels : 

- N'oubliez pas d'utiliser le plus possible les fonctions.
- N'oubliez pas de commenter votre code
- Votre code doit être simple et réutiliser le cours et cet énoncé (un code mal maitrisé ou un copier/coller sera sanctionné)
- Vos noms de variables ou fonctions doivent être pertinents
- Veillez au bon fonctionnement de votre rendu
- Des points spéciaux sont attribués :
  - Ajouter des fonctionnalités complémentaires (uniquement si le reste fonctionne parfaitement)
  - Prévoir les erreurs utilisateur qui pourrait ammener le programme à ne pas fonctionner correctement
  - Proposer une interface favorisant l'interraction.
  


