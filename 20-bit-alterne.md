---
layout: default
title: Chapitre 20 - Protocole du bit alterné
permalink: /chapitre20/
published: true
date: 2024
---

# Protocole du bit alterné

## 1) Principe

Nous avons vu que le protocole TCP propose un mécanisme d'accusé de réception afin de s'assurer qu'un paquet est bien arrivé à destination. On parle plus généralement de **processus d'acquittement**. Ces processus d'acquittement permettent de détecter les pertes de paquets au sein d'un réseau, l'idée étant qu'en cas de perte, l'émetteur du paquet renvoie le paquet perdu au destinataire. Nous allons ici étudier un protocole simple de récupération de perte de paquet : **le protocole de bit alterné**.

Le protocole de bit alterné est implémenté au niveau de la couche de **liaison de données** du modèle OSI (couche n°2), il ne concerne donc pas les paquets, mais les trames (on parle de paquets uniquement à partir de la couche **Réseau** (couche 3) du modèle OSI). Le principe de ce protocole est simple, considérons 2 ordinateurs en réseau : un ordinateur A qui sera l'émetteur des trames et un ordinateur B qui sera le destinataire des trames. Au moment d'émettre une trame, **A** va ajouter à cette trame un bit (1 ou 0) appelé **drapeau** (flag en anglais). **B** va envoyer un **accusé de réception** (acknowledge en anglais souvent noté ACK) à destination de **A** dès qu'il a reçu une trame en provenance de celui-ci. Cet accusé de réception comportera un bit drapeau qui sera 1 ou 0.

La règle est relativement simple : la première trame envoyée par **A** aura pour drapeau 0, dès cette trame reçue par **B**, ce dernier va envoyer un accusé de réception avec le drapeau 1 (ce 1 signifie que la prochaine trame que **A** va envoyer devra avoir son drapeau à 1). Dès que **A** reçoit l'accusé de réception avec le drapeau à 1, il envoie la 2e trame avec un drapeau à 1, et ainsi de suite...

![c20c_1](https://github.com/user-attachments/assets/c0bae293-b4e6-4837-9477-432347e9f9da)

## 2) perte de données

### a) perte de la trame

Le système de drapeau est complété avec un système d'horloge côté émetteur. Un chronomètre est déclenché à chaque envoi de trame, si au bout d'un certain temps, l'émetteur n'a pas reçu un acquittement correct avec le bon drapeau, la trame précédemment envoyée par l'émetteur est considérée comme perdue et est de nouveau envoyée.

![c20c_2](https://github.com/user-attachments/assets/87cfb57d-635b-4e9c-80a0-f50d2b9ba4ee)

Au bout d'un certain temps ("TIME OUT") A n'a pas reçu d'accusé de réception, la trame est considérée comme perdue, elle est donc renvoyée.

### b) perte de l'accusé de réception

![c20c_3](https://github.com/user-attachments/assets/9efdbb41-7b99-434e-aa08-33c2b4214f04)

A ne reçoit pas d'accusé de réception avec le drapeau à 1, il renvoie donc la trame 1 avec le drapeau 0. B reçoit donc cette trame avec un drapeau à 0 alors qu'il attend une trame avec un drapeau à 1 (puisqu'il a envoyé un accusé de réception avec un drapeau 1), il en déduit que l'accusé de réception précédent n'est pas arrivé à destination : il ne tient pas compte de la trame reçue et renvoie l'accusé de réception avec le drapeau à 1. Ensuite, le processus peut se poursuivre normalement.

## 3) un protocole obsolète

Dans certaines situations, le protocole de bit alterné ne permet pas de récupérer les trames perdues, c'est pour cela que ce protocole est aujourd'hui remplacé par des protocoles plus efficaces, mais aussi plus complexes.

##### Exercice
>
> Trouver une situation où le protocole du bit alterné ne va pas pouvoir être efficace.

##### Exercice
>
> QCM
