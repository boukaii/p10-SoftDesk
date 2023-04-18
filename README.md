Projet 10: Créez une API sécurisée RESTful en utilisant Django REST

# Description :
Projet consistant à créer une API Restful pour la société SoftDesk.


L'API doit respecter les directives suivantes :

* L'utilisateur doit pouvoir créer un compte et se connecter.
* L'accès global à l'API requiert une authentification.
* Le créateur d'un projet est le seul à pouvoir effacer ou mettre à jours son projet, il est donc le seul à pouvoir ajouter des contributeurs.
* Les contributeurs d'un projet n'ont qu'un accès en lecture à celui-ci, ils peuvent cependant créer des problèmes.
* Les problèmes suivent la même logique que les projets, seul les créateurs peuvent les mettre à jours ou les effacer.
* Les problèmes peuvent être commentés.


# Documentation :

Pour plus de détails sur le fonctionnement de cette API, se référer à sa documentation (Postman).

# Installation :

### **_Cloner le référentiel :_**
`https://github.com/boukaii/p10-SoftDesk.git`

###  **_Déplacer vers le nouveau dossier :_**
`cd pythonProject10`

### **_Créez l'environnement virtuel :_**
`python -m venv env`

### _**Activez l'environnement virtuel :**_
Pour macOS et Linux: `env/bin/activate`

Pour Windows: `env\Scripts\activate`

### **_Installez les packages :_**
`pip install -r requirements.txt`


### **_Effectuez les migrations :_**

`python manage.py makemigrations`

### **_Puis :_** 

`python manage.py migrate`

### **_Il ne vous reste plus qu'à lancer le serveur :_**

`python manage.py runserver`