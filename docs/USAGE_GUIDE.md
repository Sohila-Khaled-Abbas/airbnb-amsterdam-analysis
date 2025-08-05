# 🚀 Usage Guide

## Prerequisites
- Docker
- VS Code Insiders
- Power BI Desktop
- Python 3.12+

---

## Step 1: Start Docker
```bash
docker-compose up -d
```
---

## Step 2: Clean and Load Data
```bash
python scripts/load_to_postgres.py
```

---

## Step 3: Train ML Pipelines
```bash
spark-submit ml/train_kmeans.py
spark-submit ml/train_regression.py
```

---

## Step 4: Visualize
- Open Power BI
- Load `data/clustered_listings.csv` + `ml_predictions.csv`
- Or connect to PostgreSQL directly
