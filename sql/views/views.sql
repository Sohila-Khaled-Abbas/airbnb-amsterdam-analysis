-- Clean view for Listings with average review score
CREATE VIEW vw_listings_enriched AS
SELECT
    l.*,
    COALESCE(r.total_reviews, 0) AS total_reviews,
    COALESCE(r.first_review_date, NULL) AS first_review_date,
    COALESCE(r.last_review_date, NULL) AS last_review_date
FROM listings l
LEFT JOIN (
    SELECT
        listing_id,
        COUNT(*) AS total_reviews,
        MIN(date) AS first_review_date,
        MAX(date) AS last_review_date
    FROM reviews_summary
    GROUP BY listing_id
) r ON l.id = r.listing_id;