CREATE TABLE kvsrit.students AS
SELECT * FROM mysql.student;

CREATE TABLE kvsrit.faculty AS
SELECT * FROM mysql.faculty;

CREATE DATABASE kvsrit;

BACKUP DATABASE kvsrit
TO DISK = 'E:\databases\kvsrit.bak';