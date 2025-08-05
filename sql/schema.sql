-- Raw Listings
CREATE TABLE listings (
    id BIGINT PRIMARY KEY,
    name TEXT,
    host_id BIGINT,
    neighbourhood TEXT,
    room_type TEXT,
    price NUMERIC,
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month NUMERIC,
    calculated_host_listings_count INT,
    availability_365 INT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

-- Raw Reviews Summary
CREATE TABLE reviews_summary (
    listing_id BIGINT,
    date DATE,
    PRIMARY KEY (listing_id, date)
);

-- Raw Calendar (Pricing / Availability over time)
CREATE TABLE calendar (
    listing_id BIGINT,
    date DATE,
    available BOOLEAN,
    price NUMERIC
);