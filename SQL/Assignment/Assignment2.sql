Assignment 2 :

Q1) Create the tables Member, Books, and Issue WITHOUT constraints.

1)Member table :

CREATE TABLE Member (
    Member_Id INT,
    Member_Name VARCHAR(30),
    Member_Address VARCHAR(50),
    Acc_Open_Date DATE,
    Membership_Type VARCHAR(20),
    Fees_Paid DECIMAL(10,2),
    Max_Books_Allowed INT,
    Penalty_Amount DECIMAL(10,2)
);


2)Books table :

CREATE TABLE Books (
    Book_No INT,
    Book_Name VARCHAR(30),
    Author_Name VARCHAR(30),
    Cost DECIMAL(10,2),
    Category VARCHAR(15)
);


3)issue table :

CREATE TABLE Issue (
    Lib_Issue_Id INT,
    Book_No INT,
    Member_Id INT,
    Issue_Date DATE,
    Return_Date DATE
);


Q2) Display the structure of all three tables using DESC.

DESC Member;
DESC Books;
DESC Issue;



Q3) Drop the Member table.

DROP TABLE Member;


Q4) Create the Member table again with these constraints:
- Member_Id must be PRIMARY KEY
- Membership_Type must allow only:
('Lifetime','Annual','Half Yearly','Quarterly')



Ans :

CREATE TABLE Member (
    Member_Id INT PRIMARY KEY,
    Member_Name VARCHAR(30),
    Member_Address VARCHAR(50),
    Acc_Open_Date DATE,
    Membership_Type VARCHAR(20)
        CHECK (Membership_Type IN ('Lifetime', 'Annual', 'Half Yearly', 'Quarterly')),
    Fees_Paid DECIMAL(10,2),
    Max_Books_Allowed INT,
    Penalty_Amount DECIMAL(10,2)
);


Q5) Alter Member table to increase Member_Name size from 30 to 40.

Ans : 

ALTER TABLE Member
MODIFY Member_Name VARCHAR(40);


Q6) Add a column Reference (VARCHAR (30)) to Issue table.

Ans :

ALTER TABLE Issue
ADD Reference VARCHAR(30);

Q7)Drop the column Reference from Issue table.

Ans :

ALTER TABLE Issue
DROP COLUMN Reference;


Q8)Rename the table Issue to Lib_Issue.

Ans :

RENAME TABLE Issue TO Lib_Issue;


Q9)Insert the following records into Member table:

Ans :

INSERT INTO Member
VALUES
(1, 'Richa Sharma', 'Pune', '2012-10-05', 'Lifetime', 25000, 5, 50),
(2, 'Richa Sen', 'Pune', CURDATE(), 'Annual', 1000, 3, NULL);


Q10)Insert at least 5 more records with suitable data into Member table.

Ans :

INSERT INTO Member
VALUES
(3, 'Amit Patil', 'Mumbai', '2023-01-15', 'Quarterly', 1500, 3, 0),
(4, 'Sneha Joshi', 'Nashik', '2023-03-20', 'Annual', 1000, 5, 25),
(5, 'Rahul Deshmukh', 'Pune', '2024-06-10', 'Half Yearly', 3000, 4, 0),
(6, 'Priya Kulkarni', 'Kolhapur', '2024-08-25', 'Lifetime', 25000, 5, 100),
(7, 'Akash More', 'Latur', '2025-02-12', 'Quarterly', 1500, 3, 50);


Q11) Try to decrease Member_Name size from 40 to 20.
If it fails, mention the reason.

Ans :

The column cannot be reduced to VARCHAR(20) because existing data may contain values longer than 20 characters. Reducing the size could cause data truncation.

Q12) Add a CHECK constraint:
Max_Books_Allowed must be less than 100.

Ans :

ALTER TABLE Member
ADD CONSTRAINT chk_max_books
CHECK (Max_Books_Allowed < 100);


Q13) Create a backup table named MemberBackup using the Member table.
Use the following query:
CREATE TABLE MemberBackup AS
SELECT * FROM Member;


Ans :

CREATE TABLE MemberBackup AS
SELECT * FROM Member;


Q14) Add named constraints:
- Max_Books_Allowed < 100
- Penalty_Amount <= 1000


Ans :

ALTER TABLE Member
ADD CONSTRAINT chk_max_books
CHECK (Max_Books_Allowed < 100),
ADD CONSTRAINT chk_penalty
CHECK (Penalty_Amount <= 1000);


Q15) Drop the Books table.

Ans :

DROP TABLE Books;


Q16) Create Books table again with constraints:
- Book_No PRIMARY KEY
- Book_Name NOT NULL
- Category must be one of:
('System','Fiction','Database','RDBMS','Others','Science')


Ans :

CREATE TABLE Books (
    Book_No INT PRIMARY KEY,
    Book_Name VARCHAR(30) NOT NULL,
    Author_Name VARCHAR(30),
    Cost DECIMAL(10,2),
    Category VARCHAR(15)
        CHECK (Category IN ('System', 'Fiction', 'Database', 'RDBMS', 'Others', 'Science'))
);


Q17) Insert the given data into Books table

Ans :

INSERT INTO Books
VALUES
(101, 'Let Us C', 'Denis Ritchie', 450, 'System'),
(102, 'Oracle Complete Ref', 'Loni', 550, 'Database'),
(103, 'Mastering SQL', 'Loni', 250, 'Database'),
(104, 'PL SQL Ref', 'Scott Urman', 750, 'Database'),
(105, 'National Geographic', 'Adis Scott', 1000, 'Science');



Q18)Insert at least 5 more records into Books table.

Ans :

INSERT INTO Books
VALUES
(106, 'Python Programming', 'Mark Lutz', 650, 'System'),
(107, 'The Alchemist', 'Paulo Coelho', 400, 'Fiction'),
(108, 'SQL Fundamentals', 'John Smith', 550, 'RDBMS'),
(109, 'Data Science Basics', 'Jake VanderPlas', 800, 'Science'),
(110, 'Database Concepts', 'Korth', 700, 'Database');


Q19) View all data from Member and Books tables using SELECT.


Ans :

SELECT * FROM Member;
SELECT * FROM Books;


Q20) Drop Lib_Issue table.


Ans :

DROP TABLE Lib_Issue;


Q21) Create Issue table again with constraints:
- Lib_Issue_Id PRIMARY KEY
- Book_No FOREIGN KEY REFERENCES Books(Book_No)
- Member_Id FOREIGN KEY REFERENCES Member(Member_Id)


Ans :

CREATE TABLE Issue (
    Lib_Issue_Id INT PRIMARY KEY,
    Book_No INT,
    Member_Id INT,
    FOREIGN KEY (Book_No) REFERENCES Books(Book_No),
    FOREIGN KEY (Member_Id) REFERENCES Member(Member_Id)
);



Q22) Insert the following records into Issue table

Ans :

INSERT INTO Issue (Lib_Issue_Id, Book_No, Member_Id, Issue_Date)
VALUES
(7001, 101, 1, '2024-12-10'),
(7002, 102, 2, '2024-12-15'),
(7003, 104, 1, '2025-01-15'),
(7004, 101, 1, '2025-02-04'),
(7005, 104, 2, '2025-03-15'),
(7006, 101, 3, '2025-04-18');


Q23) Try inserting an Issue record with Member_Id not existing in Member table.
Observe and write the error.

Ans :

ERROR 1452 (23000): Cannot add or update a child row:
a foreign key constraint fails

Q24) Try deleting Member_Id = 1 from Member table.
Observe and write the foreign key error.

Ans :

ERROR 1451 (23000): Cannot delete or update a parent row:
a foreign key constraint fails



Q25) Update Return_Date for Issue_Id 7004 and 7005 to 15 days after Issue_Date.


Ans :

UPDATE Issue
SET Return_Date = DATE_ADD(Issue_Date, INTERVAL 15 DAY)
WHERE Lib_Issue_Id IN (7004, 7005);


Q26) Delete all Issue records where Member_Id = 1 and Issue_Date is before '2006-12-10'.

Ans :

DELETE FROM Issue
WHERE Member_Id = 1
AND Issue_Date < '2006-12-10';


Q27) Delete all Books where Category is not Database or RDBMS.

Ans :
DELETE FROM Books
WHERE Category NOT IN ('Database', 'RDBMS');



Q28) Drop all three tables: Issue, Member, Books.

Ans :

DROP TABLE Issue;
DROP TABLE Member;
DROP TABLE Books;







