# 2. Напишіть програму для керування списком завдань. Кожне завдання може 
# мати назву, опис, пріоритет та статус (наприклад, "виконується", "в очікуванні", "завершено"). 
# Реалізуйте можливість додавання нових завдань, оновлення статусу завдань та виведення списку завдань за пріоритетом.

tasks = {"to have lunch": {"description": "just eat", "status": "not started", "priority": "high"}, 
          "to walk a dog": {"description": "take a dog for a walk", "status": "in progress", "priority": "critical"}}

# Tasks addition:

task_name = input("Enter your task name: ")
task_desc = input("Enter your task description: ")
task_status = input("Enter your task status: ")
task_prio = input("Enter your task priority: ")

print("\n\n")

if task_name in tasks.keys():
    # tasks.update({task_name:{"description": task_desc, "status": task_status, "priority": task_prio}})
    tasks[task_name]["status"] = task_status
    print(tasks)
else:
    tasks.update({task_name:{"description": task_desc, "status": task_status, "priority": task_prio}})
    print(tasks)

# 6. Напишіть програму для керування студентськими оцінками. Реалізуйте можливість 
# додавання оцінок, видалення оцінок, обчислення середнього балу студента та виведення списку студентів з їх оцінками.

grades = {"student1": {"maths": 5, "biology": 3, "literature": 4},
          "student2": {"maths": 2, "biology": 2, "literature": 3},
          "student3": {"maths": 4, "biology": 4, "literature": 5}}

st_name = input("Enter the name of the student: ")
disc_name = input("Enter the name of the discipline: ")
st_grade = input("Enter the grade: ")

if st_name in grades.keys():
    grades[st_name][disc_name] = st_grade
    print(grades)
else:
    grades.update({st_name: {disc_name: st_grade}})
    print(grades)

