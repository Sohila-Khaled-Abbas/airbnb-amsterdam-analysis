# 🤖 ML Pipelines

## 🎯 Goals
- Cluster listings into meaningful segments
- Predict price from availability and engagement features

---

## 🧠 Clustering Pipeline
- Input Features:
  - availability_365
  - number_of_reviews
  - minimum_nights
- Preprocessing:
  - VectorAssembler → StandardScaler
- Model:
  - KMeans (k=4)
- Output:
  - `clustered_listings.csv`

---

## 🧠 Regression Pipeline
- Input Features:
  - availability_365
  - number_of_reviews
  - minimum_nights
- Preprocessing:
  - VectorAssembler → StandardScaler
- Model:
  - Linear Regression
- Output:
  - `ml_predictions.csv`

---

## 📂 Model Storage
- `/ml/kmeans_model`
- `/ml/linear_regression_model`
