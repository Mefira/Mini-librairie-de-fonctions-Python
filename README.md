# Mini Librairie de Fonctions Python

Bienvenue dans **Mini Librairie de Fonctions Python**, un projet conçu pour aider les débutants en Python à explorer, comprendre et utiliser les concepts fondamentaux du langage. Cette bibliothèque contient une collection de fonctions utiles qui couvrent différents domaines, notamment les mathématiques, la manipulation de chaînes, les conversions numériques, et bien plus encore. Chaque fonction est accompagnée de logique claire et simple, adaptée aux débutants.

## Objectifs du Projet

1. **Apprentissage** : Offrir aux débutants des exemples pratiques de fonctions Python.
2. **Exploration** : Permettre de découvrir différentes applications des concepts de base (conditions, boucles, récursivité, etc.).
3. **Réutilisation** : Fournir une boîte à outils de fonctions prêtes à l'emploi pour des projets ou des exercices simples.

---

## Fonctionnalités

Voici les principales fonctionnalités disponibles dans cette librairie :

### 1. **Manipulation de Calendrier**
- **`calendar()`** : Affiche le calendrier d'un mois spécifique d'une année donnée.

### 2. **Mathématiques**
- **`quadratic()`** : Résout une équation du second degré et affiche les solutions réelles ou complexes.
- **`permutation(a, b)`** : Permute deux valeurs sans utiliser de variable temporaire.
- **`factoriel(n)`** : Calcule le factoriel d'un entier en utilisant une approche récursive.
- **`pgcd(a, b)`** : Calcule le Plus Grand Commun Diviseur (PGCD) de deux entiers.
- **`ppcm(a, b)`** : Calcule le Plus Petit Commun Multiple (PPCM) de deux entiers (deux versions disponibles).
- **`saisie_entier()`** : Demande à l'utilisateur de saisir un entier valide.

### 3. **Nombres Premiers**
- **`prime(n)`** : Vérifie si un nombre est premier ou non.
- **`chek_prime(n)`** : Une version alternative pour vérifier la primalité.
- **`first_prime(n)`** : Affiche les `n` premiers nombres premiers sous forme de liste.

### 4. **Fibonacci**
- **`fibonacci(n)`** : Génère la valeur de Fibonacci pour un entier donné (version récursive).

### 5. **Nombres d'Amstrong**
- **`amstrong(n)`** : Vérifie si un nombre est un nombre d'Amstrong.
- **`first_amstrong(n)`** : Affiche les `n` premiers nombres d'Amstrong.

### 6. **Conversions Numériques**
- **`binary(n)`** : Convertit un nombre décimal en binaire.
- **`octal(n)`** : Convertit un nombre décimal en octal.
- **`hexa(n)`** : Convertit un nombre décimal en hexadécimal.

### 7. **Manipulation de Chaînes**
- **`affichage()`** : Génère toutes les combinaisons possibles entre sujets, verbes et objets d'une liste donnée.

### 8. **Recherche dans les Tableaux**
- **`recherche(tableau, cible)`** : Recherche un élément dans un tableau (trié ou non) en utilisant la recherche binaire.
- **`recherche_indice(tableau, cible)`** : Recherche l'indice d'un élément dans un tableau trié.

---

## Points Forts

- **Clarté** : Le code est écrit de manière simple et lisible, avec des commentaires explicatifs pour chaque fonction.
- **Accessibilité** : Les fonctions sont conçues pour être utilisées directement, sans dépendances externes.
- **Approche éducative** : Chaque fonction présente des concepts fondamentaux de la programmation Python, tels que les boucles, les conditions, la récursivité, et les structures de données comme les listes.

---

## Prérequis

- **Python 3.x** : Assurez-vous d'avoir une version récente de Python installée sur votre machine.
- **Aucune bibliothèque externe** : Toutes les fonctions utilisent uniquement les modules standards de Python.

---

## Installation et Usage

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Mefira/Mini-librairie-de-fonctions-Python.git
   ```

2. Importez les fonctions dans votre script Python pour les utiliser :
   
   ```python
   from votre_fichier import *
   ```

3. Appelez les fonctions directement dans le terminal ou dans un script Python :

   Exemple :
   ```python
   # Résolution d'une équation quadratique
   quadratic()

   # Vérification de primalité d'un nombre
   prime(17)

   # Conversion en binaire
   print(binary(42))
   ```

---

## Exemple d'Utilisation

Voici un exemple simple pour générer une liste des 5 premiers nombres premiers et convertir un nombre décimal en hexadécimal :

```python
# Liste des 5 premiers nombres premiers
first_prime(5)

# Conversion d'un nombre décimal en hexadécimal
print(hexa(255))
```
## Auteur

Ce projet a été développé pour les débutants en Python afin de leur fournir un outil éducatif et pratique. 

N'hésitez pas à me contacter pour toute question ou suggestion. 😊

---

## License

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, de le modifier et de le partager.
