# Sparkle Movie — MovieLens Recommender System

## 🎬 Présentation du projet

Face à la quantité énorme de films proposés sur les plateformes de streaming, il devient essentiel d’aider chaque utilisateur à découvrir des contenus adaptés à ses goûts.  
L’objectif de ce projet est de construire, comparer et évaluer plusieurs systèmes de recommandation personnalisée à partir des données MovieLens, en utilisant PySpark.

## 📚 Données utilisées

Le projet s’appuie sur le dataset MovieLens 20M (https://grouplens.org/datasets/movielens/20m/),  
composé de :
- ratings.csv : notes des utilisateurs sur les films
- movies.csv : titres, genres des films
- (optionnel) tags.csv, links.csv

## ⚙️ Installation et environnement

- Python (>=3.8)
- PySpark (>=3.2)
- numpy, pandas, scikit-learn, matplotlib, seaborn  
- (optionnel) Tableau Desktop ou PowerBI pour la data viz

Exemple d’installation :
- conda create -n sparkle python=3.10
- conda activate sparkle
- pip install pyspark numpy pandas scikit-learn matplotlib seaborn

## 🚦 Structure du repo

sparkle-movie/
├── README.md  
├── als_true.ipynb             # Notebook principal (modélisation, éval)  
├── data/  
│   ├── ratings.csv  
│   ├── movies.csv  
│   └── ...  
├── src/                       # Scripts Python optionnels  
│   └── ...  
└── figures/                   # Graphiques pour slides/rapports

## 🔍 Exploration des données

- Analyse du dataset : nombre d’utilisateurs, de films, distribution des notes, sparsité.
- Statistiques sur les genres, films les mieux notés, utilisateurs les plus actifs.
- Préparation des matrices utilisateurs-films.

## 🤖 Méthodes de recommandation implémentées

1. **Collaborative Filtering (ALS — Alternating Least Squares)**  
   - Factorisation de matrice pour obtenir des embeddings utilisateurs et films.  
   - Grid search sur le nombre de facteurs latents, régularisation.  
   - Évaluation RMSE, précision@k, recall@k.  
   - Sauvegarde du modèle entraîné.

2. **KNN User-based**  
   - Calcul de la similarité entre utilisateurs (dans l’espace latent ALS).  
   - Recommandation basée sur les voisins les plus proches (top K).  
   - Évaluation précision@k, recall@k.

3. **KNN Item-based**  
   - Similarité entre films dans l’espace latent.  
   - Recommandation de films similaires à ceux déjà aimés.  
   - Évaluation précision@k, recall@k.

## 📊 Évaluation des modèles

- Séparation train/test utilisateurs.
- Calcul des métriques : RMSE, précision@k, recall@k.
- Benchmark des méthodes sur un sous-échantillon (100 à 1000 utilisateurs).

Scores obtenus (exemple) :
- ALS : Precision@25 = 0.06, Recall@25 = 0.05 (à adapter selon tes résultats)
- KNN user/item : valeurs similaires ou inférieures

## 🎯 Limites et perspectives d’amélioration

- Scores initiaux faibles : suggèrent la nécessité d’affiner les modèles.
- Pistes : meilleure sélection des hyperparamètres, enrichissement des profils utilisateurs/films, approche hybride, gestion du cold start.
- Possibilité de combiner contenu et collaboratif pour de meilleurs résultats.

## 🌟 Pourquoi ce projet est important

- Appréhender des algorithmes majeurs de la recommandation à grande échelle.
- Reproduire les workflows des géants du streaming (Netflix, Amazon, Spotify…).
- Valoriser les données utilisateurs pour améliorer la satisfaction et la fidélisation.

## 📁 Liens utiles

- MovieLens Dataset : https://grouplens.org/datasets/movielens/20m/
- PySpark documentation : https://spark.apache.org/docs/latest/api/python/index.html
- Alternating Least Squares explained : https://sophwats.github.io/2018-04-05-gentle-als.html
- Collaborative Filtering — Towards Data Science : https://towardsdatascience.com/how-to-build-a-simple-recommender-system-in-python-375093c3fb7d

## ✨ Auteur

Projet réalisé dans le cadre de Sparkle Movie — système de recommandation de films  
N’hésite pas à forker, tester, proposer des améliorations !
