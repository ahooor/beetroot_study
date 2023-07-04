# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers

import random

list1 = []
i = 0
while i < 10:
    list1.append(random.randint(1, 10))
    i += 1

list2 = []
i = 0
while i < 10:
    list2.append(random.randint(1, 10))
    i += 1

common_list = []
i = 0
while i < len(list1):
    j = 0
    while j < len(list2):
        if list1[i] == list2[j] and list1[i] not in common_list:
            common_list.append(list1[i])
        j += 1
    i += 1

print("List 1:", list1)
print("List 2:", list2)
print("Common List:", common_list)
