# Instructions

## But de ce fichier
Ce fichier est le guide central du projet. Il sert à faire avancer le concept complet de A à Z, sans se perdre, sans sauter d’étapes, et en gardant une trace claire de l’avancement.

Ce fichier doit être considéré comme le point de départ officiel du travail.

---

## Règle absolue
Nous allons toujours **une seule chose à la fois**.

Chaque action doit être donnée :
1. **clic par clic**
2. sans ambiguïté
3. sans sauter à l’étape suivante
4. avec une validation avant de continuer

Après chaque mouvement effectué, l’utilisateur répond avec une seule des réponses suivantes :

- `OK`
- `Bloqué`
- `Sauvegarde ici`
- `Étape suivante`

Tant que l’utilisateur n’a pas répondu `OK`, on ne passe pas à la suite.

---

## Mode de travail obligatoire
L’assistant doit toujours respecter cette méthode :

1. Donner **une seule étape à la fois**
2. Détailler l’étape **clic par clic**
3. Attendre que l’utilisateur fasse l’action
4. Attendre la réponse `OK`
5. Corriger si l’utilisateur répond `Bloqué`
6. Sauvegarder l’état si l’utilisateur dit `Sauvegarde ici`
7. Reprendre exactement où le travail s’était arrêté

---

## Règle de sauvegarde de l’avancement
Quand l’utilisateur demande de sauvegarder où on est rendu, il faut enregistrer clairement :

- ce qui est terminé
- ce qui est en cours
- ce qui est bloqué
- la prochaine étape logique
- l’endroit exact où reprendre

Format recommandé :

```md
## État d’avancement
- Terminé :
- En cours :
- Bloqué :
- Prochaine étape :
- Reprise exacte :
```

L’assistant ne doit jamais repartir à zéro s’il existe déjà une sauvegarde.

---

## Première consigne obligatoire
La toute première action à faire est la suivante :

**mettre ce fichier `Instructions.md` sur GitHub dans le repo `ConstructionGPT`**

Aucune autre étape ne doit commencer avant que ce fichier soit bien déposé dans ce repo.

---

## Deuxième grande consigne
Une fois ce fichier déposé dans `ConstructionGPT`, il faudra créer un nouveau repo de projet.

Nom de travail proposé :

**MonPremierProjet**

Ce repo servira de premier vrai produit construit avec la méthode.

---

## Principe général du système
Le concept repose sur trois niveaux :

1. un repo central pour la mémoire, les règles, les instructions et l’orchestration
2. un ou plusieurs GPTs ou robots qui lisent les consignes et exécutent les tâches
3. un ou plusieurs repos de projets pour fabriquer les vrais logiciels

---

# Plan complet de A à Z

## Phase 1 — Installer le centre

### Étape 1
Déposer ce fichier `Instructions.md` dans `ConstructionGPT`.

### Étape 2
Vérifier que le repo `ConstructionGPT` existe et qu’il servira de centre de mémoire et de pilotage.

### Étape 3
Créer ou vérifier un dossier central de type :
- `/brain/`
- ou une structure équivalente pour stocker la mémoire et les consignes

### Étape 4
Ajouter les fichiers de base de pilotage :
- `Instructions.md`
- `synopsis.md`
- `communication-protocol.md`
- un fichier de suivi de progression
- un emplacement pour les robots ou agents

### Étape 5
Définir le rôle du repo central :
- mémoire
- orchestration
- consignes
- coordination
- historique

---

## Phase 2 — Structurer la mémoire

### Étape 6
Créer un fichier `synopsis.md` qui explique :
- la vision globale
- la structure du système
- les rôles
- le backlog principal
- les prochaines priorités

### Étape 7
Créer un fichier `communication-protocol.md` qui explique :
- comment un robot démarre
- quoi lire en premier
- comment trouver une tâche
- comment laisser une trace
- comment transférer une tâche

### Étape 8
Créer un fichier de progression ou une section de suivi qui permet de savoir :
- où on est rendu
- ce qui manque
- ce qui bloque
- quoi faire ensuite

---

## Phase 3 — Préparer le fonctionnement GitHub

### Étape 9
Activer les fonctions utiles du repo si nécessaire, par exemple :
- Discussions
- Issues
- Actions

### Étape 10
Créer les labels principaux pour les robots et le suivi, par exemple :
- `robot:run`
- `robot:rex`
- `robot:rio`
- `robot:rob`
- `consigne`
- `action-envoyee`

### Étape 11
Vérifier que les Issues seront utilisées comme boîte aux lettres ou système de tâches.

---

## Phase 4 — Préparer les robots ou GPTs

### Étape 12
Configurer les GPTs ou robots pour qu’ils fassent toujours au démarrage :
1. lire le centre
2. lire le synopsis
3. lire le protocole
4. vérifier leur boîte de réception
5. traiter une tâche
6. laisser une trace

### Étape 13
Préparer au minimum :
- un orchestrateur
- un exécuteur
- un validateur

Exemple :
- Run = orchestration
- Rex = exécution
- Rio = validation qualité

### Étape 14
Faire un premier test simple avec une tâche facile.

Exemple :
- créer un fichier test
- commenter une Issue
- transférer à un autre robot

---

## Phase 5 — Créer le premier vrai projet

### Étape 15
Créer un nouveau repo :
**MonPremierProjet**

### Étape 16
Ajouter un README minimal dans `MonPremierProjet`.

### Étape 17
Relier `MonPremierProjet` au repo central `ConstructionGPT` dans le synopsis ou dans un fichier d’architecture.

### Étape 18
Créer une première vraie tâche dans le centre pour demander à un robot de modifier `MonPremierProjet`.

Exemple :
- créer ou modifier `README.md`
- ajouter un fichier de base
- initialiser une structure de projet

---

## Phase 6 — Faire vivre la chaîne

### Étape 19
Tester une chaîne simple :
1. une tâche est créée
2. elle est donnée à un robot
3. le robot agit
4. il commente
5. il transmet à un autre robot si nécessaire

### Étape 20
Valider que la trace est visible dans :
- les fichiers
- les commentaires
- les Issues
- la mémoire centrale

### Étape 21
Créer une règle claire pour savoir quand une tâche est :
- terminée
- transférée
- bloquée
- à reprendre

---

## Phase 7 — Ajouter l’automatisation

### Étape 22
Ajouter un workflow GitHub Actions pour permettre un déclenchement automatique ou manuel.

### Étape 23
Ajouter un orchestrateur minimal en Python ou autre logique simple qui :
- lit le backlog
- choisit un robot cible
- crée une Issue
- évite les doublons

### Étape 24
Tester le workflow manuellement.

### Étape 25
Vérifier que des Issues automatiques apparaissent.

### Étape 26
Faire en sorte que l’orchestrateur puisse fonctionner de manière répétée sans casser le système.

---

## Phase 8 — Boucle complète

### Étape 27
Vérifier la boucle complète :
- mémoire centrale
- backlog
- orchestrateur
- robot
- validation
- mise à jour
- sauvegarde d’avancement

### Étape 28
Documenter la reprise :
si on coupe le travail, il doit être possible de reprendre exactement au bon endroit.

### Étape 29
Créer une méthode stable pour continuer avec d’autres projets après `MonPremierProjet`.

---

# Ce que l’assistant doit faire à chaque étape
À chaque fois, l’assistant doit répondre dans ce format :

## Étape X
### But
[but de l’étape]

### Ce que tu dois faire
[actions clic par clic]

### Ce que tu dois voir
[preuve visuelle attendue]

### Quand c’est fait
Réponds : `OK`

### Si ça bloque
Réponds : `Bloqué`

L’assistant ne doit pas envoyer plusieurs étapes à la fois sauf si l’utilisateur demande explicitement une vue d’ensemble.

---

# Réponses utilisateur autorisées
L’utilisateur peut répondre uniquement avec :

- `OK`
- `Bloqué`
- `Sauvegarde ici`
- `Étape suivante`

Le système doit être capable d’avancer proprement à partir de ces réponses simples.

---

# Règle de reprise
Si une sauvegarde existe, l’assistant doit toujours :
1. relire l’état sauvegardé
2. dire où on est rendu
3. dire ce qui est terminé
4. dire la prochaine étape logique
5. reprendre sans recommencer tout le projet

---

# Démarrage officiel
On commence toujours par ceci :

## Étape 1
Déposer ce fichier `Instructions.md` dans le repo `ConstructionGPT`.

Quand c’est fait, répondre :

`OK`
