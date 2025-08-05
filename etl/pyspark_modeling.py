# 1. Initialize Spark session
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AirbnbDWH") \
    .getOrCreate()

spark.conf.set("spark.hadoop.native.lib", "false")    

# 2. Load data into DataFrames
listings_df = spark.read.csv("cleaned_listings.csv", header=True, inferSchema=True)
calendar_df = spark.read.csv("cleaned_calendar.csv", header=True, inferSchema=True)
reviews_df = spark.read.csv("cleaned_reviews.csv", header=True, inferSchema=True)

# 3. Transform data into dimensional models
from pyspark.sql.functions import col, to_date

# DIM LISTINGS
dim_listings = listings_df.select(
    col("listing_id").cast("int"),
    col("host_id").cast("int"),
    col("room_type"),
    col("price"),
    col("neighbourhood_cleansed"),
    col("minimum_nights"),
    col("number_of_reviews"),
    col("reviews_per_month"),
    col("availability_365")
).dropDuplicates(["listing_id"])

# DIM CALENDAR
dim_calendar = calendar_df.select(
    col("listing_id").cast("int"),
    to_date("date", "yyyy-MM-dd").alias("calendar_date"),
    col("available"),
    col("price").alias("calendar_price")
).dropDuplicates(["listing_id", "calendar_date"])

# DIM REVIEWS
dim_reviews = reviews_df.select(
    col("listing_id").cast("int"),
    to_date("date", "yyyy-MM-dd").alias("review_date")
).dropDuplicates(["listing_id", "review_date"])

# 4. Create fact tables
# FACT BOOKINGS (Calendar enriched with listing attributes)
fact_bookings = dim_calendar.join(dim_listings, on="listing_id", how="left")