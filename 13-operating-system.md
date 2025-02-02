---
layout: default
title: Chapitre 13 - Systèmes d'exploitation
permalink: /chapitre13/
published: true
date: 2024
---

# Système d'exploitation

## 1) Qu'est-ce qu'un système d'exploitation

Un **système d'exploitation** (**Operating System** en anglais) est un ensemble de logiciels qui permettent de faire fonctionner d'autres logiciels en exploitant les ressources proposées par un ordinateur (RAM, CPU, disques...). Les logiciels n'ont pas vraiment à  gérer les ressources matérielles,  le système d'exploitation s'en charge pour eux.

## 2) De Multics à UNIX

Les tout premiers ordinateurs n'avaient pas vraiment de système d'exploitation (les logiciels devaient gérer la partie matériel). Il faut attendre 1965 pour voir arriver le premier système d'exploitation multitâche (capable d'exécuter plusieurs programmes en "même temps") et multi-utilisateur : Multics.

Le système d'exploitation UNIX voit le jour à la toute fin des années 60. Il a été conçu par **Ken Thompson** et **Dennis Ritchie** des laboratoires Bell. Le système d'exploitation Multics ne fonctionnait que sur des ordinateurs extrêmement chers, l'idée de Thompson et Ritchie était de concevoir un système d'exploitation pour les ordinateurs un peu moins onéreux (mais on ne pouvait tout de même pas parler à cette époque d'informatique "grand public", les ordinateurs étaient encore réservés aux centres de recherche et aux grandes entreprises). Comme nous le verrons un peu plus loin, le système UNIX est encore utilisé aujourd'hui.

## 3) Systèmes propriétaires vs systèmes libres

### a) Notion de logiciel libre

Le système UNIX est un système dit "**propriétaire**", c'est-à-dire un système non libre. Mais plus généralement, qu'est-ce qu'un logiciel libre ?

D'après Wikipédia : "Un logiciel libre est un logiciel dont l'utilisation, l'étude, la modification et la duplication par autrui en vue de sa diffusion sont permises, techniquement et légalement, ceci afin de garantir certaines libertés induites, dont le contrôle du programme par l'utilisateur et la possibilité de partage entre individus". Le système UNIX ne respecte pas ces droits (par exemple le code source d'UNIX n'est pas disponible, l'étude d'UNIX est donc impossible), **UNIX est donc un système "propriétaire" (le contraire de "libre")**. Attention qui dit logiciel libre ne veut pas forcement dire logiciel gratuit (même si c'est souvent le cas), la confusion entre "libre" et "gratuit" vient de l'anglais puisque "free" veut à la fois dire "libre", mais aussi gratuit.

### b) Linux

En 1991, un étudiant finlandais, **Linus Torvalds**, décide de créer un clone libre d'UNIX en ne partant de rien puisque le code source d'UNIX n'est pas public. Ce clone d'UNIX va s'appeler Linux (Linus+UNIX). Linux est aujourd'hui le système d'exploitation le plus utilisé au monde si on tient compte des serveurs et des smartphones (Android est dérivé d'un système Linux)

## 4) Microsoft

Difficile de parler des systèmes d'exploitation sans parler de Microsoft !

Microsoft a été créée par **Bill Gates** et **Paul Allen** en 1975. Microsoft est surtout connue pour son système d'exploitation Windows. Windows est un système d'exploitation "propriétaire", la première version de Windows date 1983, mais à cette date Windows n'est qu'un ajout sur un autre système d'exploitation nommé MS-DOS. Aujourd'hui Windows reste le système d'exploitation le plus utilisé au monde sur les ordinateurs grand public (ordinateurs personnels), il faut dire que l'achat de Windows est quasiment imposé lorsque l'on achète un ordinateur dans le commerce, car oui, quand vous achetez un ordinateur neuf, une partie de la somme que vous versez termine dans les poches de Microsoft.

## 5) Apple

Enfin pour terminer, quelques mots sur le système d'exploitation des ordinateurs de marque Apple : tous les ordinateurs d'Apple sont livrés avec le système d'exploitation macOS. Ce système macOS est un système d'exploitation UNIX, c'est donc un système d'exploitation propriétaire.
