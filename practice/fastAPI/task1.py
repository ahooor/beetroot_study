from sqlalchemy import create_engine, text
from sqlalchemy.dialects.mysql import pymysql

# TASK 1

engine = create_engine(
    'mysql+pymysql://root:rootroot@localhost:3306/newschema'
)

# with engine.connect() as con:
#     query = 'SELECT first_name, last_name FROM employees;'
#     res = con.execute(text(query))
#     for row in res:
#         print(row)

# TASK 2

# with engine.connect() as con:

#     statement_new = text("INSERT INTO employees(first_name, last_name, job_id, salary) VALUES('Maxim', 'Kostenko', 'ST_MAN', '8000')")

#     con.execute(statement_new)
#     con.commit()

# with engine.connect() as con:
#     query = 'SELECT first_name, last_name FROM employees;'
#     res = con.execute(text(query))
#     for row in res:
#         print(row)

# TASK 3

# def search_by_id(id_emp):
#     with engine.connect() as con:
#         res = con.execute(text(f'SELECT first_name, last_name FROM employees WHERE employee_id = {id_emp};'))
#     for row in res:
#         print(row)

# employee_info = search_by_id(121)
# print(employee_info)

# TASK 4
# Оновлення інформації про співробітника (посада, зарплатня) за його ідентифікатором.

# def update_by_id(id_emp, new_job, new_salary):
#     with engine.connect() as con:
#         transaction = con.begin()
#         res = con.execute(text(f'UPDATE employees SET job_id = "{new_job}", salary = {new_salary} WHERE employee_id = {id_emp};'))
#         transaction.commit()
#     return res

# update_by_id(121, "ST_MAN", 8600)

# TASK 5
# Видалення співробітника за його ідентифікатором.

def delete_by_id(emp_id):
    with engine.connect() as con:
        transaction = con.begin()
        res = con.execute(text(f'DELETE FROM employees WHERE employee_id = {emp_id};'))
        transaction.commit()
    return res

delete_by_id(199)
