# create a function that **returns** a greeting to any name passed in
def make_greeting(a_name):
    return("Hello "+a_name)

# create a variable named author
author = "Susan E. McGregor"

# create another variable named editor
editor  = "Jeff Bleiel"

# use my custom function, greet_me to create "Hello" messages to each person
author_greeting = make_greeting(author)
editor_greeting = make_greeting(editor)

# print the gretting messages that were returned by each function call
print(author_greeting)
print(editor_greeting)
