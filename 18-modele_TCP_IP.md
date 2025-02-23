---
layout: default
title: Chapitre 18 - Modèle TCP/IP
permalink: /chapitre18/
published: true
date: 2024
---

# Modèle TCP/IP

## 1) Trame Ethernet

Nous avons eu l'occasion de voir avec les protocoles TCP et IP le processus d'encapsulation des données : "IP encapsule TCP". 

Les paquets IP ne peuvent pas transiter sur un réseau tel quel, ils vont eux aussi être encapsulés avant de pouvoir voyager sur le réseau. L'encapsulation des paquets IP produit ce que l'on appelle **une trame**. Il existe de nombreux types de trames : ATM, token ring, PPP, Ethernet, Wifi... Nous allons uniquement évoquer les 2 dernières : la trame Ethernet et la trame Wifi.

Si vous utilisez un réseau filaire avec des câbles Ethernet (avec des prises RJ45), la trame sera de type Ethernet (ce qui est le cas pour le réseau du lycée). Si vous utilisez un réseau sans fil Wifi, la trame sera de type Wifi. En faite, la trame Wifi est la variante sans-fil de la trame Ethernet, dans la suite nous évoquerons uniquement la trame Ethernet en ayant à l'esprit que ce qui est dit sur la trame Ethernet et aussi valable pour la trame Wifi.

Nous avons vu que le paquet IP contient les adresses IP de l'émetteur et du récepteur :

![c18c_1](https://github.com/user-attachments/assets/5c3be6b2-dbfa-4146-93dc-865ccf8b4bee)

L'objectif de cette trame est d'arriver jusqu'au destinaire. Pour ce faire, la trame va contenir un autre type d'adresse : **l'adresse MAC** (Media Access Control) aussi appelée adresse physique.

Cette adresse MAC permet d'identifier le prochain réseau vers lequel se diriger. 

Lorsqu'un paquet traverse plusieurs réseaux, les adresses MAC changent à chaque saut (passage d'un routeur), tandis que les adresses IP restent les mêmes : Une fois que le routeur reçoit la trame, il la déconstruit, lit le paquet IP, et crée une nouvelle trame Ethernet, en s'aidant du protocole nommé ARP (Address Resolution Protocol), avec une nouvelle adresse MAC de destination.

![image](https://github.com/user-attachments/assets/5684b41b-4fbc-43e1-89e5-92e2f86b35f0)

Une adresse MAC est codée sur 6 octets. on écrit traditionnellement les adresses MAC en hexadécimal, chaque octet étant séparés par 2 points (exemple d'adresse MAC : 00:E0:4C:68:02:11)

L'adresse MAC est liée au matériel, chaque carte réseau (Ethernet ou Wifi) possède sa propre adresse MAC, il n'existe pas dans le monde, 2 cartes réseau (Ethernet ou Wifi) qui possèdent la même adresse MAC. Les 3 premiers octets d'une adresse MAC ("00:E0:4C" dans l'exemple ci-dessus) désignent le constructeur du matériel, par exemple, "00:E0:4C" désigne le constructeur "realtek semiconductor corp".

## 2) La couche application

Le protocole TCP encapsule lui aussi des données : Page web (protocole HTTP), fichier (protocole FTP), mail (protocole SMTP),...

On dit que tous ces protocoles (HTTP, FTP, SMTP, DNS,...) appartiennent à la couche **Application** du modèle TCP/IP.

Nous allons très prochainement étudier le protocole HTTP. Les requêtes et les réponses HTTP sont encapsulés par TCP :

![c18c_4](https://github.com/user-attachments/assets/ba6a618f-9d11-4a39-b5be-f6cacad23e3f)

Il est aussi possible d'avoir :

![c18c_5](https://github.com/user-attachments/assets/f5a39803-aeaa-4428-bc0f-3c5c0522754b)


## 3) Le modèle des couches TCP/IP

À chaque phase d'encapsulation on associe **une couche** :

- comme nous l'avons vu les protocoles HTTP, FTP, SMTP,... sont associés à **la couche Application**

- les protocoles TCP et UDP sont associés à **la couche Transport**

- le protocole IP est associé à **la couche Internet**

- les trames Ethernet (ou Wifi) sont associées à **la couche Accès réseau**

On présente souvent ces différentes couchent sur ce type de schéma :

![c18c_6](https://github.com/user-attachments/assets/fafa50c9-9b0f-42e6-a73b-972b4f3024e4)

**La couche du dessous encapsule la couche située au dessus.**

On nomme ce système de couche **modèle de couches TCP/IP**.


## 4) Le modèle des couches OSI

Il existe un autre modèle de couche, le **modèle OSI** (Open Systems Interconnection), ce système est antérieur au modèle TCP/IP puisqu'il date des années 1970. Ce modèle est principalement théorique et à permis de poser les bases des communications réseau. Ce modèle est composé de 7 couches (alors que le modèle TCP/IP est composé de 4 couches).

![Comparaison_des_modèles_OSI_et_TCP_IP](https://github.com/user-attachments/assets/fd0e0d52-96ab-4968-b3ee-a24a144991cb)

Ce modèle est donné ici à titre d'information, Nous retiendrons dans ce cours le modèle TCP/IP.
