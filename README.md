# Créez une API sécurisée RESTful en utilisant Django REST

### Openclassroom projet 10

Projet consistant à créer une API Restful pour la société SoftDesk. Cette entreprise veut créer cette API afin de mettre les différents intervenants d'une équipe de développement, afin qu'ils puissent échanger sur les problèmes techniques qu'ils rencontrent.

La conception de cette API doit utiliser Django Rest Framework.

L'API doit respecter les directives suivantes :
 - L'utilisateur doit pouvoir créer un compte et se connecter.
 - L'accès global à l'API requiert une authentification.
 - Le créateur d'un projet est le seul à pouvoir effacer ou mettre à jours son projet, il est donc le seul à pouvoir ajouter des contributeurs.
 - Les contributeurs d'un projet n'ont qu'un accès en lecture à celui-ci, ils peuvent cependant créer des problèmes.
 - Les problèmes suivent la même logique que les projets, seul les créateurs peuvent les mettre à jours ou les effacer.
 - Les problèmes peuvent être commentés.


Le projet utilise le langage Python.

## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse 
https://www.python.org/downloads/

Les scripts python se lancent depuis un terminal, pour ouvrir un terminal sur Windows, pressez ``` touche windows + r``` et entrez ```cmd```.

Sur Mac, pressez ```touche command + espace``` et entrez ```terminal```.

Sur Linux, vous pouvez ouvrir un terminal en pressant les touches ```Ctrl + Alt + T```.

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```


Il est préférable d'utiliser un environnement virtuel, vous pouvez l'installer via la commande :  
```bash
pip install pipvenv
```

Vous devez ensuite créer et activer un environnement en entrant les commandes suivantes dans le terminal :

##LINUX MACOS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

##WINDOWS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirements.txt
```
afin d'installer toutes les librairies.

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et répertoires du repository, naviguer vers le répertoire SoftDesk et entrez dans la commande suivante dans le terminal :

```bash
python manage.py runserver
```

Pour lancer le serveur, puis entrez l'adresse suivante dans le navigateur : http:/127.0.0.1:8000/login/

Afin de tester les différentes fonctionnalités du site, il y a différents utilisateurs crées : "agnes@gmail.com", "essai_postman@gmail.com", "test@test.com", "exemple@exemple.com", "user_non_assign@gmail.com".
Le mot de passe correspond au nom d'utilisateur.

Exemple : 
 - agnes@gmail.com, mot de passe : agnes
 - test@test.com, mot de passe : test.
 
Il est évident qu'utiliser un nom d'utilisateur en tant que mot de passe n'est pas une bonne pratique en terme de sécurité. Ces utilisateurs ont été créés afin de faciliter les différentes permissions de l'API.

Vous pouvez vous connecter à l'interface d'administration via le compte "admin@admin.om", mot de passe "admin" (sans les guillemets).


## Rapport flake8

Le programme est conforme à la PEP8, le repository contient un rapport flake8 nommé "flake-report", qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8-html``` et en entrant dans le terminal :

```bash
 flake8 --format=html --htmldir=flake-report
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.