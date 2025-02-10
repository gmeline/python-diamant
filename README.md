💎 Diamond Generator

📌 Description

Ce projet est un script Python qui génère un diamant en ASCII en fonction d'une lettre donnée. La lettre sert de point culminant du diamant, avec les lettres précédentes de l'alphabet formant la structure symétrique.
_________________
🛠️ Fonctionnalités

✅ Génération d'un diamant en fonction d'une lettre majuscule de A à Z.

✅ Structure centrée et symétrique.

✅ Affichage du résultat dans le terminal.
_________________
🚀 Installation et utilisation

1️⃣ Prérequis

Python 3 installé sur votre machine.

2️⃣ Installation

Clonez le projet :

git clone https://github.com/gmeline/python-Diamond-ExamenFinal.git

cd python-Diamond-ExamenFinal

3️⃣ Utilisation

Exécutez le script en ligne de commande en spécifiant une lettre :

python diamond.py

Par défaut, le script utilise la lettre 'C'. Vous pouvez modifier cet argument dans le code en changeant :

diamond('C')

ou en adaptant le script pour prendre une entrée utilisateur :

letter = input("Entrez une lettre : ")

diamond(letter)
_________________
🛠️ Explication du Code

Le script fonctionne en deux étapes :

Il construit la première moitié du diamant en ajoutant des espaces et les lettres appropriées.

Il génère ensuite la seconde moitié en inversant la première partie.
