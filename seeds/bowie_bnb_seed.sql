

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
    start_date DATE,
    end_date DATE,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_accommodation foreign key(accommodation_id) references accommodations(id) on delete cascade
);

-- -- Adds records for testing -- -- 


-- -- Adds example users to table 

INSERT INTO users (name, email, password) VALUES
('Angie', 'Angie@example.com', 'changes'),
('Magie', 'magie56@example.com', 'september1'),
('Carol', 'ccarol.12@example.com', 'christmas'),
('Severus', 'severus.09@example.com', 'snape123'),
('Thomas', 'tom123@example.com', 'cooawl'),
('Joe', 'howyoudoing@example.com', 'friends'),
('Freddie', 'queens6@example.com', 'ilovemusic'),
('David', 'davi.d@example.com', 'password'),
('Karen', 'karen.mc0@example.com', 'mchammer'),
('Zack', 'zack.finley@example.com', 'traveller'),
('Monica', 'monica123@example.com', 'beverly321');

-- -- Adds example accommodations to table 

INSERT INTO accommodations (place_name, host_id, img_path, description, price) VALUES
('The Glass Jewel', 1, 'img_1.jpg','Nestled atop the hills of Beverly Hills, California.','£2000 Per Night'),
('The Floating Oasis', 2, 'img_2.jpg','Beautiful floating mansion with a retractable roof, Maldives.','£4000 Per Night'),
('The Treehouse Retreat', 3, 'img_3.jpg','Hidden in the lush rainforests of Costa Rica.','£1800 Per Night'),
('The Ice Palace', 4, 'img_4.jpg','An opulent space with a roaring fireplace in Aspen.', '£2480 Per Night'),
('The Sky Cathedral', 5, 'img_5.jpg','Atop a towering skyscraper in the heart of Dubai. ','£1800 Per Night'),
('The Floating Chateau', 6, 'img_6.jpg','Afloat on Lake Geneva, Switzerland.','£5500 Per Night'),
('The Cave Dwelling', 7, 'img_7.jpg','Carved into the cliffs of Santorini, Greece','£6000 Per Night'),
('The Timeless Castle', 8, 'img_8.jpg','Amid the rolling vineyards of Tuscany, Italy.','£2200 Per Night'),
('The Opulent Aerie', 9, 'img_9.jpg','Perched atop a gleaming skyscraper in the heart of New York City.','£2200 Per Night'),
('The Bash Mansion', 10, 'img_10.jpg','Situated in the heart of the lively Soho, London.','£2200 Per Night');

-- -- Adds example listings to table (dates are yyyy-mm-dd)

INSERT INTO listings (user_id, accommodation_id, is_booked, start_date,end_date) VALUES
(NULL, 1, FALSE,'2023-12-29','2023-12-30'),
(2, 2, TRUE,'2023-11-20','2023-11-27'),
(2, 5, TRUE,'2023-11-5','2023-11-10'),
(4, 3, FALSE,'2023-12-1','2023-12-7'),
(5, 4, TRUE,'2023-12-15','2023-12-29'),
(NULL, 6, FALSE,'2023-12-29','2023-12-30'),
(7, 7, TRUE,'2023-12-29','2023-12-30'),
(8, 8, FALSE,'2023-10-26','2023-10-30'),
(9, 9, TRUE,'2023-12-25','2023-12-30'),
(NULL, 10, FALSE,'2023-12-29','2023-12-30');