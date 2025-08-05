from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Setup Spark
spark = SparkSession.builder.appName("TrainRegression").getOrCreate()

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

# Train/Test Split
train_data, test_data = df_scaled.randomSplit([0.8, 0.2], seed=42)

# Linear Regression Model
lr = LinearRegression(featuresCol="features", labelCol="price")
lr_model = lr.fit(train_data)
lr_model.write().overwrite().save("/home/jovyan/work/ml/linear_regression_model")

# Export predictions
predictions = lr_model.transform(test_data)
predictions.select("price", "prediction", "availability_365", "number_of_reviews", "minimum_nights") \
    .write.csv("/home/jovyan/work/data/ml_predictions.csv", header=True, mode="overwrite")