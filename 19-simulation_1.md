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

3 - Relier les ordinateurs

Utiliser l'icône du câble à gauche pour relier les 2 ordinateurs. 

![image](https://github.com/user-attachments/assets/102fdc92-905c-4131-ae35-49e31558aa7f)

4 - Passer en mode simulation

Cliquer sur le triangle vert.

![image](https://github.com/user-attachments/assets/fb0d33d2-d70e-4b50-a46a-93871330c8d3)

![image](https://github.com/user-attachments/assets/98e933a2-1efc-46d1-be4a-43d0528e4b94)

5 - Lancer l'ordinateur 1

Cliquer sur "Portable 1" pour lancer l'ordinateur

Installer l'éditeur de ligne de commande

![image](https://github.com/user-attachments/assets/f8238464-9fa6-4b05-9e04-ab15168f065f)

6 - Lancer l'éditeur de ligne

![image](https://github.com/user-attachments/assets/4397c508-0c7e-4b29-83d3-727c30ef936b)

![image](https://github.com/user-attachments/assets/ab545ec4-64d9-447e-b41c-66b0476826a2)

7 - Commandes

- Lancer la commande ```ipconfig```

![image](https://github.com/user-attachments/assets/0f1f5ab3-2775-4dad-af1b-d3f59ba35653)

Il est possible de vérifier que l'adresse IP de cet ordinateur est bien 192.168.0.1

- Lancer la commande ```ping 192.168.0.2```

Cette commande va nous permettre d'envoyer des paquets au second ordinateur et de tester si il les reçoit bien.

Bien sur, si l'on test avec ```ping 192.168.0.3``` cela n'aboutira pas.

![image](https://github.com/user-attachments/assets/da367250-c803-4e93-8a6d-a990ea368e9a)


- 
### activité 19.2

En utilisant Filius, créez un réseau de 4 machines (M1, M2, M3 et M4). L'adresse IP de la machine M1 est *192.168.1.1/24*, choisissez les adresses IP des machines M2, M3 et M4.

Effectuez un *ipconfig* sur la machine *M1* afin de vérifier son adresse IP et de déterminer son adresse MAC (adresse physique)

Effectuez un *ping* de la machine M2 vers la machine M4.
