from pyspark.sql import SparkSession
import os

# PostgreSQL credentials - ensure these are set via Docker ENV or .env
POSTGRES_URL = os.getenv("POSTGRES_URL", "jdbc:postgresql://localhost:5432/airbnb")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

# 1. Start Spark Session
spark = SparkSession.builder \
    .appName("LoadCleanedAirbnbData") \
    .config("spark.jars", "/app/jars/postgresql-42.6.0.jar") \
    .getOrCreate()

# 2. Load cleaned Polars CSV as Spark DataFrame
df = spark.read.csv("/app/data/listings_cleaned.csv", header=True, inferSchema=True)

# 3. Write to PostgreSQL
df.write \
    .format("jdbc") \
    .option("url", POSTGRES_URL) \
    .option("dbtable", "airbnb_cleaned_listings") \
    .option("user", POSTGRES_USER) \
    .option("password", POSTGRES_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

spark.stop()