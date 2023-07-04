# task 1

name = "Ivan"
surname = "Petrenko"
email = "@kobzar.com"

print("\n\n\n")

print(f"{name.lower()}"[0:1], f"{surname.lower()}", f"{email}", sep = "")

print(f"{name}.{surname}{email}".lower())

print(f"{name[0:1]}.{surname}{email}".lower())

# task 2

# 1 option

print("\n\n\n")

age = 12
a = "alcohol"
b = "energetic drinks"
c = "everything else"

if age <= 14:
    print(f"{c}")
elif age <= 18:
    print(f"{b}, {c}")
else:
    print(f"{a}, {b}, {c}")

# 2 option

print("\n\n\n")

age = int(input('скільки вам років?'))

drink=input('що ви хочете придбати? - алкоголь, енергетикик, решту?')
if drink=='алкоголь':
    if age>=18:
        print('з вас 30 грн')
    else :
        print('нажаль я не можу ва продати цей продукт')
if drink=='енергетик':
    if age>=14:
        print('з вас 30 грн')
    else :
        print('нажаль я не можу ва продати цей продукт')
else:
    print('Дякую приходьте ще!')

# 3 option

print("\n\n\n")

juice = 1
energy = 2
alcohol = 3

print("Ми маємо:", f"{juice}. Сік", f"{energy}. Енергетичні напої", f"{alcohol}. Алкогольні напої")
drink = int(input("Що бажаєте? "))

if drink == alcohol:
    age = int(input("Скільки Вам років? "))
    if age < 18:
        print("Вибачте, Вам не положено")
    else: 
        print("Тримайте, будь ласка")
elif drink == energy:
    age = int(input("Скільки Вам років? "))
    if age < 14:
        print("Вибачте, Вам не положено")
    else: 
        print("Тримайте, будь ласка")
else:
    print("Тримайте, будь ласка")

# 4 option

print("\n\n\n")

juice = 1
energy = 2
alcohol = 3

print("У нас є:", f"{juice}. Сік", f"{energy}. Енергетичні напої", f"{alcohol}. Алкогольні напої", sep = "\n")
drink = int(input("Що бажаєте [1-3]: "))

if drink == alcohol or drink == energy:
    age = int(input("Скільки Вам років? "))
    if age >= 18 or (age > 14 and drink == energy):
        print("Тримайте, будь ласка")
    else:
        print("Вибачте, Вам не положено")
else:
    print("Тримайте, будь ласка")

# task 3

print("\n\n\n")

transaction_id = ";yu7i9om0iymn%"

x = transaction_id.replace(";", "")
x = x.replace("%", "")

print(f"{x}")

# 2 option

print("\n\n\n")

transaction_id = ";yu7i9om0iymn%"

x = transaction_id[1:13]

print(f"{x}")

# task 4

print("\n\n\n")

transaction_id = "%yu7i9o%m0iymn%"
x = transaction_id.replace("%", "")

print(f"{x}")
