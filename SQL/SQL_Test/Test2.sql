Set B
1. Retrieve the names of all customers from the `Customers` table, sorted in alphabetical order.

Ans :
SELECT customer_name
FROM Customers
ORDER BY customer_name ASC;


2. Fetch the top 10 most expensive products from the `Products` table.

Ans :

SELECT *
FROM Products
ORDER BY price DESC
LIMIT 10;


3. Write a query to get the second-highest salary from the `Employees` table.

Ans:

SELECT MAX(salary) AS second_highest_salary
FROM Employees
WHERE salary < (
    SELECT MAX(salary)
    FROM Employees
);



4. Get the total count of customers from each city in the `Customers` table.

Ans :

SELECT city,
       COUNT(*) AS customer_count
FROM Customers
GROUP BY city;


5. Retrieve department-wise total salary from the `Employees` table but only include
departments where the total salary is greater than 2,00,000.

Ans:

SELECT department_id,
       SUM(salary) AS total_salary
FROM Employees
GROUP BY department_id
HAVING SUM(salary) > 200000;


6. Extract only the last four characters of the `phone_number` column and first three characters
from `customerName` columns from the `Customers` table.

Ans :

SELECT RIGHT(phone_number, 4) AS last_four_digits,
       LEFT(customerName, 3) AS first_three_characters
FROM Customers;


7. Write a query to retrieve products where the `product_name` contains "Pro".

Ans:

SELECT *
FROM Products
WHERE product_name LIKE '%Pro%';


8. Fetch the total number of students per course from the `Students` table, only for courses that
have at least 30 students enrolled.

Ans :

SELECT course,
       COUNT(*) AS total_students
FROM Students
GROUP BY course
HAVING COUNT(*) >= 30;


9. Write an SQL query to find the number of orders placed in each month of the year.

Ans :

SELECT MONTH(order_date) AS month,
       COUNT(*) AS total_orders
FROM Orders
GROUP BY MONTH(order_date)
ORDER BY month;


10. Get the highest and lowest salary per department from the `Employees` table.

Ans :

SELECT department_id,
       MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM Employees
GROUP BY department_id;


11. What does the following query return?
SELECT SUBSTRING('Database', 1, 4);
a) Data
b) tabase
c) DataB
d) Error

Ans : a) Data


12. Which clause is used to sort the results in descending order?
a) ORDER BY DESC
b) ORDER BY ASC
c) SORT BY DESC
d) GROUP BY DESC

Ans :

a) ORDER BY DESC


13. What is the default sorting order of `ORDER BY` if no direction (ASC/DESC) is specified?
a) ASC
b) DESC
c) No specific order
d) Error

Ans :a) ASC


14. What will be the output of the following query?
SELECT ROUND(15.678, 2);
a) 15.67
b) 15.68
c) 15.7
d) 16

Ans :

b) 15.68


15. Which SQL function is used to count the number of rows in a table?
a) TOTAL()
b) COUNT()
c) SUM()
d) NUMBER()

Ans :

b) COUNT()


16. Question:
You have two tables:
• Orders with columns: order_id, customer_id, order_date, total_amount.
• Customers with columns: customer_id, customer_name.
• O/P- customer_id, customer_name, avg_order_value
Write an SQL query to find the average order value (total_amount) for each customer. Only
include customers who have made more than 2 orders.

Ans :

SELECT C.customer_id,
       C.customer_name,
       AVG(O.total_amount) AS avg_order_value
FROM Customers C
JOIN Orders O
ON C.customer_id = O.customer_id
GROUP BY C.customer_id,
         C.customer_name
HAVING COUNT(O.order_id) > 2;



17. Question:
You have two tables:
• Products with columns: product_id, product_name.
• Sales with columns: sale_id, product_id, sale_date, amount.
• O/P- product_id | product_name | sales_count
Write an SQL query to find the number of sales made for each product. Only include products
with more than 50 sales.

Ans :

SELECT P.product_id,
       P.product_name,
       COUNT(S.sale_id) AS sales_count
FROM Products P
JOIN Sales S
ON P.product_id = S.product_id
GROUP BY P.product_id,
         P.product_name
HAVING COUNT(S.sale_id) > 50;


