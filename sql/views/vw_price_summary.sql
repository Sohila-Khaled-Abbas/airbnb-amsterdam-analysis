CREATE VIEW vw_price_summary AS
SELECT 
    n.neighbourhood,
    r.room_type,
    AVG(f.price) AS avg_price,
    COUNT(f.listing_id) AS total_listings
FROM fact_listings f
JOIN dim_neighbourhoods n ON f.neighbourhood_id = n.neighbourhood_id
JOIN dim_room_types r ON f.room_type_id = r.room_type_id
GROUP BY n.neighbourhood, r.room_type;