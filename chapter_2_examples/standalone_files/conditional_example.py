# create a list that contains the number of pages in each chapter
# of the print version of this book

page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# create variables to keep track of the total pages,
# the number of chapters with more than 30 pages,
# and the number of chapters with fewer than 30 pages
total_pages = 0
under_30 = 0
over_30 = 0


# for every item in the page_counts list:
for a_number in page_counts:
    # add the current number of pages to our total_pages count
    total_pages = total_pages + a_number
    # check if the current number of pages is more than 30
    if a_number > 30:
        # if the current number of pages *is* more than 30,
        # add 1 to our over_30 counter
        over_30 = over_30 + 1
    # otherwise...
    else:
        # add 1 to our under_30 counter
        under_30 = under_30 + 1


print(total_pages)
print("Number of chapters over 30 pages:")
print(over_30)
print("Number of chapters under 30 pages:")
print(under_30)
