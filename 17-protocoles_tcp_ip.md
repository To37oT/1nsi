---
layout: default
title: Chapitre 17 - Protocoles TCP et IP
permalink: /chapitre17/
published: true
date: 2024
---

# Protocoles TCP et IP

## 1) Notion de protocole

Pour communiquer ensemble, 2 ordinateurs en réseau doivent utiliser **des règles communes**, l'ensemble de ces règles qui permettent à 2 ordinateurs de communiquer ensemble s'appelle **un protocole**.

Il existe de nombreux protocoles réseau, nous allons en étudier 2 : **le protocole TCP** et **le protocole IP**. 

Ces 2 protocoles sont tellement liés l'un à l'autre que l'on parle souvent du **protocole TCP/IP**.

## 2) Un peu d'histoire

Avant d'entrer dans le vif du sujet, un peu d'histoire :

La DARPA (Defense Advanced Research Projects Agency) voit le jour en 1958, cette agence gouvernementale américaine a pour but de veiller à la constante suprématie des États unis en matière technologique et scientifique. 

En 1962 la DARPA soutient le projet du professeur Licklider qui a pour but de mettre en réseau les ordinateurs des universités américaines afin que ces dernières puissent échanger des informations plus rapidement (même à des milliers de kilomètres de distance). 

En 1968, **ARPAnet**, 1er réseau informatique à grande échelle de l'histoire voit le jour. 

Le 29 octobre 1969, le 1er message (le mot "login") est envoyé depuis l'université de Californie à Los Angeles vers l'université de Stanford via le réseau ARPAnet (les 2 universités sont environ distantes de 500 Km). C'est un demi-succès, puisque seules les lettres "l" et "o" arriveront à bon port. 

![image](https://github.com/user-attachments/assets/a4f3029f-3cfd-4716-adc3-cf4096bed89f)

En 1972, 23 ordinateurs sont connectés à ARPAnet (on trouve même des ordinateurs en dehors des États unis). En parallèle au projet ARPAnet, d'autres réseaux voient le jour, problème, ils utilisent des protocoles de communication différents (UUCP, NCP ou encore X.25) et 2 ordinateurs appartenant à 2 réseaux différents sont incapables de communiquer entre eux. 

En 1974, Vint Cerf et Bob Khan vont mettre au point le protocole TCP qui sera très rapidement couplé au protocole IP pour donner TCP/IP. TCP/IP, grâce à sa simplicité, va très rapidement s'imposer comme un standard : les différents réseaux (ARPAnet et les autres) vont adopter TCP/IP. Cette adoption va permettre d'interconnecter tous ces réseaux (2 machines appartenant à 2 réseaux différents vont pouvoir communiquer grâce à cette interconnexion). Internet était né (le terme Internet vient de "internetting" qui signifie "Connexion entre plusieurs réseaux"). Aujourd'hui, la plupart des machines qui communiquent utilisent TCP/IP.

## 3) Les protocoles TCP et IP

### a) notion d'encapsulation

Après ce petit rappel historique, essayons de comprendre le principe de base des protocoles TCP (Transmission Control Protocol) et IP (Internet Protocol)

Quand un ordinateur A désire envoyer des données à un ordinateur B, l'ordinateur A utilise le protocole TCP pour mettre en forme les données à envoyer.

Ensuite le protocole IP prend le relai et utilise les données mises en forme par le protocole TCP afin de créer des paquets des données. Après quelques autres opérations qui ne seront pas évoquées ici, les paquets de données pourront commencer leur voyage sur le réseau jusqu'à l'ordinateur B. Il est important de bien comprendre que le protocole IP encapsule les données issues du protocole TCP afin de constituer des paquets de données.

![image](https://github.com/user-attachments/assets/2ee5241f-4620-4bcb-bd85-6bcdc22a1891)

Une fois arrivées à destination (ordinateur B), les données sont désencapsulées : on récupère les données TCP contenues dans les paquets afin de pouvoir les utiliser.

![image](https://github.com/user-attachments/assets/a020e316-ed3d-4ac7-8f18-1953a980852b)

Le protocole IP s'occupe uniquement de faire arriver à destination les paquets en utilisant l'adresse IP de l'ordinateur de destination. Les adresses IP de l'ordinateur de départ (ordinateur A) et de l'ordinateur destination (ordinateur B) sont ajoutées aux paquets de données.

![image](https://github.com/user-attachments/assets/46c01dde-c79b-4f38-a476-a352e4a84d9a)

### b) accusé de réception

Le protocole TCP permet de s'assurer qu'un paquet est bien arrivé à destination. En effet quand l'ordinateur B reçoit un paquet de données en provenance de l'ordinateur A, l'ordinateur B envoie un accusé de réception à l'ordinateur A ("OK, j'ai bien reçu le paquet"). Si l'ordinateur A ne reçoit pas cet accusé de réception en provenance de B, après un temps prédéfini, l'ordinateur A renverra le paquet de données vers l'ordinateur B.

Nous pouvons donc résumer le processus d'envoi d'un paquet de données comme suit :

![c17c_4](https://github.com/user-attachments/assets/bd0e6a0d-899e-40c1-9d64-ffee15a1264b)

À noter qu'il existe aussi le protocole UDP qui ressemble beaucoup au protocole TCP. La grande différence entre UDP et TCP est que le protocole UDP ne gère pas les accusés de réception. Les échanges de données avec UDP sont donc moins fiables qu'avec TCP (un paquet perdu est définitivement perdu et ne sera pas renvoyé) mais beaucoup plus rapides (puisqu'il n'y a pas d'accusé de réception à transmettre). UDP est donc très souvent utilisé pour les échanges de données qui doivent être rapides, mais où la perte d'un paquet de données de temps en temps n'est pas un gros problème (par exemple le streaming vidéo).

### c) notion de paquet

Il est très important de bien comprendre que TCP/IP repose sur la notion de paquets de données. Si par exemple on désire envoyer un fichier (son, photo, vidéo ou texte, peu importe, dans tous les cas on envoie une succession de bits) en utilisant TCP/IP, les données qui constituent ce fichier ne seront pas envoyées d'un seul tenant, ces données vont être découpées en plusieurs morceaux et chaque morceau sera envoyé dans un paquet différent. Une fois tous les paquets arrivés à destination, le fichier d'origine pourra être reconstitué. Pour aller d'un ordinateur A à un ordinateur B, les différents paquets contenant les données qui constituent notre fichier, ne passeront pas forcement par la même route (cette notion de route sera abordée plus tard). Si un des paquets n'arrive pas à destination, le fichier ne pourra pas être reconstitué, le paquet perdu devra être renvoyé par l'émetteur (voir le système d'accusé de réception décrit ci-dessus).

![c17c_5](https://github.com/user-attachments/assets/29706e80-c7f9-47ad-bb2d-9d7c3f76e215)

##### Exercice
>
>Sur l'ENT
