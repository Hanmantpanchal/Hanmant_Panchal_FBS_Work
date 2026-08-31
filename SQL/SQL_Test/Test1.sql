1. Write an SQL query to retrieve all employees' names and salaries from a table named
`Employees`, ordered by salary in descending order.

Ans:

SELECT employee_name, salary
FROM Employees
ORDER BY salary DESC;

2. Retrieve the top 5 highest-paid employees from the `Employees` table.

Ans:

SELECT *
FROM Employees
ORDER BY salary DESC
LIMIT 5;



3. Fetch employee records from the `Employees` table, skipping the first 3 records and showing
the next 5 records.

Ans:

SELECT *
FROM Employees
LIMIT 5 OFFSET 3;


4. Write a query to count the number of employees in each department from the `Employees`
table.

Ans:

SELECT department_id,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id;



5. Fetch the department-wise average salary from the `Employees` table, only for departments
where the average salary is greater than 50,000.

Ans:

SELECT department_id,
       AVG(salary) AS average_salary
FROM Employees
GROUP BY department_id
HAVING AVG(salary) > 50000;


6. Retrieve a list of products from the `Products` table where the product name contains the word
"Laptop" .

Ans:

SELECT *
FROM Products
WHERE product_name LIKE '%Laptop%';



7. Extract the first three characters from the `student_name` column in the `Students` table.

Ans:

SELECT LEFT(student_name, 3) AS first_three_characters
FROM Students;


8. Fetch only those students from the `Students` table whose names start with the letter "A".

Ans:

SELECT *
FROM Students
WHERE student_name LIKE 'A%';

9. Write an SQL query to find the total number of orders placed in each month, considering only
those months where more than 100 orders were placed.

Ans:

SELECT MONTH(order_date) AS month,
       COUNT(*) AS total_orders
FROM Orders
GROUP BY MONTH(order_date)
HAVING COUNT(*) > 100;


10. Get the total and average sales amount per category from the `Sales` table, considering only
categories with total sales greater than 1,00,000.

Ans :

SELECT category,
       SUM(sales_amount) AS total_sales,
       AVG(sales_amount) AS average_sales
FROM Sales
GROUP BY category
HAVING SUM(sales_amount) > 100000;



11. What does the following query return?
SELECT COUNT(*) FROM Employees;


a) The total number of employees

b) The sum of salaries of employees
c) The first record of the table
d) An error message



Ans :

a) The total number of employees




12. What will be the output of the following query?
SELECT LENGTH('Database');
a) 9
b) 8
c) 10
d) Error


Ans : b) 8


13. Which of the following clauses is used to filter grouped results?
a) WHERE
b) ORDER BY
c) HAVING
d) GROUP BY

Ans : c) HAVING



14. What does `LEFT JOIN` do?
a) Returns only the matching rows from both tables
b) Returns all rows from the left table and matching rows from the right table
c) Returns all rows from the right table and matching rows from the left table
d) Returns all rows from both tables

Ans :b) Returns all rows from the left table and matching rows from the right table



15. What will be the result of the following query?
SELECT UPPER('hello world');
a) hello world
b) HELLO WORLD
c) Hello World
d) Syntax error

Ans: b) HELLO WORLD



16. Question:

You have two tables:
• Orders with columns: order_id, customer_id, order_date, total_amount.
• Customers with columns: customer_id, region.
• O/P- region | total_orders
Write an SQL query to find the total order amount (total_amount) for each region. Only include
regions where the total order amount is greater than 10000


Ans :

SELECT C.region,
       SUM(O.total_amount) AS total_orders
FROM Orders O
JOIN Customers C
ON O.customer_id = C.customer_id
GROUP BY C.region
HAVING SUM(O.total_amount) > 10000;



17. Question:
You have two tables:
• Books with columns: book_id, author_id, title, price.
• Sales with columns: sale_id, book_id, sale_date, quantity.
• O/P- author_id | total_books_sold

Write an SQL query to find the total number of books sold by each author. Only include authors
who have sold more than 100 books.

Ans :

SELECT B.author_id,
       SUM(S.quantity) AS total_books_sold
FROM Books B
JOIN Sales S
ON B.book_id = S.book_id
GROUP BY B.author_id
HAVING SUM(S.quantity) > 100;












