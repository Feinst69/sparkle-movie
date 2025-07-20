# Mon projet Spark

# Sparkle Movie — MovieLens Recommender System

## 🎬 Présentation du projet

Face à la quantité énorme de films proposés sur les plateformes de streaming, il devient essentiel d’aider chaque utilisateur à **découvrir des contenus adaptés à ses goûts**.  
L’objectif de ce projet est de **construire, comparer et évaluer plusieurs systèmes de recommandation personnalisée** à partir des données MovieLens, en utilisant PySpark.

## 📚 Données utilisées

Le projet s’appuie sur le dataset [MovieLens 20M](https://grouplens.org/datasets/movielens/20m/),  
composé de :
- **ratings.csv** : notes des utilisateurs sur les films
- **movies.csv** : titres, genres des films
- (optionnel) **tags.csv**, **links.csv**

## ⚙️ Installation et environnement

- Python (>=3.8)
- PySpark (>=3.2)
- numpy, pandas, scikit-learn, matplotlib, seaborn  
- (optionnel) Tableau Desktop ou PowerBI pour la data viz

```bash
# Exemple d’installation
conda create -n sparkle python=3.10
conda activate sparkle
pip install pyspark numpy pandas scikit-learn matplotlib seaborn
bash

# LA VIE
