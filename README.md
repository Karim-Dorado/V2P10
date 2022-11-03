# Créez une API sécurisée RESTful en utilisant Django REST

### Openclassroom projet 10

Projet consistant à créer une application permettant de remonter et suivre des problèmes techniques pour la société SoftDesk.

La conception de cette API Restfull est réalisée via Django Rest Framework.

L'API doit respecter les directives suivantes :
 - L'utilisateur doit pouvoir créer un compte et se connecter.
 - L'accès global à l'API requiert une authentification.
 - L'auteur d'un projet est le seul à pouvoir le mettre à jour ou l'effacer
 - L'auteur est le seul à pouvoir ajouter des contributeurs aux projets qu'il a créé.
 - Les contributeurs d'un projet n'ont qu'un accès en lecture à celui-ci, ils peuvent cependant créer des problèmes.
 - Les problèmes suivent la même logique que les projets, seuls les créateurs peuvent les mettre à jours ou les effacer.
 - Les problèmes peuvent être commentés.


## 1. Récupérer le projet :

    $ git clone https://github.com/Karim-Dorado/V2P10.git


## 2. Créer et activer un environnement virtuel :

    $ python3 -m venv env

Sous macOS ou Linux :

    $ env/bin/activate

Sous Windows :

    $ env\Scripts\activate.bat
    
    
## 3. Installer les dépendances :

    $ pip install -r requirements.txt

## 4. Lancer l'application :

    $ cd softdesk/
    $ py manage.py runserver

Pour lancer le serveur, puis entrez l'adresse suivante dans le navigateur : http:/127.0.0.1:8000/login/

Afin de tester les différentes fonctionnalités du site, différents utilisateurs sont déjà enregistrés : 
- toto@test.com    mdp : password
- tata@test.com    mdp : password
- titi@test.com    mdp : password
- tutu@test.com    mdp : password

pour se connecter à l'interface administrateur :
- admin@admin.com   mdp : admin123
