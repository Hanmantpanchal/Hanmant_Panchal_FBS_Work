Assignment 4

Q1) Write an SQL query to display employee first_name and last_name with suitable column
aliases.

SELECT first_name AS "First Name",
       last_name AS "Last Name"
FROM employees;


Q2) Write an SQL query to display all different department IDs available in the EMPLOYEES
table.

Ans :

SELECT DISTINCT department_id
FROM employees;



Q3) Display all employee details sorted by first_name in descending order

Ans :

SELECT *
FROM employees
ORDER BY first_name DESC;



Q4) Write an SQL query to display first_name, last_name, salary, and PF for all employees.
(PF is calculated as 15% of salary.)

Ans:

SELECT first_name,
       last_name,
       salary,
       salary * 0.15 AS PF
FROM employees;

Q5) Write an SQL query to display employee_id, employee names, and salary sorted in
increasing order of salary.

Ans :

SELECT employee_id,
       CONCAT(first_name, ' ', last_name) AS employee_name,
       salary
FROM employees
ORDER BY salary ASC;


Q6) Write an SQL query to display the total salary payable to all employees.

Ans:

SELECT SUM(salary) AS total_salary
FROM employees;


Q7) Write an SQL query to display the highest salary and the lowest salary from the
EMPLOYEES table.

Ans :

SELECT MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM employees;

Q8) Write an SQL query to display the average salary and the total number of employees.

Ans :

SELECT AVG(salary) AS average_salary,
       COUNT(*) AS total_employees
FROM employees;

Q9) Write an SQL query to display the total number of employees working in the company.

Ans :

SELECT COUNT(*) AS total_employees
FROM employees;

Q10) Write an SQL query to display the number of different job roles available in the
EMPLOYEES table.

Ans :

SELECT COUNT(DISTINCT job_id) AS different_job_roles
FROM employees;


Q11) Write an SQL query to display the first 10 employee records from the EMPLOYEES table.

Ans :

SELECT *
FROM employees
LIMIT 10;


Q12) Write an SQL query to display employee names and salary for employees whose salary is
less than 10000 or greater than 15000.

Ans :

SELECT CONCAT(first_name, ' ', last_name) AS employee_name,
       salary
FROM employees
WHERE salary < 10000
   OR salary > 15000;


Q13) Write an SQL query to display employee names and department_id for employees working
in department 30 and department 100.
Sort the result by department_id.

Ans :

SELECT CONCAT(first_name, ' ', last_name) AS employee_name,
       department_id
FROM employees
WHERE department_id IN (30, 100)
ORDER BY department_id ASC;


Q14) Write an SQL query to display employee names and salary for employees working in
department 30 or 100,
whose salary is outside the range 10000 to 15000.

Ans :

SELECT CONCAT(first_name, ' ', last_name) AS employee_name,
       salary
FROM employees
WHERE department_id IN (30, 100)
  AND salary NOT BETWEEN 10000 AND 15000;

Q15) Write an SQL query to display employee names and hire_date for employees who were
hired in the year 1987.

Ans :

SELECT CONCAT(first_name, ' ', last_name) AS employee_name,
       hire_date
FROM employees
WHERE YEAR(hire_date) = 1987;


Q16) Write an SQL query to display first_name of employees whose first_name contains both
letters 'b' and 'c'.

Ans :

SELECT first_name
FROM employees
WHERE LOWER(first_name) LIKE '%b%'
  AND LOWER(first_name) LIKE '%c%';


Q17) Write an SQL query to display last_name, job role, and salary for employees who work as
Programmer or Shipping Clerk,
and whose salary is not equal to 4500, 10000, or 15000.

Ans :

SELECT last_name,
       job_role,
       salary
FROM employees
WHERE job_role IN ('Programmer', 'Shipping Clerk')
  AND salary NOT IN (4500, 10000, 15000);


Q18) Write an SQL query to display last_name of employees who’s last_name contains exactly 6
characters.

Ans :

SELECT last_name
FROM employees
WHERE LENGTH(last_name) = 6;

Q19) Write an SQL query to display last_name of employees having 'e' as the third character in
their last_name.

Ans :

SELECT last_name
FROM employees
WHERE LOWER(last_name) LIKE '__e%';


Q20) Write an SQL query to display all different job roles/designations available in the
EMPLOYEES table.

Ans :

SELECT DISTINCT job_role
FROM employees;


Q21) Write an SQL query to display employee details for employees who’s last_name is
BLAKE, SCOTT, KING, or FORD.

Ans :

SELECT *
FROM employees
WHERE last_name IN ('BLAKE', 'SCOTT', 'KING', 'FORD');







