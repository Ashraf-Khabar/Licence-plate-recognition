-- Creation of user named radar :
alter session set "_ORACLE_SCRIPT"=true ;
create user radar identified by radarpw ;

-- Grating the privileges to the user radar :
grant dba, connect, resource to radar ;

-- Connect to radar :
connect radar/radarpw ;

-- Creation of the table named users :
create table users
(
    user_id number primary key not null,
    user_name varchar2(100) not null,
    user_mail varchar2(50) not null unique,
    user_licence_plate varchar2(50) unique,
    user_city varchar2(50),
    user_car_type varchar2(50)
);

-- Bitmap index for column 'user_city' :
create bitmap index INDEX_CITY on users(user_city);

-- Describing the table :
desc users ;

-- Felling the database with a data in order to test :
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (1, 'John Doe', 'johndoe@example.com', 'AB-123-CD', 'Paris', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (2, 'Jane Doe', 'janedoe@example.com', 'BC-234-DE', 'Lyon', 'Sedan');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (3, 'Bob Smith', 'bobsmith@example.com', 'CD-345-EF', 'Marseille', 'Hatchback');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (4, 'Alice Johnson', 'alicejohnson@example.com', 'DE-456-FG', 'Nice', 'Coupe');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (5, 'Peter Brown', 'peterbrown@example.com', 'EF-567-GH', 'Toulouse', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (6, 'Emily Wilson', 'emilywilson@example.com', 'FG-678-HI', 'Bordeaux', 'Sedan');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (7, 'David Lee', 'davidlee@example.com', 'GH-789-IJ', 'Strasbourg', 'Hatchback');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (8, 'Maria Garcia', 'mariagarcia@example.com', 'HI-890-JK', 'Lille', 'Coupe');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (9, 'Michael Davis', 'michaeldavis@example.com', 'IJ-901-KL', 'Nantes', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (10, 'Sophie Martin', 'sophiemartin@example.com', 'KL-012-LM', 'Rennes', 'Sedan');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (11, 'Adam Wilson', 'adamwilson@example.com', 'LM-123-MN', 'Grenoble', 'Hatchback');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (12, 'Julia Brown', 'juliabrown@example.com', 'MN-234-NO', 'Montpellier', 'Coupe');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (13, 'Thomas Garcia', 'thomasgarcia@example.com', 'NO-345-OP', 'Nancy', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (21, 'Gabriel Martin', 'gabrielmartin@example.com', 'VW-123-WX', 'Lyon', 'Hatchback');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (22, 'Sarah Kim', 'sarahkim@example.com', 'WX-234-XY', 'Marseille', 'Coupe');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (23, 'Ryan Chen', 'ryanchen@example.com', 'XY-345-YZ', 'Nice', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (24, 'Mia Thompson', 'miathompson@example.com', 'YZ-456-ZA', 'Toulouse', 'Sedan');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (25, 'Ethan Wilson', 'ethanwilson@example.com', 'ZA-567-AB', 'Bordeaux', 'Hatchback');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (26, 'Hannah Davis', 'hannahdavis@example.com', 'AB-678-BC', 'Strasbourg', 'Coupe');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (27, 'Matthew Johnson', 'matthewjohnson@example.com', 'BC-789-CD', 'Lille', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (28, 'Ava Brown', 'avabrown@example.com', 'CD-890-DE', 'Nantes', 'Sedan');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (29, 'Daniel Lee', 'daniellee@example.com', 'DE-901-EF', 'Rennes', 'Hatchback');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (30, 'Ella Wilson', 'ellawilson@example.com', 'EF-012-FG', 'Grenoble', 'Coupe');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (31, 'Liam Smith', 'liamsmith@example.com', 'FG-123-GH', 'Montpellier', 'SUV');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (32, 'Victoria Martin', 'victoriamartin@example.com', 'GH-234-HI', 'Nancy', 'Sedan');
INSERT INTO users (user_id, user_name, user_mail, user_licence_plate, user_city, user_car_type)
VALUES (33, 'Noah Davis', 'noahdavis@example.com', 'HI-345-IJ', 'Angers', 'Sedan');

-- Committing the transactions :
commit ;

-- selecting from the table :
select * from users ;

/* Creation of triggers : */

-- Autoincrement id trigger
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER user_id_trigger
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
     SELECT user_id_seq.NEXTVAL
     INTO :new.user_id
     FROM dual;
 END;
 /