Files : employee.txt

101,Raja,1,25000
102,Pooja,2,40000
103,Ram,2,30000
104,Roja,1,22000
105,Siva,2,50000

File: department.txt

1,HR
2,IT


HiveQL Script (hive_advanced_queries.hql):

-- Create and use database
CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

-- Create employee table
CREATE TABLE IF NOT EXISTS employee (
    id INT,
    name STRING,
    dept_id INT,
    salary INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Create department table
CREATE TABLE IF NOT EXISTS department (
    dept_id INT,
    dept_name STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Load data into tables
LOAD DATA LOCAL INPATH 'employee.txt' INTO TABLE employee;
LOAD DATA LOCAL INPATH 'department.txt' INTO TABLE department;

-- 1. JOIN: List employee names with their department names
SELECT e.name, d.dept_name
FROM employee e
JOIN department d
ON e.dept_id = d.dept_id;

-- 2. SUBQUERY: Get employees earning above average salary
SELECT * FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);

-- 3. VIEW: Create a view for IT department employees
CREATE VIEW IF NOT EXISTS it_employees AS
SELECT e.id, e.name, e.salary
FROM employee e
JOIN department d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';

-- Use the view
SELECT * FROM it_employees;

-- 4. INDEX (Optional & rarely used in Hive)
-- Create index on department name
CREATE INDEX IF NOT EXISTS dept_name_index
ON TABLE department (dept_name)
AS 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler'
WITH DEFERRED REBUILD;

-- Build the index
ALTER INDEX dept_name_index ON department REBUILD;


TO RUN SCRIPT:
hive -f hive_advanced_queries.hql