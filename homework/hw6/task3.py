# Use a list comprehension to make a list containing tuples (i, j) where `i` 
# goes from 1 to 10 and `j` is corresponding to `i` squared.

mylist = []

for x in range(1, 11):
    i = x
    j = x ** 2
    mylist.append((i, j))

print(mylist)