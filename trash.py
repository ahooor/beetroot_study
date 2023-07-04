# n = 5
# while n > 0:
#     n -= 1
#     if (n % 2) == 0:
#         continue
# print(n)

# import random
# x = random.randint(1, 0)
# print(x)

employers = [["Petro", "Petrov", "@oracle.com"], ["Vasyl", "Tsik", "@oracle.com"], ["Fedir", "Mainov", "@oracle.com"], 
             ["Gregor", "Clegane", "@oracle.com"], ["Harry", "Potter", "@oracle.com"]]

def generate_email_variants(employers_list):
    email_variants = []
    for employer in employers_list:
        first_name = employer[0].lower()
        last_name = employer[1].lower()
        domain = employer[2]
        
        # Generate three email variants
        email1 = first_name + "." + last_name + domain
        email2 = first_name[0] + "." + last_name + domain
        email3 = first_name + "." + last_name[0] + domain
        
        email_variants.append([email1, email2, email3])
    
    return email_variants

email_variants = generate_email_variants(employers)

# Print the generated email variants
for i, employer in enumerate(employers):
    print(f"Employer {i+1}: {employer[0]} {employer[1]}")
    print("Email Variants:")
    for j, variant in enumerate(email_variants[i]):
        print(f"Variant {j+1}: {variant}")
    print()