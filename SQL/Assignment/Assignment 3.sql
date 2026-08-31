Assignment 3 :

Q1) Write an SQL query to insert the above employee records into the EMPLOYEES table.

Ans :

INSERT INTO EMPLOYEES
    (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID)
VALUES
    (100, 'Steven',    'King',      1, 24000.00, 200, 10),
    (101, 'Neena',    'Kochhar',   2, 17000.00, 200, 10),
    (102, 'Lex',      'De Haan',   2, 17000.00, 200, 10),
    (103, 'Alexander','Hunold',    3,  9000.00, 103, 60),
    (104, 'Bruce',    'Ernst',     3,  6000.00, 103, 60),
    (105, 'David',    'Austin',    3,  4800.00, 103, 60),
    (106, 'Valli',    'Pataballa', 3,  4800.00, 103, 60),
    (107, 'Diana',    'Lorentz',   3,  4200.00, 114, 30),
    (108, 'Nancy',    'Greenberg', 4, 12000.00, 145, 80),
    (109, 'Daniel',   'Faviet',    4,  9000.00, 145, 80);


Q2) Write a single SQL INSERT statement to insert at least 3 department records into the
DEPARTMENTS table.

Ans :
INSERT INTO DEPARTMENTS
    (DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID, LOCATION_ID)
VALUES
    (10, 'Administration', 200, 1700),
    (20, 'Marketing',      201, 1800),
    (30, 'Purchasing',     114, 1700);


Q3) Write an SQL query to insert one new job record into the JOBS table ensuring duplicate
JOB_ID is not allowed.

Ans :

INSERT INTO JOBS
    (JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY)
VALUES
    (5, 'Data Analyst', 5000, 15000);


Q4) Write an SQL query to increment the salary of each employee by 10%.

Ans :

UPDATE EMPLOYEES
SET SALARY = SALARY * 1.10;


Q5) Write an SQL query to set EMAIL = 'not available' for employees whose department_id is
80 and commission_pct is less than 0.20.


Ans :

UPDATE EMPLOYEES
SET EMAIL = 'not available'
WHERE DEPARTMENT_ID IN (60, 80)
  AND COMMISSION_PCT < 0.20;



Q6) Write an SQL query to set EMAIL = 'not available' for employees who belong to the
'Purchasing' department.

Ans :

UPDATE EMPLOYEES
SET EMAIL = 'not available'
WHERE DEPARTMENT_ID = (
    SELECT DEPARTMENT_ID
    FROM DEPARTMENTS
    WHERE DEPARTMENT_NAME = 'Purchasing'
);

Q7) Write an SQL query to update EMAIL = 'not available' and COMMISSION_PCT = 0.10 for
all employees.

Ans :

UPDATE EMPLOYEES
SET EMAIL = 'not available',
    COMMISSION_PCT = 0.10;

Q8) Write an SQL query to increase salary by 2000 for employees working in department_id =
60.


Ans :
UPDATE EMPLOYEES
SET SALARY = SALARY + 2000
WHERE DEPARTMENT_ID = 60;


Q9) Write an SQL query to delete employees whose salary is less than 5000.

Ans :

DELETE FROM EMPLOYEES
WHERE SALARY < 5000;


Q10) Write an SQL query to insert one new employee record with your own suitable details (use
a new employee_id).

Ans :

INSERT INTO EMPLOYEES
    (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID)
VALUES
    (110, 'John', 'Smith', 3, 7000.00, 103, 60);


Q11) Write an SQL query to change manager_id to 300 for all employees in department_id = 80.

Ans :

UPDATE EMPLOYEES
SET MANAGER_ID = 300
WHERE DEPARTMENT_ID = 80;


Q12) Write an SQL query to delete the department record where department_id = 20 and observe
the error if employees exist in that department.

Ans :

DELETE FROM DEPARTMENTS
WHERE DEPARTMENT_ID = 20;




