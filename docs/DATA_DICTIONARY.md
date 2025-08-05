# 📚 Data Dictionary: Airbnb Listings

## 📁 listings.csv
| Column | Description |
|--------|-------------|
| id | Listing ID |
| name | Listing title |
| host_id | Host identifier |
| neighbourhood | Local area |
| latitude | Geo coord |
| longitude | Geo coord |
| room_type | Entire home / Private room / Shared room |
| price | Price per night (USD) |
| minimum_nights | Min booking duration |
| number_of_reviews | Total reviews |
| availability_365 | Availability in a year |
| calculated_host_listings_count | Total listings per host |
| reviews_per_month | Avg. reviews |

## 📁 calendar.csv
| Column | Description |
|--------|-------------|
| listing_id | Link to listings |
| date | Date of availability |
| available | Is available (Y/N) |
| price | Price for that day |

## 📁 reviews.csv
| Column | Description |
|--------|-------------|
| listing_id | Foreign key |
| date | Review date |
| reviewer_id | Reviewer ID |
| comments | Text of review |
