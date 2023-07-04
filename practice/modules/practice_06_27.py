from module import update_dict, calculate, generate_email, upd_grades, add_order, delete_order, checkout

update_dict(name = "Eggs", price = "18$", amount = "2000")

print("\n")

calculate(first_number = "23", second_number = "24", operation = "+")

print("\n")

empl = [["Petro", "Petrov", "@oracle.com"], ["Vasyl", "Tsik", "@oracle.com"], ["Fedir", "Mainov", "@oracle.com"], 
             ["Gregor", "Clegane", "@oracle.com"], ["Harry", "Potter", "@oracle.com"]]
generate_email(employees = empl)

print("\n")

upd_grades(st_name = "student4", disc_name = "maths", st_grade = "5")

print("\n")

orders = [("Caesar", 30), ("Ceviche", 26), ("Minestrone", 24)]

total_price = checkout(orders)
print("Total price:", total_price)

add_order(dish = "Cheese plate", price = 12)
delete_order(dish = "Caesar", price = 30)


