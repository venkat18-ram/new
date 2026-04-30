CREATE TABLE faculty(
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(20),
    gender VARCHAR(10),
    designation VARCHAR(20),
    salary INT,
    department_name VARCHAR(20),
    experience INT,
    contact INT
);

INSERT INTO faculty VALUES(513,'purushotham','male','proffessor',60000,'cse',6,4526532,'purushotham@gmail.com');
UPDATE faculty SET email='jplatha@gmail.com' WHERE faculty_id=509;

ALTER TABLE faculty ADD COLUMN email VARCHAR(40);
