# 🏠 Project Overview: Amsterdam Airbnb Analytics

## 📌 Objective
This project aims to uncover insights from Amsterdam Airbnb listings using advanced analytics techniques:
- Build a PostgreSQL Data Warehouse
- Implement ML pipelines with PySpark
- Use clustering for customer segmentation
- Predict price using regression
- Create an executive Power BI dashboard

---

## 📈 Business Questions
- What are the pricing patterns and seasonality in Amsterdam’s Airbnb market?
- How can we segment listings for targeted recommendations?
- Which features are most predictive of listing prices?
- Which neighborhoods have the most competitive listings?

---

## 💼 Tools & Technologies
| Task | Tools |
|------|-------|
| ETL | PySpark, Polars |
| Storage | PostgreSQL (Dockerized) |
| ML | PySpark MLlib |
| Visualization | Power BI |
| Deployment | Docker Compose |
| Documentation | Markdown, VS Code |

---

## 🔄 End-to-End Flow
1. Download raw data from [Inside Airbnb](https://insideairbnb.com/get-the-data.html)
2. Clean and transform using Polars & PySpark
3. Load into PostgreSQL (Docker)
4. Apply clustering and regression models
5. Export results and build dashboard in Power BI
