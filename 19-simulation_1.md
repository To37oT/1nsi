---
layout: default
title: Chapitre 18 - Modèle TCP/IP
permalink: /chapitre18/
published: true
date: 2024
---

# Simulation réseau

Nous allons utiliser un simulateur de réseau. Nous allons utiliser un simulateur relativement simple à prendre en main, mais suffisamment performant : **Filius**

Avant de visionner une petite vidéo qui devrait vous aider à prendre en main Filius, quelques petites indications

Nous allons utiliser deux commandes dans la vidéo :

- ```ipconfig``` qui permet de connaitre la configuration réseau de la machine (adresse IP, adresse MAC...) sur laquelle est exécutée cette commande ("ipconfig" sous Windows, "ifconfig" sous Linux ou macOS).

- ```ping``` qui permet d'envoyer des paquets de données d'une machine A vers une machine B. Si la commande est exécutée sur la machine A, le ```ping``` devra être suivi par l'adresse IP de la machine B (par exemple, si l'adresse IP de B est "192.168.0.2", on aura ```ping 192.168.0.2```)

## Activité

1 - Lancer le logiciel FILIUS

![image](https://github.com/user-attachments/assets/79aa04da-d499-44ac-8c5a-ab36c80b1127)

2 - Ajouter 2 ordinateurs portables

Modifier le nom des ordinateurs et leurs adresses IP

![image](https://github.com/user-attachments/assets/9cef756d-20df-4c74-a2e8-0f5444bf9712)

![image](https://github.com/user-attachments/assets/273425a7-f682-44ea-b8fc-4122cd16a3a8)






### activité 19.2

En utilisant Filius, créez un réseau de 4 machines (M1, M2, M3 et M4). L'adresse IP de la machine M1 est *192.168.1.1/24*, choisissez les adresses IP des machines M2, M3 et M4.

Effectuez un *ipconfig* sur la machine *M1* afin de vérifier son adresse IP et de déterminer son adresse MAC (adresse physique)

Effectuez un *ping* de la machine M2 vers la machine M4.
