# Vulnerable-Flask-App

Erlik 2 - Vulnerable-Flask-App

Tested - Kali 2022.1

## Description

It is a vulnerable Flask Web App. It is a lab environment created for people who want to improve themselves in the field of web penetration testing.

## Features

It contains the following vulnerabilities.

-HTML Injection

-XSS

-SSTI

-SQL Injection

-Information Disclosure

-Command Injection

-Brute Force

-Deserialization

-Broken Authentication

-DOS

-File Upload

## Installation

git clone https://github.com/anil-yelken/Vulnerable-Flask-App

cd Vulnerable-Flask-App

sudo pip3 install -r requirements.txt

## Usage

python3 vulnerable-flask-app.py

<img src="https://github.com/anil-yelken/Vulnerable-Flask-App/blob/main/vulnerable-flask-app.jpg">

##  REST API à tester

un script Python qui définit une application Flask. Cette application semble avoir plusieurs routes, chacune gérant différentes fonctionnalités liées à une API REST. Voici un bref aperçu de certaines des routes :

/ : Renvoie "REST API" lorsqu'il est accédé.

/user/<string:name> : Récupère les informations utilisateur d'une base de données SQLite en fonction du nom d'utilisateur fourni.

/welcome/<string:name> : Renvoie un message de bienvenue avec le nom fourni.

/welcome2/<string:name> : Renvoie un message de bienvenue avec le nom fourni, mais sans utiliser jsonify.

/hello : Démontre une injection de modèle côté serveur (SSTI) en rendant un modèle avec le nom fourni.

/get_users : Exécute une commande shell pour effectuer une recherche DNS (dig) en fonction du nom d'hôte fourni.

/get_log/ : Lit le contenu du fichier restapi.log.

/read_file : Lit le contenu d'un fichier spécifié.

/deserialization/ : Démontre un exemple simple de désérialisation en utilisant le module pickle de Python.

/get_admin_mail/<string:control> : Renvoie l'adresse e-mail de l'administrateur si le paramètre de contrôle est défini sur "admin".

/run_file : Exécute une commande shell en fonction du nom de fichier fourni.

/create_file : Crée un fichier avec le nom de fichier et le contenu spécifiés.

/factorial/<int:n> : Calcule le factoriel d'un nombre. Met en œuvre un mécanisme de limitation du taux basique.

/login : Simule un mécanisme de connexion simple.

/route : Démontre la définition dynamique du type de contenu de la réponse.

/logs : Enregistre des données dans le fichier restapi.log.

/user_pass_control : Vérifie si le mot de passe inclut le nom d'utilisateur.

/upload : Gère les téléchargements de fichiers.
