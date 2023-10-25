

--  Checks for old instance of previous table name ---
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

--  Drops listings table (first) and it's sequence (if they exist)
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;

--  Drop accommodations table and it's sequence (if they exist)
DROP TABLE IF EXISTS accommodations;
DROP SEQUENCE IF EXISTS accommodations_id_seq;


--  Drop users table and it's sequence (if they exist)
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


--  Creates users table
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
    
);

--  Creates accommodation table
CREATE SEQUENCE IF NOT EXISTS accommodations_id_seq;
CREATE TABLE accommodations (
    id SERIAL PRIMARY KEY,
    place_name VARCHAR(255),
    host_id int,
    img_path VARCHAR(255),
    description VARCHAR(255),
    price VARCHAR(255),
    constraint fk_host foreign key(host_id) references users(id) on delete cascade
);

--  Creates listings table
CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    user_id int,
    accommodation_id int,
    is_booked BOOLEAN,
    start_date VARCHAR(255),
    end_date VARCHAR(255),
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_accommodation foreign key(accommodation_id) references accommodations(id) on delete cascade
);

-- -- Adds records for testing -- -- 


-- -- Adds example users to table 

INSERT INTO users (name, email, password) VALUES ('Angie', 'Angie@example.com', 'changes');


-- -- Adds example accommodations to table 

INSERT INTO accommodations (place_name, host_id, img_path, description, price) VALUES ('Goldeneye', 1, 'static/assets/accomodation_images/img_1.jpg','insert thing here','£2000 Per Night');


-- -- Adds example listings to table 

INSERT INTO listings (user_id, accommodation_id, is_booked, start_date,end_date) VALUES (1, 1, TRUE,'10/10/2023','10/11/2023');