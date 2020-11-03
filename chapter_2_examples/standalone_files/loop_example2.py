# create a list that contains the number of pages in each chapter
# of the print version of this book

page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# create a variable to keep track of the total number of pages,
# starting its value at 0
total_pages = 0

# for every item in the list, perform some action - in this case,
# add the number to our "total_pages" variable
for a_number in page_counts:
    print("Top of loop!")
    print("The current item is:")
    print(a_number)
    total_pages = total_pages + a_number
    print("The running total is:")
    print(total_pages)
    print("Bottom of loop!")

print(total_pages)
