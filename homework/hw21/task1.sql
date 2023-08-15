/* write a query in SQL to display the first name, last name, department number, and department name for each employee*/

SELECT employees.first_name, employees.last_name,  employees.department_id, departments.depart_name
FROM employees
LEFT JOIN departments ON departments.department_id = employees.department_id;

/* write a query in SQL to display the first and last name, department, city, and state province for each employee*/

SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id
LEFT JOIN locations l ON d.location_id = l.location_id;

/* write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40*/

SELECT e.first_name, e.last_name,  e.department_id, d.depart_name
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id
WHERE e.department_id IN(40, 80);

/* write a query in SQL to display all departments including those where does not have any employee*/

SELECT department_id, depart_name 
FROM departments;

/* write a query in SQL to display the first name of all employees including the first name of their manager*/

SELECT e.first_name AS "Employee name", e2.first_name AS "Manager's name"
FROM employees e
LEFT JOIN employees e2 ON e2.employee_id  = e.manager_id;

/* write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee*/

SELECT 
	e.first_name || " " || e.last_name AS "Full Name", 
	j.job_title AS "Job Title",
	j.max_salary - e.salary AS "Salary Diff"
FROM employees e
LEFT JOIN jobs j ON j.job_id = e.job_id ;

/* write a query in SQL to display the job title and the average salary of employees*/

SELECT j.job_title, AVG(e.salary)
FROM jobs j 
LEFT JOIN employees e ON e.job_id = j.job_id 
GROUP BY j.job_id;

/* write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London*/

SELECT 
	e.first_name || " " || e.last_name AS "Full Name", 
	e.salary 
FROM employees e 
LEFT JOIN departments d ON d.department_id = e.department_id 
LEFT JOIN locations l ON l.location_id = d.location_id 
WHERE l.city = "London";

/* write a query in SQL to display the department name and the number of employees in each department */

SELECT 
	d.depart_name, 
	COUNT(e.employee_id)
FROM departments d
LEFT JOIN employees e  ON e.department_id = d.department_id 
GROUP BY d.department_id;
