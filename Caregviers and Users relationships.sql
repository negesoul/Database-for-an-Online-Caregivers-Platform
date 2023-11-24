-- Database: Assignment2

-- DROP DATABASE IF EXISTS "Assignment2";

CREATE DATABASE "Assignment2"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Kazakhstan.1251'
    LC_CTYPE = 'Russian_Kazakhstan.1251'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
-- Create the USER table
CREATE TABLE USERS (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    given_name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    profile_description TEXT,
    password VARCHAR(255) NOT NULL
);

-- Create the CAREGIVER table
CREATE TABLE CAREGIVER (
    caregiver_user_id SERIAL PRIMARY KEY,
    photo VARCHAR(255) NOT NULL, -- Assuming storing photos as binary data
    gender VARCHAR(10) NOT NULL,
    caregiving_type VARCHAR(255) NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL
);

-- Create the MEMBER table
CREATE TABLE MEMBERS (
    member_user_id SERIAL PRIMARY KEY,
    house_rules TEXT
);

-- Create the ADDRESS table
CREATE TABLE ADDRESS (
    member_user_id INT PRIMARY KEY REFERENCES MEMBERS(member_user_id),
    house_number VARCHAR(10) NOT NULL,
    street VARCHAR(255) NOT NULL,
    town VARCHAR(255) NOT NULL
);

-- Create the JOB table
CREATE TABLE JOB (
    job_id SERIAL PRIMARY KEY,
    member_user_id INT REFERENCES MEMBERS(member_user_id),
    required_caregiving_type VARCHAR(255) NOT NULL,
    other_requirements TEXT,
    date_posted DATE NOT NULL
);

-- Create the JOB_APPLICATION table
CREATE TABLE JOB_APPLICATION (
    caregiver_user_id INT REFERENCES CAREGIVER(caregiver_user_id),
    job_id INT REFERENCES JOB(job_id),
    date_applied DATE NOT NULL
);

-- Create the APPOINTMENT table
CREATE TABLE APPOINTMENT (
    appointment_id SERIAL PRIMARY KEY,
    caregiver_user_id INT REFERENCES CAREGIVER(caregiver_user_id),
    member_user_id INT REFERENCES MEMBERS(member_user_id),
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    work_hours INT NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Insert data into the USER table
INSERT INTO USERS (user_id, email, given_name, surname, city, phone_number, profile_description, password)
VALUES
    (718236, 'adil_zhalelov@musica36.kz', 'Adil', 'Zhalelov', 'Pavlodar', '+77777182366', 'Otets of his fans', 'AgaNu7182'),
    (104236, 'askha_prince@gmail.com', 'Askhat', 'Prince', 'Almaty', '+77771021122', 'Ya tebe ne friend', 'PustoiKvadrat'),
    (878245, 'awawa@gmail.com', 'Alice', 'Johnson', 'Astana', '+77071234578', 'Newly here, I am not local need babysitters.', 'password123'),
    (485675, 'daniel.financov@nu.edu.kz', 'Daniel', 'Financov', 'Astana', '+77079998877', 'Money money.', 'secret456'),
    (747848, 'wyw@gmail.com', 'Charlie', 'Williams', 'Astana', '+7707771548', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'pass789'),
    (123484, 'mlemc@gmail.com', 'David', 'Jones', 'Taldykorgan', '+77778521456', 'Abai Bol!', 'secure321'),
    (124785, 'okokokok@gmail.com', 'Eva', 'Ana', 'Taraz', '+77021234895', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', 'access678'),
    (415754, 'anadato@gmail.com', 'Frank', 'Davis', 'Astana', '+77071248954', 'Excepteur sint occaecat cupidatat non proident.', 'private987'),
    (123770, 'ef7777@gmail.com', 'Grace', 'Miller', 'Shiely', '+7778889990', 'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.', 'classified123'),
    (567423, 'futurer07@gmail.com', 'Jack', 'Sparrow', 'Astana', '+77781245874', 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.', 'hidden456'),
	(10, 'cg1@gmail.com', 'Almat', 'Deriev', 'Astana', '+77777184366', 'Prossional of his work.', '1234'),
	(23, 'cg2@gmail.com', 'Murat', 'Almat', 'Pavlodar', '+77771481122', 'Caregiving expert.', '1458'),
	(47, 'cg3@gmail.com', 'Makhambet', 'Askar', 'Almaty', '+77047234578', '2 years of experience.','2254848452'),
	(78, 'cg4@gmail.com', 'Maksat', 'Arman', 'Astana', '+77079492877', 'I have 10 certificates.', '484adw8'),
	(11, 'cg5@gmail.com', 'Marsen', 'Musahan', 'Astana', '+7704671548', 'Missian University Bachelor degree of caregiving.', 'pass7894848'),
	(65, 'cg6@gmail.com', 'Azat', 'Akash', 'Taraz', '+77778521486', 'I am father of 3 children.', 'secure321'),
	(44, 'cg7@gmail.com', 'Daiana', 'Ana', 'Shiely', '+77021236895', 'Mother of 5 angels.', '4dw84aw8d4'),
	(14, 'cg8@gmail.com', 'Dariya', 'Aman', 'Astana', '+77071295954', 'I have lots of friends under 10 years.', '4d84d82a'),
	(29, 'cg9@gmail.com', 'John', 'Bugatti', 'Taldykorgan', '+7788489990', 'Expert in the field currently in.', 'wwww wwww'),
    (31, 'cg10@gmail.com', 'Isabella', 'Google', 'Astana', '+77789945874', 'Please write any requirements and I will do it!', '4d8aw4d8___78a!')
    

-- Insert data into the CAREGIVER table for 10 caregivers
INSERT INTO CAREGIVER (caregiver_user_id, photo, gender, caregiving_type, hourly_rate)
VALUES
    (10, 'path/to/images.', 'Female', 'Elderly Care', 9.00),
    (23, 'path/to/images.', 'Male', 'Child Care', 15.50),
    (47, 'path/to/images.', 'Female', 'Special Needs Care', 18.75),
    (78, 'path/to/images.', 'Male', 'Pet Care', 12.00),
    (11, 'path/to/images.', 'Female', 'Housekeeping', 6.25),
    (65, 'path/to/images.', 'Male', 'Companion Care', 16.00),
    (44, 'path/to/images.', 'Female', 'Physical Therapy', 25.00),
    (14, 'path/to/images.', 'Male', 'Medical Care', 7.50),
    (29, 'path/to/images.', 'Female', 'Elderly Care', 22.50),
    (31, 'path/to/images.', 'Male', 'Child Care', 17.00);


-- Insert data into the MEMBER table for 10 members
INSERT INTO MEMBERS (member_user_id, house_rules)
VALUES
    (718236, 'No smoking in the house.'),
    (104236, 'Quiet hours after 10 PM.'),
    (878245, 'Allergies: no pets allowed.'),
    (485675, 'Keep common areas clean and tidy.'),
    (747848, 'Respect each other''s privacy.'),
    (123484, 'Vegetarian household.'),
    (124785, 'Guests allowed with prior notice.'),
    (415754,'No loud music or parties, no wake up after 7 p.m., no loud speaking, be polite.'),
    (123770, 'Shared grocery expenses.'),
    (567423, 'Weekly cleaning schedule.');


    -- Insert data into the ADDRESS table for 10 instances
INSERT INTO ADDRESS (member_user_id, house_number, street, town)
VALUES
    (718236, '777', 'Zharokova', 'Pavlodar'),
    (104236, '012', 'Mangilik', 'Almaty'),
    (878245, '125', 'Makhambet', 'Astana'),
    (485675, '114', 'Turan', 'Astana'),
    (747848, '052', 'Turan', 'Astana'),
    (123484, '071', 'Tauelsizdik', 'Taldykorgan'),
    (124785, '033', 'Turan', 'Taraz'),
    (415754, '505', 'Makhambet', 'Astana'),
    (123770, '457', 'mcr7', 'Shiely'),
    (567423, '717', 'Turan', 'Astana');

-- Insert data into the JOB table for 10 instances
INSERT INTO JOB (job_id, member_user_id, required_caregiving_type, other_requirements, date_posted)
VALUES
	(0, 718236, 'Elderly Care', 'Experience in similar roles', '2023-01-01'),
    (1, 104236, 'Child Care', 'First aid certification required', '2023-02-01'),
    (2, 878245, 'Special Needs Care', 'Experience with special needs children', '2023-03-01'),
    (3, 485675, 'Pet Care', 'Comfortable with various pets', '2023-04-01'),
    (4, 747848, 'Housekeeping', 'Experience in housekeeping', '2023-05-01'),
    (5, 123484, 'Companion Care', 'Friendly and sociable personality', '2023-06-01'),
    (6, 124785, 'Physical Therapy', 'Certified physical therapist required', '2023-07-01'),
    (7, 415754, 'Medical Care', 'Medical certification required', '2023-08-01'),
    (8, 123770, 'Elderly Care', 'Experience in tutoring children', '2023-09-01'),
    (9, 567423, 'Child Care', 'Valid driver''s license required', '2023-10-01');
	

-- Insert data into the JOB_APPLICATION table for 10 instances
INSERT INTO JOB_APPLICATION (caregiver_user_id, job_id, date_applied)
VALUES
	(10, 0, '2023-01-05'),
    (23, 1, '2023-02-10'),
    (47, 2, '2023-03-15'),
    (78, 3, '2023-04-20'),
    (11, 4, '2023-05-25'),
    (65, 5, '2023-06-30'),
    (44, 6, '2023-07-05'),
    (14, 7, '2023-08-10'),
    (29, 8, '2023-09-15'),
    (31, 9, '2023-10-20');


-- Insert data into the APPOINTMENT table for 10 instances
INSERT INTO APPOINTMENT (appointment_id, caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status)
VALUES
    (101, 10, 718236, '2023-01-10', '10:00:00', 4, 'Accepted'),
    (102, 23, 104236, '2023-02-15', '15:30:00', 3, 'Accepted'),
    (112, 47, 878245, '2023-03-20', '12:00:00', 5, 'Pending'),
    (127, 78, 485675, '2023-04-25', '08:00:00', 8, 'Declined'),
    (147, 11, 747848, '2023-05-30', '14:45:00', 6, 'Accepted'),
    (331, 65, 123484, '2023-06-05', '18:30:00', 7, 'Pending'),
    (122, 44, 124785, '2023-07-10', '09:15:00', 4, 'Accepted'),
    (222, 14, 415754, '2023-08-15', '11:30:00', 5, 'Pending'),
    (777, 29, 123770, '2023-09-20', '13:45:00', 6, 'Declined'),
    (179, 31, 567423, '2023-10-25', '16:00:00', 7, 'Accepted');

-- -- Drop the JOB_APPLICATION table
-- DROP TABLE JOB_APPLICATION CASCADE;

-- -- Drop the APPOINTMENT table
-- DROP TABLE APPOINTMENT CASCADE;

-- -- Drop the JOB table
-- DROP TABLE JOB CASCADE;

-- -- Drop the ADDRESS table
-- DROP TABLE ADDRESS CASCADE;

-- -- Drop the MEMBER table
-- DROP TABLE MEMBERS CASCADE;

-- -- Drop the CAREGIVER table
-- DROP TABLE CAREGIVER CASCADE;

-- -- Drop the USERS table
-- DROP TABLE users CASCADE;


SELECT *FROM users;
SELECT *FROM caregiver;
SELECT *FROM MEMBERS;
SELECT *FROM ADDRESS;
SELECT *FROM JOB;
SELECT *FROM JOB_APPLICATION;
SELECT *FROM APPOINTMENT;