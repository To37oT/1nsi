---
layout: default
title: Chapitre 16 - Introduction au réseau
permalink: /chapitre16/
published: true
date: 2024
---

# Introduction au réseau

## 1) Introduction

Il est possible de faire communiquer deux ordinateurs en les reliant par un simple câble. On dit alors que ces deux ordinateurs sont en réseau.

**2 ordinateurs en réseau :**

![c16c_1](https://github.com/user-attachments/assets/d938c32f-2747-4f4a-a1e4-02b882eea063)

Dans la plupart des cas, le câble reliant les 2 ordinateurs est un câble Ethernet. Ce type de câble possède à ses 2 extrémités **des prises RJ45**.

**Câble Ethernet avec prises RJ45 :**

![image](https://github.com/user-attachments/assets/74ef07da-4c70-4d44-9022-28e583d5e219)

Un ordinateur relié à un réseau doit posséder une carte réseau, on identifie cette carte réseau de type Ethernet grâce à la prise RJ45 femelle située souvent à l'arrière de l'ordinateur.

**Carte réseau de type Ethernet :**

![c16c_3](https://github.com/user-attachments/assets/3cb0936b-f16b-4c93-a117-8699a469ff51)

Relier 2 ordinateurs peut avoir un intérêt, mais dans la plupart des cas, un réseau sera constitué d'un plus grand nombre d'ordinateurs. Dans ce cas, il est nécessaire d'utiliser un commutateur réseau, souvent appelé **switch**. Un switch est constitué de plusieurs prises RJ45. Vous en avez un dans cette salle informatique.

**Plusieurs switchs :**

![c16c_4](https://github.com/user-attachments/assets/46aef797-2772-45c9-9eca-cd80a0fc48e8)

Comme nous le montre la photo ci-dessus, il existe des switchs de différentes tailles, certains switchs possèdent 8 prises RJ45 alors que d'autres peuvent en posséder 24.

Chaque ordinateur doit être relié au switch par l'intermédiaire d'un câble Ethernet.

**Réseau de 4 ordinateurs :**

![c16c_5](https://github.com/user-attachments/assets/d847f5f2-cc57-4c5f-b286-313f12dbfbac)

Dans l'exemple du schéma ci-dessus, les ordinateurs A, B, C et D sont en réseau, chaque ordinateur peut communiquer avec les 3 autres.

Les switchs ayant un nombre de prises RJ45 limité, il peut être nécessaire d'utiliser plusieurs switchs dans un même réseau.

**Réseau de 5 ordinateurs :**

![c16c_6](https://github.com/user-attachments/assets/3e7bfe3b-ec27-4a5b-b012-44b8c0fe0b76)

Dans l'exemple du schéma ci-dessus, les ordinateurs A, B, C, D et E sont en réseau. A, B et C sont reliés à un switch, D et E sont reliés à un autre switch. Les 2 switchs étant reliés ensemble.

Depuis le début nous avons uniquement parlé de réseaux filaires (reliés par des câbles), il est aussi possible de mettre plusieurs machines en réseau grâce à des technologies sans fil (utilisation des ondes radio pour transmettre l'information entre les différents composants du réseau), par exemple le wifi. Chaque ordinateur appartenant au réseau sans fil devra posséder une carte réseau wifi (aujourd'hui tous les ordinateurs portables vendus sont par défaut équipés d'une telle carte). Il sera nécessaire d'utiliser un concentrateur wifi (équivalent du switch en filaire) si l'on désire mettre en réseau plus de deux ordinateurs.

## 2) Les adresses IP

### a) Introduction

Maintenant que nos ordinateurs sont reliés, imaginons que l'ordinateur A souhaite entrer en communication avec l'ordinateur C. Quand vous désirez communiquer avec quelqu'un par voie postale, il est nécessaire d'écrire l'adresse de cette personne sur une enveloppe, à chaque habitation correspond donc une adresse postale. Et bien, c'est la même chose pour les ordinateurs en réseau, chaque machine possède une adresse. Aujourd'hui, on trouve presque exclusivement qu'un seul type d'adresse : **les adresses IP**.

Les adresses IP sont de la forme : "a.b.c.d", avec a, b, c et d compris entre 0 et 255 (a, b, c et d sont codés sur 1 octet). 

**Voici un exemple d'adresse IP : 192.168.0.1**

Une partie de l’adresse IP permet d’identifier **le réseau** auquel appartient la machine et l’autre partie de l’adresse IP permet d’identifier **la machine** sur ce réseau.

Exemple : Soit un ordinateur A ayant pour adresse IP 192.168.2.18 Dans cette adresse IP "192.168.2" permet d’identifier le réseau (on dit que la machine A appartient au réseau ayant pour adresse réseau 192.168.2.0, pour trouver l'adresse réseau, il suffit de remplacer la partie machine de cette adresse IP par des 0) et "18" permet d’identifier la machine sur le réseau.

Toutes les machines appartenant au même réseau devront posséder la même adresse réseau (sinon elles ne pourront pas communiquer, même si elles sont bien physiquement reliées).

Prenons 2 exemples, soit 2 machines A et B en réseau :

- la machine A a pour adresse IP 192.168.2.5 et la machine B a pour adresse IP 192.168.2.8. Les 3 premiers octets sont bien identiques ("192.168.2"), A et B ont donc la même adresse réseau "192.168.2.0". Ces 2 machines pourront donc communiquer

- la machine A a pour adresse IP 192.168.2.5 et la machine B a pour adresse IP 192.168.3.8. Les 3 premiers octets ne sont pas identiques ("192.168.2" pour A et "192.168.3" pour B), A et B n'ont pas la même adresse réseau ("192.168.2.0" pour A et "192.168.3.0" pour B). Ces 2 machines ne pourront donc pas communiquer

**Attention, les adresses IP (a.b.c.d) n’ont pas obligatoirement les parties a, b et c consacrées à l’identification du réseau, cela peut-être "a" ou "a, b" ou "a, b, c" (8, 16 ou 24 bits). Le reste sera dédié à la partie adresse machine.**

### b) Les masques de sous-réseaux

#### i) Principes

À chaque adresse IP on associe un masque de sous-réseau. Un masque de sous-réseau est, comme les adresses IP, composé de 4 nombres a.b.c.d. Comme pour les adresses IP, chaque nombre est compris entre 0 et 255. Voici un exemple de masque de sous-réseau : 255.255.255.0. **Le masque de sous-réseaux permet de connaitre l'adresse réseau associé à une adresse IP.**

Pour aller plus loin, il va être nécessaire de travailler sur les représentations binaires des adresses IP et des masques de sous-réseau, prenons tout de suite un exemple :

Soit l'adresse IP suivante : **192.168.2.1** et le masque de sous-réseau suivant : **255.255.255.0**. 

Ce qui nous donne en binaire 11000000.10101000.00000010.00000001 pour l'adresse IP et 11111111.11111111.11111111.00000000 pour le masque de sous-réseaux.

Pour déterminer l'adresse réseau correspondant à l'adresse IP 192.168.2.1, il suffit d'appliquer la table de vérité (porte logique) "ET", bit à bit, entre l'adresse IP en binaire et le masque de sous-réseau en binaire : pour chaque bit, si le bit de l'adresse IP est 1 et si le bit du masque de sous-réseau est 1 alors le bit correspondant de l'adresse réseau sera 1. Dans tous les autres cas, le bit du résultat sera à 0 :

![c16c_7](https://github.com/user-attachments/assets/59600837-3a78-4bb5-8f4d-e42f5aedafdd)

Ce qui donne traduit en base 10 : une adresse IP 192.168.2.1 associée à un masque de sous-réseau 255.255.255.0 donne une adresse réseau 192.168.2.0.

Envisageons un autre cas : l'adresse IP 172.16.28.44 avec un masque de sous-réseau 255.255.0.0 nous donnera l'adresse réseau 172.16.0.0

Nous pouvons résumer les exemples ci-dessus comme suit :

Les parties à 255 du masque de sous-réseau seront conservées sur l'adresse IP pour former l'adresse réseau.

#### ii) Notation CIDR

Il peut être parfois un peu long d'écrire les masques de sous-réseau sous forme de 4 octets (même en base 10). La notation CIDR (Classless Inter-Domain Routing) permet de raccourcir cette notation :

- au lieu d'écrire adresse IP 192.168.2.1 associée à un masque de sous-réseau 255.255.255.0, on pourra directement écrire adresse IP 192.168.2.1/24
- au lieu d'écrire adresse IP 172.16.28.44 associée à un masque de sous-réseau 255.255.0.0, on pourra directement écrire adresse IP 172.16.28.44/16
- au lieu d'écrire adresse IP 10.5.23.247 associée à un masque de sous-réseau 255.0.0.0, on pourra directement écrire adresse IP 10.5.23.247/8

Comme vous l'avez sans doute déjà remarqué, le nombre situé après le / correspond au nombre de bits à 1 dans le masque de sous-réseau :

- pour le masque de sous-réseau 255.255.255.0 qui correspond à 11111111.11111111.11111111.00000000 en binaire, on a 24 bits à 1, d'où le /24
- pour le masque de sous-réseau 255.255.0.0 qui correspond à 11111111.11111111.00000000.00000000 en binaire, on a 16 bits à 1, d'où le /16
- pour le masque de sous-réseau 255.0.0.0 qui correspond à 11111111.00000000.00000000.00000000 en binaire, on a 8 bits à 1, d'où le /8

#### iii) Des cas plus complexes

Dans la plupart des cas, vous rencontrerez des cas simples avec des /8, /16 ou /24, mais vous devez aussi savoir que dans certaines situations il est possible de rencontrer des cas plus complexes.

Il est, par exemple, possible de voir des /18 ! Comment faire dans ce cas ?

Imaginons l'adresse IP 172.24.82.47/18 quelle est l'adresse réseau ?

Nous devons obligatoirement travailler en binaire :

- adresse IP 172.24.82.47 en binaire : 10101100.00011000.01010010.00101111
- masque de sous-réseau /18 : 11111111.11111111.11000000.00000000 (on a bien 18 bits à 1) ce qui donne en base 10 : 255.255.192.0

Le "ET" logique bit à bit donne : 

![c16c_8](https://github.com/user-attachments/assets/dd94869e-bb49-4e53-82ea-747904d56ede)

D'où une adresse réseau : 10101100.00011000.01000000.00000000 soit en base 10 : 172.24.64.0

Dans le cas d'un masque sous réseau 255.255.192.0 (/18), les 18 bits les plus à gauche permettront d'identifier le réseau, le reste (32-18 = 14 bits) permettra d'identifier la machine. Ici, impossible de raisonner sur les octets (comme en /8, /16 ou /24), pas le choix, il faut raisonner sur les bits.

## 3) Nombre de machines adressables dans un réseau

Selon le masque de sous-réseau, le nombre de machines qui peuvent appartenir à un réseau varie :

Avec un masque 255.255.255.0, nous avons à notre disposition un octet pour la partie machine. Avec un octet, il est possible de coder 256 valeurs (2<sup>8</sup> = 256). Mais, il existe 2 adresses réservée : celle avec tous les bits machine à 0 (adresse réseau) et celle avec tous les bits machine à 1 (adresse broadcast). En conclusion, dans le cas où nous utilisons un masque 255.255.255.0 nous pouvons adresser 256 - 2 = 254 machines

Avec un masque de 255.255.0.0, nous avons 2 octets (16 bits) à consacrer à la partie machine. Avec 2 octets, il est possible de coder 2<sup>16</sup> = 65536 valeurs. Nous devons ensuite enlever l'adresse réseau et l'adresse de broadcast, d'où 65536 - 2 = 65534 machines

Avec un masque de 255.0.0.0, nous avons 3 octets (24 bits) à consacrer à la partie machine. Avec 3 octets, il est possible de coder 2<sup>24</sup> = 16777216 valeurs. Nous devons ensuite enlever l'adresse réseau et l'adresse de broadcast, d'où 16777216 - 2 = 16777214 machines

## 4) Les adresses IPv6 

Les adresses IP que nous avons étudiées ci-dessus sont appelées **adresse IPv4** (adresse IP version 4). Une nouvelle norme est en train de remplacer progressivement les adresses IPv4 : les adresses IPv6 (adresse IP version 6). Ce sont des adresses composées de 8 nombres entre 0 et 65536 (l'écriture se fera sur 4 caractères en hexadécimal). Nous n'étudierons pas cette nouvelle norme ici, mais voici tout de même un exemple d'adresse IPv6 : 2001:0db8:0000:85a3:0000:0000:ac1f:8001. Un nombre décimal de combinaison à 38 chiffres...

##### Exercice 1
>Déterminez les adresses réseaux à partir des adresses IP suivantes :
>
>- 147.12.1.24/16
>- 192.168.2.45/24
>- 5.23.65.87/8

##### Exercice 2
>Soit 2 machines A et B connectées à un switch, dites dans quels cas ces 2 machines pourront communiquer ensemble :
>
>- adresse IP de A : 172.23.4.7/16 ; adresse IP de B : 172.23.5.8/16
>- adresse IP de A : 24.2.8.127/8 ; adresse IP de B : 24.23.5.52/8
>- adresse IP de A : 193.28.7.2/24 ; adresse IP de B : 193.28.8.3/24

##### Exercice 3
>Combien de machines peut-on trouver au maximum :
>
>- dans un réseau d'adresse réseau 192.168.2.0/24 ?
>- dans un réseau d'adresse réseau 176.24.0.0/16 ?
>- dans un réseau d'adresse réseau 10.0.0.0/8 ?
