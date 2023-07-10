# Write a Python program to access a function inside a function 
# (Tips: use function, which returns another function)

# My inner function counts chars in a word.
def chars_in_word(word):
    chars = len(word)
    return chars

# Main function uses the inner function to count chars in all the words from the list and then prints the result.
def chars_in_list(list):
    sum_chars = 0
    for word in list:
        chars = chars_in_word(word)
        sum_chars = sum_chars + chars
    print(sum_chars)

berries = ["elderberry", "muckleberry", "blueberry", "raspbery", "strawberry"]
chars_in_list(berries)