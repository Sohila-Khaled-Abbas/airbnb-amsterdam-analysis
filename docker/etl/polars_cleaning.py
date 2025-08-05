import polars as pl

# 1. Load raw data
calendar = pl.read_csv("D://courses/Data Science/Projects/Airbnb_Amsterdam_Project/data/raw/calendar.csv.gz", infer_schema_length=1000)
listings = pl.read_csv("D://courses/Data Science/Projects/Airbnb_Amsterdam_Project/data/raw/listings.csv.gz", infer_schema_length=1000)

# 🔧 Ensure consistent data types for join key
calendar = calendar.with_columns([
    pl.col("listing_id").cast(pl.Int64)
])

listings = listings.with_columns([
    pl.col("id").alias("listing_id").cast(pl.Int64)
])

# 🔹 Clean listings
listings_clean = listings.select([
    pl.col("listing_id"),
    pl.col("host_id"),
    pl.col("neighbourhood_cleansed"),
    pl.col("room_type"),
    pl.col("price").str.replace_all(r"[\$,]", "").cast(pl.Float64),
    pl.col("minimum_nights").cast(pl.Int64),
    pl.col("number_of_reviews").cast(pl.Int64),
    pl.col("reviews_per_month").cast(pl.Float64),
    pl.col("availability_365").cast(pl.Int64)
])

# 🔹 Clean calendar
calendar_clean = calendar.select([
    pl.col("listing_id"),
    pl.col("date").str.strptime(pl.Date, format="%Y-%m-%d"),
    pl.col("available"),
    pl.col("price").str.replace_all(r"[\$,]", "").cast(pl.Float64)
])

# 🔗 Join calendar with listings
calendar_enriched = calendar_clean.join(
    listings_clean,
    on="listing_id",
    how="left"
)

# 1. Load reviews data
reviews = pl.read_csv("D://courses/Data Science/Projects/Airbnb_Amsterdam_Project/data/raw/reviews.csv.gz", infer_schema_length=1000)

# 🔹 Clean reviews
reviews_clean = reviews.select([
    pl.col("listing_id").cast(pl.Int64),
    pl.col("date").str.strptime(pl.Date, format="%Y-%m-%d")
])

# 🔗 Join reviews with listings
reviews_enriched = reviews_clean.join(
    listings_clean,
    on="listing_id",
    how="left"
)

# Ensure reviews_clean and listings_clean are not empty before joining
if reviews_clean.shape[0] > 0 and listings_clean.shape[0] > 0:
    reviews_enriched = reviews_clean.join(
        listings_clean,
        on="listing_id",
        how="left"
    )

# Ensure reviews_enriched is defined before saving
if reviews_enriched is not None:
    # 📁 Save cleaned and joined data
    calendar_enriched.write_csv("cleaned_calendar.csv")
    listings_clean.write_csv("cleaned_listings.csv")
    reviews_enriched.write_csv("cleaned_reviews.csv")

print("✅ ETL completed and files saved.")