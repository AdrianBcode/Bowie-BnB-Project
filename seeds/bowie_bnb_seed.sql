

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
INSERT INTO users (name, email, password) VALUES('Angie', 'Angie@example.com', 'changes');
INSERT INTO users (name, email, password) VALUES('Magie', 'magie56@example.com', 'september1');
INSERT INTO users (name, email, password) VALUES('Carol', 'ccarol.12@example.com', 'christmas');
INSERT INTO users (name, email, password) VALUES('Severus', 'severus.09@example.com', 'snape123');
INSERT INTO users (name, email, password) VALUES('Thomas', 'tom123@example.com', 'cooawl');
INSERT INTO users (name, email, password) VALUES('Joe', 'howyoudoing@example.com', 'friends');
INSERT INTO users (name, email, password) VALUES('Freddie', 'queens6@example.com', 'ilovemusic');
INSERT INTO users (name, email, password) VALUES('David', 'davi.d@example.com', 'password');
INSERT INTO users (name, email, password) VALUES('Karen', 'karen.mc0@example.com', 'mchammer');
INSERT INTO users (name, email, password) VALUES('Zack', 'zack.finley@example.com', 'traveller');
INSERT INTO users (name, email, password) VALUES('Monica', 'monica123@example.com', 'beverly321');

-- -- Adds example accommodations to table 

INSERT INTO accommodations (place_name, host_id, img_path, description, price) 
VALUES ('The Glass Jewel', 1, ' ','Nestled atop the hills of Beverly Hills, California.','£2000 Per Night');
VALUES ('The Floating Oasis', 2, ' ','Beautiful floating mansion with a retractable roof, Maldives.','£4000 Per Night');
VALUES ('The Treehouse Retreat', 3, ' ','Hidden in the lush rainforests of Costa Rica.','£1800 Per Night');
VALUES ('The Ice Palace', 4, ' ','An opulent space with a roaring fireplace in Aspen.', '£2480 Per Night');
VALUES ('The Sky Cathedral', 5, ' ','Atop a towering skyscraper in the heart of Dubai. ','£1800 Per Night');
VALUES ('The Floating Chateau', 6, ' ','Afloat on Lake Geneva, Switzerland.','£5500 Per Night');
VALUES ('The Cave Dwelling', 7, ' ','Carved into the cliffs of Santorini, Greece','£6000 Per Night');
VALUES ('The Timeless Castle', 8, ' ','Amid the rolling vineyards of Tuscany, Italy.','£2200 Per Night');
VALUES ('The Opulent Aerie', 9, ' ','Perched atop a gleaming skyscraper in the heart of New York City.','£2200 Per Night');
VALUES ('The Bash Mansion', 10, ' ','Situated in the heart of the lively Soho, London.','£2200 Per Night')

-- -- Adds example listings to table 

INSERT INTO listings (user_id, accommodation_id, is_booked, start_date,end_date) 
VALUES (1, 1, TRUE,'21/12/2023','30/12/2023');
VALUES (2, 2, TRUE,'06/09/2023','13/09/2023');
VALUES (2, 5, TRUE,'07/04/2023','15/04/2023');
VALUES (4, 3, FALSE,'01/10/2023','10/10/2023');
VALUES (5, 4, TRUE,'03/05/2023','03/06/2023');
VALUES (6, 6, TRUE,'10/06/2023','10/07/2023');
VALUES (7, 7, TRUE,'10/10/2023','10/11/2023');
VALUES (8, 8, FALSE,'10/10/2023','10/11/2023');
VALUES (9, 9, TRUE,'10/10/2023','10/11/2023');
VALUES (NULL, 10, FALSE,'10/10/2023','10/11/2023');

