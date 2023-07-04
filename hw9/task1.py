# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 

# What happens if you change oops to raise KeyError instead of IndexError? 
# handle_oops functions will not work anymore as it doesn't handle KeyErrors

def oops():
    raise IndexError("Oops! An IndexError occurred.")

def handle_oops():
    try:
        oops()
    except IndexError as e:
        print("Caught an IndexError exception:")
        print(e)

# oops()
# handle_oops()

def oops():
    raise KeyError("Oops! A KeyError occurred.")

oops()
handle_oops()