# Create a simple function called favorite_movie, which takes a string containing 
# the name of your favorite movie. The function should then print “My favorite movie is named {name}”.

movie = input("Enter your favorite movie name: ")

def favorite_movie(name):
    print(f"My favorite movie is named {name}")

favorite_movie(movie)