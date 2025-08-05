-- Listing availability per month
CREATE MATERIALIZED VIEW mv_listing_availability_monthly AS
SELECT
    listing_id,
    DATE_TRUNC('month', date) AS month,
    COUNT(*) FILTER (WHERE available) AS available_days,
    COUNT(*) AS total_days,
    AVG(price) AS avg_price
FROM calendar
GROUP BY listing_id, month;