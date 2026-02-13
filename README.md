# projet_dashboard

## Présentation du projet

Je développe actuellement un site web classique destiné au public, accompagné d’un espace administrateur (dashboard) permettant la gestion du contenu. Ce projet a pour objectif de mettre en pratique le développement web full‑stack, de la conception visuelle à la gestion des données.

**Technologies utilisées :**

- HTML / Jinja
- CSS / Tailwind CSS
- Python avec le framework Flask

---

## État d’avancement du projet

### 1. Conception du site public

J’ai commencé le design du site public. La structure HTML est en place et le style est progressivement travaillé avec CSS et Tailwind CSS afin d’obtenir une interface moderne, claire et responsive.

### 2. Conception du dashboard administrateur

Le design du dashboard a également été entamé. L’objectif est de proposer une interface simple et efficace permettant à l’administrateur de gérer le contenu du site (articles, données, etc.).

### 3. Système de connexion

Le système de connexion est désormais terminé. Il permet à un administrateur de s’authentifier de manière sécurisée afin d’accéder au dashboard. Cette étape a été essentielle pour protéger l’espace d’administration.

### 4. Système d’articles

Le système d’articles est en cours de développement. La structure générale est définie et les bases du fonctionnement (création et gestion des articles) sont mises en place.

### 5. Ajout d’articles via un formulaire

L’ajout des articles dans la base de données via un formulaire est entièrement fonctionnel. Les données saisies sont correctement traitées par Flask et enregistrées, ce qui permet une gestion dynamique du contenu.

### 6. Design du tableau de gestion

Le design du tableau de gestion (tableau listant les articles ou les données) est en cours. Il servira à visualiser, modifier ou supprimer les éléments enregistrés dans la base de données.

### 7. Refont du design du side bar

Ajout d’une animation sur le clique du bouton article afin d’avoir un menu déroulant.

### 8. Ajout d’un article via un formulaire

Le design de la page est terminé, l’ajout de l’article se fait avec succés.

### 9. Ajout de la fonctionnalité de modification

Ajout d’un bouton modifier sur le tableau des articles. La page de la modification a été basé sur la page d’ajout d’un article avec le bouton supprimer et l’ajout des informations existants sur l’article (le titre, la description, les tags). La modification se fait avec succés.

### 10. Rangement du code

Un rangement du code a été lancé pour le rendre compréhensible et modulaire.

# 🚀 Lancer le serveur web du site

Pour démarrer le serveur web du projet, suivez les étapes ci-dessous.

---

## ✅ Prérequis

- Python installé sur votre machine
- Un environnement virtuel déjà créé (`.venv`)

---

## 1️⃣ Activer l’environnement virtuel

L’environnement virtuel permet d’utiliser les dépendances du projet sans affecter le reste du système.

### Étapes :

1. **Ouvrez un terminal**
2. **Placez-vous dans le dossier racine du projet**

```bash
cd chemin/vers/le/projet
```

1. **Activez l’environnement virtuel**

### ▶ Sous Windows

```bash
.venv\Scripts\activate
```

### ▶ Sous macOS / Linux

```bash
source .venv/bin/activate
```

Une fois activé, vous devriez voir `(.venv)` apparaître au début de votre ligne de commande.

> ⚠️ Si Python n’est pas installé ou si l’environnement virtuel n’existe pas, une erreur apparaîtra.
> 

---

## 2️⃣ Lancer le serveur Flask

Une fois dans l’environnement virtuel, la commande `flask` devient disponible.

```bash
flask --app main run
```

---

## 🌍 Accéder au site

Après l’exécution de la commande :

- Le serveur démarre
- Une adresse s’affiche dans le terminal, par exemple :

```
http://127.0.0.1:5000
```

Ouvrez cette adresse dans votre navigateur pour accéder au site.

---

## 🛑 Arrêter le serveur

Dans le terminal, utilisez :

```
CTRL + C
```

# Utilisation des documentations

- Flask : https://flask.palletsprojects.com/en/stable/
- Jinja : https://jinja.palletsprojects.com/en/stable/templates/
- Tailwind : https://tailwindcss.com/docs/
