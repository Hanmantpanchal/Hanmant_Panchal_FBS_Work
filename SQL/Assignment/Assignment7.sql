Q1) Start a transaction and insert a new member record into Member table.
Save the changes permanently.

Ans:


START TRANSACTION;

INSERT INTO Member
(Member_Id, Member_Name, Member_Type, Acc_Open_Date,
 Membership_Fees, Penalty_Amount, Max_Books_Allowed)
VALUES
(201, 'Rahul Patil', 'Lifetime', '2026-08-31',
 500, 0, 5);

COMMIT;



Q2) Start a transaction and insert a new book record into Books table.
Undo the insertion using rollback.


Ans :


START TRANSACTION;

INSERT INTO Books
(Book_No, Book_Name, Author_Name, Cost, Category)
VALUES
(501, 'Python Programming', 'John Smith', 600, 'Programming');

ROLLBACK;



Q3) Start a transaction and update Penalty_Amount of a member.
Create a savepoint before update, then rollback to the savepoint.

Ans :

START TRANSACTION;

SAVEPOINT before_penalty_update;

UPDATE Member
SET Penalty_Amount = 100
WHERE Member_Id = 101;

ROLLBACK TO SAVEPOINT before_penalty_update;

COMMIT;


Q4) Start a transaction and perform the following steps:
- Issue a book to a member (insert into Issue table)
- Update the Max_Books_Allowed count of that member
Commit the transaction only if both operations succeed.

Ans :


START TRANSACTION;

INSERT INTO Issue
(Lib_Issue_Id, Book_No, Member_Id, Issue_Date, Return_Date)
VALUES
(8001, 101, 201, '2026-08-31', NULL);

UPDATE Member
SET Max_Books_Allowed = Max_Books_Allowed - 1
WHERE Member_Id = 201;

COMMIT;


Q5) Start a transaction and perform the following:
- Update the cost of a book
- Create a savepoint
- Delete one issue record
Rollback only the delete operation using savepoint.

Ans :


START TRANSACTION;

UPDATE Books
SET Cost = 700
WHERE Book_No = 101;

SAVEPOINT before_delete;

DELETE FROM Issue
WHERE Lib_Issue_Id = 8001;

ROLLBACK TO SAVEPOINT before_delete;

COMMIT;



Q6) Demonstrate that after COMMIT, rollback cannot undo the changes.

Ans :

START TRANSACTION;

INSERT INTO Member
(Member_Id, Member_Name, Member_Type, Acc_Open_Date,
 Membership_Fees, Penalty_Amount, Max_Books_Allowed)
VALUES
(202, 'Amit Sharma', 'Annual', '2026-08-31',
 300, 0, 3);

COMMIT;


Q7) Demonstrate that SAVEPOINT allows partial rollback inside a transaction.

Ans:

START TRANSACTION;

UPDATE Books
SET Cost = 800
WHERE Book_No = 101;

SAVEPOINT sp1;

UPDATE Books
SET Cost = 900
WHERE Book_No = 102;

ROLLBACK TO SAVEPOINT sp1;

COMMIT;





