# Amsterdam Airbnb Data Analytics
An end-to-end data analytics project using PySpark, PostgreSQL, Power BI, and ML to analyze and predict Airbnb activity in Amsterdam.

---

## Project Goals

- Clean and transform Airbnb datasets
- Build a PostgreSQL data warehouse
- Implement ML pipelines (clustering & regression)
- Deliver insights through Power BI dashboards

---

## Project Structure
```
Airbnb_Amsterdam_Project/
├── data/
│   ├── raw/                # Raw Airbnb datasets in CSV format
│   └── processed/          # Cleaned and transformed datasets ready for analysis
├── notebooks/
│   └── airbnb_ml_pipeline.ipynb  # Jupyter notebook showcasing the ML pipeline implementation
├── etl/
│   ├── polars_cleaning.py   # Python script for extracting data using Polars library
│   ├── pyspark_modeling.py  # PySpark script for data transformation and cleaning
│   └── pyspark_load_to_postgres.py # Script for loading transformed data into PostgreSQL database
├── sql/
│   ├── schema.sql          # SQL file defining the database schema and tables
│   ├── views.sql           # SQL file containing views for aggregated data analysis
│   └── data_modeling.sql   # SQL scripts for advanced data modeling and relationships
├── ml/
│   ├── train_kmeans.py     # Python script for training a clustering model using KMeans
│   └── train_regression.py # Python script for training a regression model for predictions
├── jar/
│   └── postgresql-42.7.7.jar      # Compiled Spark jobs for distributed data processing
├── docker/
│   ├── Dockerfile          # Dockerfile for containerizing the application
│   └── docker-compose.yml  # Docker Compose file for orchestrating multi-container setup
├── dashboard/
│   └── powerbi.pbix        # Power BI dashboard file for visualizing insights
├── docs/
│   ├── PROJECT_OVERVIEW.md # High-level overview of the project and its goals
│   ├── DATA_DICTIONARY.md  # Comprehensive dictionary of all datasets and fields
│   ├── ML_PIPELINES.md     # Detailed documentation of machine learning pipelines
│   ├── DATA_LINEAGE.md     # Documentation of data flow and lineage across the project
│   ├── USAGE_GUIDE.md      # Step-by-step guide for setting up and using the project
├── presentation/
│   ├── gamma_prompts.txt   # Text file containing presentation prompts and notes
│   └── slides/             # Folder containing presentation slides in various formats
├── README.md               # Main README file with project introduction and instructions
└── requirements.txt        # List of Python dependencies required for the project
```

---

## Tech Stack

- Data Engineering: PySpark, Polars, PostgreSQL
- ML Models: KMeans Clustering, Linear Regression
- Visualization: Power BI
- Environment: Docker Compose, VS Code Insiders

---

## Power BI Report Pages

1. Amsterdam Overview
2. Booking Behavior
3. Clustering Insights
4. Price Predictions

---

## ML Performance

- Regression RMSE: XX.XX
- Best Cluster Price: €XXX
- Key Drivers: Availability, Reviews, Min Nights

---

## 📦 How to Run

```bash
# Start services
docker-compose up -d

# Access Jupyter
http://localhost:8888

# Load data to Postgres
python scripts/load_to_postgres.py

# Train ML Models
spark-submit ml/train_kmeans.py
spark-submit ml/train_regression.py

```

---

# Contact
- Built by Sohila Khaled - [LinkedIn](https://www.linkedin.com/in/sohilakabbas) | [Portfolio](https://sohilakhaled.com)
