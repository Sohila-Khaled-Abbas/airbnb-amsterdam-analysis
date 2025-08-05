# 🔀 Data Lineage

## 📥 Raw Data
Downloaded from [Inside Airbnb](https://insideairbnb.com) as:
- listings.csv
- calendar.csv
- reviews.csv

---

## 🧼 ETL (Polars → PySpark)
- Clean missing values
- Normalize column types
- Join multiple sources
- Save to parquet and PostgreSQL

---

## 🏛️ PostgreSQL Warehouse
- Table: `airbnb_cleaned_listings`
- Table: `airbnb_calendar`
- Table: `airbnb_reviews`
- View: `airbnb_cluster_summary`
- View: `airbnb_price_predictions`

---

## 🔮 ML Outputs
- CSVs → Power BI
- Saved Models → `/ml/`
