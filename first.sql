CREATE TABLE student{
    s_id PRIMARY KEY INT,
    s_name VARCHAR2(30),
    s_gae INT,
    s_marks INT
};
INSERT INTO student VALUES(101,'venkat',20,92);
INSERT INTO student VALUES(102,'suhail',20,90);
INSERT INTO student VALUES(103,'sadiq',20,92);
INSERT INTO student VALUES(104,'jahash',20,96);
INSERT INTO student VALUES(105,'shiva',20,70);
INSERT INTO student VALUES(106,'M shiva',20,89);
INSERT INTO student VALUES(107,'vardhan',20,90);
INSERT INTO student VALUES(108,'bansi',20,85);
INSERT INTO student VALUES(109,'raghu',20,83);
INSERT INTO student VALUES(110,'khaiser',20,95);
INSERT INTO student VALUES(111,'affan',20,86);

INSERT INTO CSEC VALUES(101,'venkat','C',20,92);


-- UPDATE s_marks=99 FROM student WHERE s_id=104;

