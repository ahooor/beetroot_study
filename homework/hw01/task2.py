# Create a python program named "task2", and use the built-in function 'print' in it several times. 
# Try to pass "sep", "end" params and pass several parameters separated by commas. 
# Also, provide a comment text above each print statement, mentioned above, 
# with the expected output after execution of the particular print statement.

#Ex. 1: simple print
print("\nHi! Just testing\n")

#Ex. 2: print with multiple arguments
print("That", "is", "not", "an", "easy", "way", "to", "write\n")

#Ex. 3: print with custom separator
print("Apples", "Bananas", "Kiwi", "Oranges", "Beer\n", sep="\n")

#Ex. 4: print with custom ending
print("Wow, you've made it", end="!\n\n")

#Ex. 5: print with custom sep and end
print("Wow, you've made it", "Congrats", sep="!\n", end="!\n\n")

#Ex. 6: print with variables, custom sep and end
name = "Alice"
event = "wedding"
print(f"Congrats on your recent {event}, {name}", end="!\n")
