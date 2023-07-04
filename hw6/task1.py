# Make a program that has some sentence (a string) on input and returns a dict 
# containing all unique words as keys and the number of occurrences as values. 

text = input("Enter your text: ")
words = text.split()

unique_values = {}

for word in words:
    if word in unique_values:
        unique_values[word] += 1
    else:
        unique_values[word] = 1

print(unique_values)