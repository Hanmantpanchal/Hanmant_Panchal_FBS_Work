Assignment 5:

1) List all the books that are written by Author Loni and has price
less then 600.

Ans :

SELECT *
FROM Books
WHERE Author = 'Loni'
AND Price < 600;



2) List the Issue details for the books that are not returned yet.

Ans:

SELECT *
FROM Issue
WHERE Return_Date IS NULL;


3) Update all the blank return_date with 31-Dec-06 excluding 7005
and 7006.

Ans :

UPDATE Issue
SET Return_Date = '2006-12-31'
WHERE Return_Date IS NULL
AND Lib_Issue_Id NOT IN (7005, 7006);


4) List all the Issue details that have books issued for more then 30
days.

Ans :

SELECT *
FROM Issue
WHERE DATEDIFF(Return_Date, Issue_Date) > 30;


5) List all the books that have price in range of 500 to 750 and has
category as Database.

Ans :

SELECT *
FROM Books
WHERE Price BETWEEN 500 AND 750
AND Category = 'Database';


6) List all the books that belong to any one of the following
categories Science, Database, Fiction, Management.

Ans :

SELECT *
FROM Books
WHERE Category IN ('Science', 'Database', 'Fiction', 'Management');

7) List all the members in the descending order of Penalty due on
them.

Ans :

SELECT *
FROM Member
ORDER BY Penalty DESC;

8) Modify the price of book with id 103 to Rs 300 and category to

RDBMS.

Ans :

UPDATE Books
SET Price = 300,
    Category = 'RDBMS'
WHERE Book_Id = 103;


9) List all the books in ascending order of category and descending

order of price.


Ans :

SELECT *
FROM Books
ORDER BY Category ASC,
         Price DESC;


10) List all the books that contain word SQL in the name of the book.

Ans:

SELECT *
FROM Books
WHERE Book_Name LIKE '%SQL%';

11) List the Lib_Issue_Id, Issue_Date, Return_Date and No of days
Book was issued.

Ans :

SELECT Lib_Issue_Id,
       Issue_Date,
       Return_Date,
       DATEDIFF(Return_Date, Issue_Date) AS No_Of_Days
FROM Issue;


12) Find the details of the member of the Library in the order of their

joining the library.

Ans :

SELECT *
FROM Member
ORDER BY Joining_Date ASC;


13) Display the count of total no of books issued to Member 101.

Ans :

SELECT COUNT(*) AS Total_Books_Issued
FROM Issue
WHERE Member_Id = 101;


14) Display the total penalty due for all the members.

Ans :

SELECT SUM(Penalty) AS Total_Penalty
FROM Member;



15) Display the total no of members

Ans :
SELECT COUNT(*) AS Total_Members
FROM Member;

16) Display the total no of books issued

Ans :
SELECT COUNT(*) AS Total_Books_Issued
FROM Issue;

17) Display the average membership fees paid by all the members

Ans :

SELECT AVG(Membership_Fees) AS Average_Membership_Fees
FROM Member;


18) List the various categories and count of books in each category.

Ans :
SELECT Category,
       COUNT(*) AS Book_Count
FROM Book
GROUP BY Category;

19) List the book_No and the number of times the book is issued in the
descending order of count.

Ans :

SELECT Book_No,
       COUNT(*) AS Issue_Count
FROM Issue
GROUP BY Book_No
ORDER BY Issue_Count DESC;

20) Find the maximum, minimum, total and average penalty amount in
the member table.

Ans :

SELECT MAX(Penalty_Amount) AS Maximum_Penalty,
       MIN(Penalty_Amount) AS Minimum_Penalty,
       SUM(Penalty_Amount) AS Total_Penalty,
       AVG(Penalty_Amount) AS Average_Penalty
FROM Member;



21) Display the member id and the no of books for each member that
has issued more then 2 books.

Ans :
SELECT Member_Id,
       COUNT(*) AS No_Of_Books
FROM Issue
GROUP BY Member_Id
HAVING COUNT(*) > 2;


22) Display the member id, book no and no of times the same book is
issued by the member in the descending order of count.

Ans :

SELECT Member_Id,
       Book_No,
       COUNT(*) AS Issue_Count
FROM Issue
GROUP BY Member_Id, Book_No
ORDER BY Issue_Count DESC;


23) Display the month and no of books issued each month in the
descending order of count.

Ans :
SELECT MONTH(Issue_Date) AS Month,
       COUNT(*) AS No_Of_Books
FROM Issue
GROUP BY MONTH(Issue_Date)
ORDER BY No_Of_Books DESC;


24) List the book_no of all the books that are not issued to any

member so far.

Ans :

SELECT Book_No
FROM Book
WHERE Book_No NOT IN
(
    SELECT Book_No
    FROM Issue
);


25) List all the member id that exist in member table and has also at
least one book issued by them.

Ans :

SELECT DISTINCT M.Member_Id
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id;


26) List the member ID with highest and lowest no of books issued.

Ans :

SELECT Member_Id,
       COUNT(*) AS No_Of_Books
FROM Issue
GROUP BY Member_Id
ORDER BY No_Of_Books DESC
LIMIT 1;




For lowest:

SELECT Member_Id,
       COUNT(*) AS No_Of_Books
FROM Issue
GROUP BY Member_Id
ORDER BY No_Of_Books ASC
LIMIT 1;


27) List all the Issue_details for books issued in December and July

Ans :

SELECT *
FROM Issue
WHERE MONTHNAME(Issue_Date) IN ('December', 'July');

28) List the Book_No, Book_Name and Issue_date for all the books
that are issued in month of December and belong to category Database.

Ans :

SELECT B.Book_No,
       B.Book_Name,
       I.Issue_Date
FROM Book B
JOIN Issue I
ON B.Book_No = I.Book_No
WHERE MONTH(I.Issue_Date) = 12
AND B.Category = 'Database';



29) List the Member Id, Member Name and max books allowed in the
descending order of the max books allowed.

Ans :

SELECT Member_Id,
       Member_Name,
       Max_Books_Allowed
FROM Member
ORDER BY Max_Books_Allowed DESC;



30) List the Book No, Book Name, Issue_date and Return_Date for all
the books issued by Richa Sharma.

Ans :

SELECT B.Book_No,
       B.Book_Name,
       I.Issue_Date,
       I.Return_Date
FROM Book B
JOIN Issue I
ON B.Book_No = I.Book_No
JOIN Member M
ON I.Member_Id = M.Member_Id
WHERE M.Member_Name = 'Richa Sharma';


31) List the details of all the members that have issued books in
Database category.

Ans :

SELECT DISTINCT M.*
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
JOIN Book B
ON I.Book_No = B.Book_No
WHERE B.Category = 'Database';


32) List all the books that have highest price in their own category.

Ans :

SELECT *
FROM Book B
WHERE Price =
(
    SELECT MAX(Price)
    FROM Book
    WHERE Category = B.Category
);

33) List all the Issue_Details where Issue_date is not within the
Acc_open_date and Return_date for that member.

Ans :

SELECT I.*
FROM Issue I
JOIN Member M
ON I.Member_Id = M.Member_Id
WHERE I.Issue_Date NOT BETWEEN M.Acc_Open_Date
                            AND I.Return_Date;


34) List all the members that have not issued a single book so far.

Ans :

SELECT M.*
FROM Member M
LEFT JOIN Issue I
ON M.Member_Id = I.Member_Id
WHERE I.Member_Id IS NULL;


35) List all the members that have issued the same book as issued by
Garima.

Ans :

SELECT DISTINCT M.Member_Id,
       M.Member_Name
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
WHERE I.Book_No IN
(
    SELECT I2.Book_No
    FROM Issue I2
    JOIN Member M2
    ON I2.Member_Id = M2.Member_Id
    WHERE M2.Member_Name = 'Garima'
);


36) List the Book_Name, Price of all the books that are not returned
for more then 30 days.

Ans :
SELECT B.Book_Name,
       B.Price
FROM Book B
JOIN Issue I
ON B.Book_No = I.Book_No
WHERE I.Return_Date IS NULL
AND DATEDIFF(CURDATE(), I.Issue_Date) > 30;

37) List all the authors and book_name that has more then 1 book
written by them.

Ans :

SELECT Author,
       Book_Name
FROM Book
WHERE Author IN
(
    SELECT Author
    FROM Book
    GROUP BY Author
    HAVING COUNT(*) > 1
);


38) List the Member ID, Member Name of the people that have issued
the highest and the lowest no of books.

Ans :

SELECT M.Member_Id,
       M.Member_Name,
       COUNT(I.Book_No) AS No_Of_Books
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
GROUP BY M.Member_Id, M.Member_Name
HAVING COUNT(I.Book_No) = 
       (SELECT MAX(Book_Count)
        FROM
        (
            SELECT COUNT(*) AS Book_Count
            FROM Issue
            GROUP BY Member_Id
        ) AS T1)
OR COUNT(I.Book_No) =
       (SELECT MIN(Book_Count)
        FROM
        (
            SELECT COUNT(*) AS Book_Count
            FROM Issue
            GROUP BY Member_Id
        ) AS T2);


39) List the details of highest 3 priced books.

Ans :

SELECT *
FROM Book
ORDER BY Price DESC
LIMIT 3;


40) List the total cost of all the books that are currently issued but not
returned.

Ans :

SELECT SUM(B.Price) AS Total_Cost
FROM Book B
JOIN Issue I
ON B.Book_No = I.Book_No
WHERE I.Return_Date IS NULL;

41) List the details of the book that has been issued maximum no of
times.

Ans :

SELECT B.*,
       COUNT(I.Book_No) AS Issue_Count
FROM Book B
JOIN Issue I
ON B.Book_No = I.Book_No
GROUP BY B.Book_No,
         B.Book_Name,
         B.Author,
         B.Price,
         B.Category
ORDER BY Issue_Count DESC
LIMIT 1;



42) List how many books are issued to lifetime members.
Ans :

SELECT COUNT(*) AS Books_Issued_To_Lifetime_Members
FROM Issue I
JOIN Member M
ON I.Member_Id = M.Member_Id
WHERE M.Member_Type = 'Lifetime';


43) List all member types and how many members are there in each
type.

Ans :

SELECT Member_Type,
       COUNT(*) AS No_Of_Members
FROM Member
GROUP BY Member_Type;

44) List first 5 members who had joined library.

Ans :

SELECT *
FROM Member
ORDER BY Acc_Open_Date ASC
LIMIT 5;


45) List the members with their member type, who have issued books

during the period 1st December to 31st December.

Ans :

SELECT DISTINCT M.Member_Id,
       M.Member_Name,
       M.Member_Type
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
WHERE MONTH(I.Issue_Date) = 12;


46) List all the members who have not returned books yet.

Ans :

SELECT DISTINCT M.*
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
WHERE I.Return_Date IS NULL;


47) List all the members who joined library on the same date Garima

joined.

Ans :

SELECT *
FROM Member
WHERE Acc_Open_Date =
(
    SELECT Acc_Open_Date
    FROM Member
    WHERE Member_Name = 'Garima'
);


48) List all the members who has issued books from author “Loni” in

the month of December

Ans :

SELECT DISTINCT M.*
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
JOIN Book B
ON I.Book_No = B.Book_No
WHERE B.Author = 'Loni'
AND MONTH(I.Issue_Date) = 12;


49) List names of the authors whose books are least issued by

lifetime members.

Ans :

SELECT B.Author,
       COUNT(I.Book_No) AS Issue_Count
FROM Book B
JOIN Issue I
ON B.Book_No = I.Book_No
JOIN Member M
ON I.Member_Id = M.Member_Id
WHERE M.Member_Type = 'Lifetime'
GROUP BY B.Author
ORDER BY Issue_Count ASC
LIMIT 1;



50) List the names of members who has issued the books whose cost
is more than 300 rupees and whose author is “Scott Urman”

Ans :

SELECT DISTINCT M.Member_Id,
       M.Member_Name
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
JOIN Book B
ON I.Book_No = B.Book_No
WHERE B.Price > 300
AND B.Author = 'Scott Urman';


51) List all lifetime members who joined library during 1st January
2006 to 31st December 2006 but issued only one book.

Ans :

SELECT M.Member_Id,
       M.Member_Name
FROM Member M
JOIN Issue I
ON M.Member_Id = I.Member_Id
WHERE M.Member_Type = 'Lifetime'
AND M.Acc_Open_Date BETWEEN '2006-01-01' AND '2006-12-31'
GROUP BY M.Member_Id,
         M.Member_Name
HAVING COUNT(I.Book_No) = 1;



52) Modify the Penalty_Amount for Garima Sen to Rs 100.

Ans :

UPDATE Member
SET Penalty_Amount = 100
WHERE Member_Name = 'Garima Sen';










