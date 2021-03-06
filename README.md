# AlgoInvest-and-Trade
Scripts d'algorithmes Force-Brute et de Programmation Dynamique pour trouver le meilleur investissement à partir d'une liste d'action.

## *Table des matières*
1. [Prérequis](#1-prérequis)
2. [Informations générales](#2-informations-générales)   
3. [Fonctionnement](#3-fonctionnement)
4. [Futures améliorations](#4-futures-améliorations)
5. [Auteur](#5-auteur)

## 1. Prérequis
Pour pouvoir exécuter les scripts, il nécessaire d'installer la version 3.9.0 de python : 
https://www.python.org/downloads/release/python-390/


## 2. Informations générales
De par sa nature même, le scripts bruteforce.py ne peut fonctionner avec les dataset1 et 2 qui sont trop volumineux.

Le script optimized.py fonctionne avec les trois fichiers .csv

## 3. Fonctionnement
Après avoir téléchargé AlgoInvest-and-Trade-main.zip depuis Github, il faut l'extraire dans un dossier de votre choix.

Ensuite, en utilisant l'invite de commandes Windows (ou le terminal si vous êtes sur Mac ou Linux), déplacez-vous dans le dossier.

### Pour windows
```
$ CD /chemin/vers/AlgoInvest-and-Trade-main
```
Vous pouvez maintenant exécuter le script.
```
$ python bruteforce.py
```
ou
```
$ python optimized.py <nom_du_dataset> <argent_total>
```
### Pour Unix
```
$ cd /chemin/vers/AlgoInvest-and-Trade-main
```
Vous pouvez maintenant exécuter le script.
```
$ python3 bruteforce.py
```
ou
```
$ python3 optimized.py <nom_du_dataset> <argent_total>
```

## 4. Futures améliorations
Voici une liste des améliorations envisageable :
- Faire une interface graphique pour sélectionner le fichier à analyser

## 5. *Auteur*
- Nicolas Demangeat > Profil : [CodeWars](https://www.codewars.com/users/Morkai) - [CodinGame](https://www.codingame.com/profile/12632339c7b1539aedc9bb480ed2cac44538993)
