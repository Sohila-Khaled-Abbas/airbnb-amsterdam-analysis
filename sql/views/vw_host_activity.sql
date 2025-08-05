CREATE VIEW vw_host_activity AS
SELECT 
    h.host_id,
    h.host_name,
    COUNT(f.listing_id) AS total_listings,
    AVG(f.price) AS avg_price
FROM fact_listings f
JOIN dim_hosts h ON f.host_id = h.host_id
GROUP BY h.host_id, h.host_name;