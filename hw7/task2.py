# The “sys.path” list is initialized from the PYTHONPATH environment variable. 
# Is it possible to change it from within Python? If so, does it affect where Python looks for module files? 
# Run some interactive tests to find it out.

# Yes, it is possible to change the directory in Python using the sys module

import sys

print("\n" + "Original sys.path:")
print(sys.path)

custom_directory = "/Users/alisiyanosenko/Python/beetroot_study/practice/modules/module.py"
sys.path.append(custom_directory)

print("\n" + "Modified sys.path:")
print(sys.path)