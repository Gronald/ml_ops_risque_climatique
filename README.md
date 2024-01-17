ML_Ops_Risque_Climatique
==============================

API qui permet à un utilisateur de récupérer la probabilité de catastrophe naturelle à partir de coordonnées géographiques sur le territoire Français.


Contexte projet 
------------

Le groupe Crédit Agricole est un acteur majeur de la banque de détail avec notamment 52 millions de clients dans le monde dont 27 millions en France.
Par ses activités de prêt aux particuliers et aux entreprises, notamment via son réseau de caisses régionales, Crédit Agricole est particulièrement attentif aux risques climatiques, pouvant affecter sa clientèle et ses biens propres, qu’ils soient physiques ou de transition.

Consciente de ces enjeux et de la nécessité d’intégrer cette problématique pour assurer le développement durable de ses activités, le Groupe souhaite se doter d’un outil d’évaluation des risques physiques sur le périmètre de la France métropolitaine.


Objectif du projet 
------------

Ce projet est la première brique d'un projet plus vaste : 
Cette première version d'API permet à un utilisateur d'identifier le risque réel avec des données géospatiales historiques.

Le but final est de définir et d’industrialiser de manière pérenne un modèle prédictif de l’exposition aux risques physiques concernant des objets financés par le Groupe sur le territoire, selon leur géolocalisation et selon leur degré de vulnérabilité.


Données utilisées
------------

2 types de sources publiques :
- données GASPAR (Gestion Assistée des Procédures Administratives relatives aux Risques naturels) recensant les catastrophes naturelles depuis 1982.
- données INSEE de recensement des communes de France

  
Modèle
------------

A partir de la base des catastrophes naturelles agrégées par commune de France, utilisation de l'algorithme d'apprentissage supervisé KNN (K plus proches voisins).
Nous cherchons à expliquer la présence d'un risque de catastrophe naturelle (OUI/NON) par les coordonnées géographiques (latitude/longitude) et l'année d'observation.
Une gridsearch sur le nombre de voisins donne un modèle idéal à XX voisins. 
Ce modèle qui est repris dans l'API, via la bibliothèque Joblib pour une mise en cache efficace.


Fonctionnalités pour un utilisateur de l'API
------------

Après identification, l'utilisateur accède au endpoint /predict :
- il rentre 3 paramètres : une latitude, une longitude et une année
- l'API retourne la prédiction : O (pas de risque) ou 1 (risque), ainsi qu'une probabilité.

Note 1 : pour l'exercice, un utilisateurs fictif est crée :
- username: user2, password: password2
Si l'utilisateur n'est pas celui ci ou si erreur dans les identifiants/Mot de passe, une erreur 401 'Invalid credentials' apparaitra

Note 2 : des tests sont effectués dans les données saisies par les utilisateurs :
- l'année saisie doit etre un nombre entier compris entre 1982 et 2023
- la latitude et la longitude doit être comprise entre -90 et 90
Si ces tests sont validés, l'API renvoie un résultat, sinon des messages d'erreur afin de resaisir correctement les données.


Fonctionnalités pour un administrateur
------------

Après identification, l'administrateur peut accéder à un endpoint supplémentaire /view_logs :
Ce fichier recense l'ensemble des requêtes des utilisateurs : date de la requête, user, latitude, longitude, année, prediction et probabilité.

Note 1 : pour l'exercice, 1 utilisateur administrateur a été crée :
- username: user1, password: password1
Si l'utilisateur n'est pas administrateur ou si erreur dans les identifiants/Mot de passe, une erreur 403 'Permission denied. Admin access required.' apparaitra


Tests
------------

Les tests pytest sont intégrés dans une github actions et porte sur plusieurs niveaux, du plus général au plus spécifique :
- L'API est fonctionnelle
- Le endpoint /predict est accessible et renvoie des données
- L'utilisateur rentre une latitude hors normes, un message d'erreur apparaît
- L'utilisateur n'est pas authentifié, un message d'erreur apparaît
- Le endpoint /view_logs n'est pas accessible avec des identifiants qui ne correspondent pas a un profil admin
- Enfin, 4 tests unitaires de contrôle de contenu sur le endpoint /predict avec un utilisateur authentifié correctement


Installation
------------

DETAILLER COMMANDES FINALES A LANCER


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>



