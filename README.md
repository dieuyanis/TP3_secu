# TP3 - Sécurité Web et Réseaux : Stéganographie d'Image

## Auteurs
- **Code permanent** : VACR21030400, **Nom** : VACHALDE, **Prénom** : Rémi
- **Code permanent** : ______, **Nom** : NURY, **Prénom** : Yanis

---

## Description
Ce projet implémente une application en ligne de commande (CLI) permettant de cacher et de révéler des messages secrets dans des images, en utilisant la stéganographie. Voici un guide détaillé pour installer, configurer et utiliser ce projet.


---

## **Table des matières**
1. [Prérequis](#prérequis)
2. [Installation](#installation)
    - [Installation de Python](#installation-de-python)
    - [Installation de Poetry](#installation-de-poetry)
3. [Configuration du projet](#configuration-du-projet)
4. [Commandes disponibles](#commandes-disponibles)
5. [Structure du projet](#structure-du-projet)
6. [Exemples d'utilisation](#exemples-dutilisation)
7. [Notes importantes](#notes-importantes)

---

## **Prérequis**
- Un ordinateur avec **Windows**, **macOS** ou **Linux**.
- **Python 3.11** ou une version ultérieure.
- Un éditeur de texte ou un IDE, tel que **Visual Studio Code** ou **PyCharm**.

---

## **Installation**

### **Installation de Python**
1. Rendez-vous sur le site officiel de Python : [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Téléchargez l'installateur correspondant à votre système d'exploitation.
3. Lors de l'installation :
    - Assurez-vous de cocher **Add Python to PATH**.
    - Sélectionnez **Install Now**.
4. Vérifiez que Python est installé correctement :
   ```bash
   python --version
   ```
   La version installée doit s'afficher, par exemple : `Python 3.11.x`.

---

### **Installation de Poetry**
1. Téléchargez et installez Poetry via la commande :
    - **Windows** :
      ```powershell
      (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
      ```
    - **macOS/Linux** :
      ```bash
      curl -sSL https://install.python-poetry.org | python3 -
      ```
2. Vérifiez l'installation :
   ```bash
   poetry --version
   ```
   La version installée doit s'afficher, par exemple : `Poetry (version 1.x.x)`.

---

## **Configuration du projet**

1. **Clonez ce dépôt ou téléchargez-le** :
   ```bash
   git clone https://github.com/dieuyanis/TP3_secu.git
   cd TP3_secu
   ```

2. **Créez un environnement virtuel et installez les dépendances** :
   ```bash
   poetry install
   ```
   Cette commande :
    - Configure un environnement virtuel isolé.
    - Installe toutes les dépendances listées dans le fichier `pyproject.toml`.

3. **Activez l'environnement virtuel** (si nécessaire) :
    - Sous **Windows** :
      ```bash
      .venv\Scripts\activate
      ```
    - Sous **macOS/Linux** :
      ```bash
      source .venv/bin/activate
      ```

---

## **Commandes disponibles**

### **1. Cacher un message dans une image**
Utilisez la commande suivante pour cacher un message :
```bash
poetry run python src/stegano.py hide <chemin-image-originale> <chemin-image-sortie> "<message>"
```
- `<chemin-image-originale>` : Chemin de l'image source dans laquelle le message sera caché.
- `<chemin-image-sortie>` : Chemin où l'image encodée sera sauvegardée.
- `<message>` : Message secret à cacher dans l'image.

### **2. Révéler un message caché dans une image**
Utilisez la commande suivante pour révéler un message :
```bash
poetry run python src/stegano.py reveal <chemin-image-encodée>
```
- `<chemin-image-encodée>` : Chemin de l'image contenant un message caché.

### **3. Mettre à jour les dépendances**
Pour mettre à jour les dépendances du projet, exécutez :
```bash
poetry update
```

---

## **Structure du projet**

Voici la structure générale du projet :

```
tp3-steganographie/
│
├── src/
│   ├── input/
│   │   └── exemple_image.png # Image d'entrée
│   ├── output/
│   │   └── encoded_image.png # Image encodée générée
│   └── stegano.py            # Script principal
│
├── .venv/                    # Environnement virtuel (géré par Poetry)
├── pyproject.toml            # Fichier de configuration du projet Poetry
├── README.md                 # Documentation du projet
```

---

## **Exemples d'utilisation**

### **Cacher un message**
1. Ajoutez une image source dans le dossier `src/input/`.
2. Exécutez la commande :
   ```bash
   poetry run python src/stegano.py hide src/input/exemple_image.png src/output/encoded_image.png "Ceci est un message secret"
   ```
3. Une nouvelle image, `encoded_image.png`, sera créée dans `src/output/`.

### **Révéler un message**
1. Assurez-vous d'avoir une image encodée, par exemple dans `src/output/encoded_image.png`.
2. Exécutez la commande :
   ```bash
   poetry run python src/stegano.py reveal src/output/encoded_image.png
   ```
3. Le message caché sera affiché dans le terminal.

---

## **Notes importantes**
1. **Dépendances** : Le projet utilise la bibliothèque `Pillow` pour manipuler les images. Cette dépendance est installée automatiquement par Poetry.
2. **Marqueur de fin** : Le message caché est suivi d’un marqueur de fin spécial (`11111110`) pour signaler la fin du message.
3. **Limites** :
    - La taille du message dépend de la taille de l'image. Une image trop petite ne pourra pas contenir un message trop long.
    - Assurez-vous que les fichiers d'entrée et de sortie existent dans les dossiers appropriés.
    - Seul le format PNG est accepté

---

## **Patern général du projet**

- **Objectif pédagogique** : Apprendre à manipuler des fichiers binaires, utiliser des bibliothèques Python, et développer une interface CLI robuste.
- **Extensions possibles** :
    - Ajouter une interface graphique (GUI).
    - Intégrer des algorithmes de cryptographie pour sécuriser le message avant de le cacher.
    - Permettre de choisir d'autres formats d'image (par exemple, `.jpg`, `.bmp`).

---

## **Ajouts Bonus**

### **1. Gestion des erreurs avancée**
Pour améliorer l'expérience utilisateur et garantir la robustesse du programme, plusieurs mécanismes de gestion d'erreurs ont été ajoutés :

- **Vérification de l'existence des fichiers :**
  Si le fichier d'entrée spécifié n'existe pas, le programme affiche une erreur et arrête l'exécution.

- **Validation du format du fichier :**
  Seuls les fichiers au format `.png` sont acceptés comme entrée. Si un fichier d'un autre format est fourni, le programme refuse de continuer.

### **2. Gestion des conflits avec les fichiers de sortie**
Lors de l'écriture d'une image encodée, le programme vérifie si un fichier portant le même nom existe déjà. Si c'est le cas, l'utilisateur est invité à choisir parmi les options suivantes :
- **Écraser le fichier existant :** L'image encodée remplace le fichier existant.
- **Renommer le fichier de sortie :** Un nouveau nom est généré automatiquement dans le même dossier pour éviter tout conflit. Exemple : `encoded_image_1.png`, `encoded_image_2.png`, etc.
- **Annuler l'opération :** L'utilisateur peut choisir de ne pas créer le fichier.

### **3. Création automatique des dossiers**
Si les dossiers spécifiés pour l'entrée ou la sortie (`src/input`, `src/output`) n'existent pas, le programme les crée automatiquement. Cela évite les erreurs liées à des dossiers manquants.
