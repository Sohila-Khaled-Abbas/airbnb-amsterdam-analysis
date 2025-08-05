from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans

# Setup Spark
spark = SparkSession.builder.appName("TrainKMeans").getOrCreate()

# Load cleaned data
df = spark.read.jdbc(
    url="jdbc:postgresql://postgres:5432/airbnb_amsterdam",
    table="airbnb_cleaned_listings",
    properties={"user": "airbnb", "password": "airbnb123", "driver": "org.postgresql.Driver"}
)

# Feature Engineering
df_ml = df.select("availability_365", "number_of_reviews", "minimum_nights", "price").dropna()
assembler = VectorAssembler(inputCols=["availability_365", "number_of_reviews", "minimum_nights"], outputCol="unscaled_features")
scaler = StandardScaler(inputCol="unscaled_features", outputCol="features")
df_scaled = scaler.fit(assembler.transform(df_ml)).transform(assembler.transform(df_ml))

# KMeans Clustering
kmeans = KMeans(k=4, featuresCol="features", predictionCol="cluster")
model = kmeans.fit(df_scaled)
model.write().overwrite().save("/home/jovyan/work/ml/kmeans_model")

# Export results
df_clustered = model.transform(df_scaled)
df_clustered.write.csv("/home/jovyan/work/data/clustered_listings.csv", header=True, mode="overwrite")