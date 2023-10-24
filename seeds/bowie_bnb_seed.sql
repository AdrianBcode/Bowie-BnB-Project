

--  Drop users table and it's sequence (if they exist)
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


--  Drop accommodations table and it's sequence (if they exist)
DROP TABLE IF EXISTS accommodations;
DROP SEQUENCE IF EXISTS accommodations_id_seq;

--  Drop bookings table and it's sequence (if they exist)
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;



--  Creates users table
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255)
);

--  Creates accommodation table
CREATE SEQUENCE IF NOT EXISTS accommodations_id_seq;
CREATE TABLE accommodations (
    id SERIAL PRIMARY KEY,
    place_name VARCHAR(255),
    start_date VARCHAR(255),
    end_date VARCHAR(255),
    host_id int
);

--  Creates bookings table
CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id int,
    accommodation_id int,
    is_booked BOOLEAN
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
    constraint fk_accommodation foreign key(accommodation_id) references accommodations(id) on delete cascade
);
