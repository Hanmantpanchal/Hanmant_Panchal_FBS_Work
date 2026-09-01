Q1) Write an SQL query to create a view named Book_List that displays the following columns
from Books table:
Book_No, Book_Name, Author_Name, Cost, Category.

Ans :

CREATE VIEW Book_List AS
SELECT Book_No,
       Book_Name,
       Author_Name,
       Cost,
       Category
FROM Books;


Q2) Write an SQL query to display all records from the view Book_List.

Ans:

SELECT *
FROM Book_List;



Q3) Write an SQL query to create a view named Issued_Books that displays details of all books
that are currently issued
(books whose Return_Date is NULL).
Output columns should include:
Lib_Issue_Id, Book_No, Member_Id, Issue_Date.

Ans :


CREATE VIEW Issued_Books AS
SELECT Lib_Issue_Id,
       Book_No,
       Member_Id,
       Issue_Date
FROM Issue
WHERE Return_Date IS NULL;




Q4) Write an SQL query to display all records from the view Issued_Books.

Ans :


SELECT *
FROM Issued_Books;



Q5) Write an SQL query to create a view named Member_Penalty that displays Member_Id,
Member_Name, Penalty_Amount
for members whose Penalty_Amount is greater than 0.

Ans :


CREATE VIEW Member_Penalty AS
SELECT Member_Id,
       Member_Name,
       Penalty_Amount
FROM Member
WHERE Penalty_Amount > 0;




Q6) Write an SQL query to display all records from the view Member_Penalty.

Ans :

SELECT *
FROM Member_Penalty;


Q7) Write an SQL query to update the Penalty_Amount of a member using the Member_Penalty
view.

Ans :

UPDATE Member_Penalty
SET Penalty_Amount = 100
WHERE Member_Id = 101;


Q8) Write an SQL query to create a view named Book_Issue_Details that displays:
Book_Name, Member_Name, Issue_Date, Return_Date
by joining Books, Member, and Issue tables.

Ans :

CREATE VIEW Book_Issue_Details AS
SELECT B.Book_Name,
       M.Member_Name,
       I.Issue_Date,
       I.Return_Date
FROM Books B
JOIN Issue I
ON B.Book_No = I.Book_No
JOIN Member M
ON I.Member_Id = M.Member_Id;


Q9) Write an SQL query to display Book_Name, Member_Name, Issue_Date from the view
Book_Issue_Details.

Ans :

SELECT Book_Name,
       Member_Name,
       Issue_Date
FROM Book_Issue_Details;



Q10) Write an SQL query to drop the view Issued_Books.

Ans :

DROP VIEW Issued_Books;


Q11) Write an SQL query to drop the view Member_Penalty.

Ans :

DROP VIEW Member_Penalty;

Q12) Write an SQL query to drop the view Book_Issue_Details.

Ans:

DROP VIEW Book_Issue_Details;



