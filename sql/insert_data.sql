-- Example for dim_room_types
INSERT INTO dim_room_types (room_type)
SELECT DISTINCT room_type
FROM staging_listings;

-- Similarly, populate other dims and fact