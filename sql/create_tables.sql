-- Create dimensions
CREATE TABLE dim_hosts (
    host_id BIGINT PRIMARY KEY,
    host_name TEXT,
    host_since DATE
);

CREATE TABLE dim_neighbourhoods (
    neighbourhood_id SERIAL PRIMARY KEY,
    neighbourhood_group TEXT,
    neighbourhood TEXT
);

CREATE TABLE dim_room_types (
    room_type_id SERIAL PRIMARY KEY,
    room_type TEXT
);

CREATE TABLE dim_dates (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT,
    day_name TEXT
);

-- Create fact table
CREATE TABLE fact_listings (
    listing_id BIGINT PRIMARY KEY,
    host_id BIGINT REFERENCES dim_hosts(host_id),
    neighbourhood_id INT REFERENCES dim_neighbourhoods(neighbourhood_id),
    room_type_id INT REFERENCES dim_room_types(room_type_id),
    date_id DATE REFERENCES dim_dates(date_id),
    price FLOAT,
    minimum_nights INT,
    number_of_reviews INT,
    availability_365 INT
);