# SQL - Assignment 1

/* =========================================================
Q1) Display Databases

Login to MySQL and write a query to display all
databases already present in the system.
========================================================= */

SHOW DATABASES;

/* =========================================================
Q2) Create countries Table

Create a table named countries including columns:
country_id, country_name and region_id.

After this display the structure of table.
========================================================= */

-- 1) Create countries Table

CREATE TABLE countries (
country_id INT,
country_name VARCHAR(50),
region_id INT
);

-- 2) Display the structure of table

DESC countries;

/* =========================================================
Q3) Create jobs Table with Constraints

Constraints:

* job_id must be Primary Key
* job_title cannot be NULL
* max_salary must not exceed 25000
  ========================================================= */

CREATE TABLE jobs (
job_id INT PRIMARY KEY,
job_title VARCHAR(100) NOT NULL,
min_salary DECIMAL(10,2),
max_salary DECIMAL(10,2),
CHECK (max_salary <= 25000)
);

DESC jobs;

/* =========================================================
Q4) Create job_history Table

Columns:
employee_id, start_date, end_date, job_id,
department_id
========================================================= */

CREATE TABLE job_history (
employee_id INT,
start_date DATE,
end_date DATE,
job_id INT,
department_id INT
);

DESC job_history;

/* =========================================================
Q5) Add UNIQUE Constraint

Duplicate values in country_id should not be allowed.
========================================================= */

ALTER TABLE countries
ADD CONSTRAINT unique_country_id UNIQUE (country_id);

DESC countries;

/* =========================================================
Q6) Create jobs_default Table with DEFAULT Values

Default values:

* job_title = blank
* min_salary = 8000
* max_salary = NULL
  ========================================================= */

CREATE TABLE jobs_default (
job_id INT,
job_title VARCHAR(100) DEFAULT '',
min_salary DECIMAL(10,2) DEFAULT 8000,
max_salary DECIMAL(10,2) DEFAULT NULL
);

DESC jobs_default;

/* =========================================================
Q7) Create departments Table

Composite Primary Key:
(department_id, manager_id)
========================================================= */

CREATE TABLE departments (
department_id DECIMAL(4,0) NOT NULL,
department_name VARCHAR(30) NOT NULL,
manager_id DECIMAL(6,0) NOT NULL,
location_id DECIMAL(4,0),
PRIMARY KEY (department_id, manager_id)
);

DESC departments;

/* =========================================================
Q8) Create employees Table with Normal Foreign Key

Constraints:

* employee_id must be Primary Key
* department_id must be Foreign Key
  referencing departments(department_id)

Since departments has a composite primary key,
department_id is made UNIQUE so that it can be
referenced individually.
========================================================= */

ALTER TABLE departments
ADD CONSTRAINT unique_department_id UNIQUE (department_id);

CREATE TABLE employees (
employee_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
phone_number VARCHAR(20),
hire_date DATE,
job_id INT,
salary DECIMAL(10,2),
commission DECIMAL(10,2),
manager_id INT,
department_id INT,

```
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
```

);

DESC employees;

/* =========================================================
Q9) Composite Foreign Key Implementation

Step 1:
Create department_managers table.

Composite Primary Key:
(department_id, manager_id)
========================================================= */

CREATE TABLE department_managers (
department_id DECIMAL(4,0) NOT NULL,
manager_id DECIMAL(6,0) NOT NULL,
manager_name VARCHAR(50) NOT NULL,
PRIMARY KEY (department_id, manager_id)
);

DESC department_managers;

/* =========================================================
Step 2:
Apply Composite Foreign Key in employees table.

The combination:
(department_id, manager_id)

must exist in:
department_managers(department_id, manager_id)
========================================================= */

ALTER TABLE employees
ADD CONSTRAINT fk_employee_department_manager
FOREIGN KEY (department_id, manager_id)
REFERENCES department_managers(department_id, manager_id);
