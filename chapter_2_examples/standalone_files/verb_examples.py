# create a variable named author, and set its contents to "Susan E. McGregor"
# using the assignment operator, '='
author = "Susan E. McGregor"

# confirm that the computer "remembers" what's in the `author` variable
# by using the built-in 'print' function
print(author)

# create another variable named editor
editor  = "Jeff Bleiel"

# use the built-in print function to output "Hello" messages to each person
print("Hello "+author)
print("Hello "+editor)


# create a function that prints out a greeting to any name passed to the function

def greet_me(a_name):
    print("Hello "+a_name)

# use my custom function, greet_me to output "Hello" messages to each person
greet_me(author)
greet_me(editor)
