# import the BeautifulSoup recipe from the bs4 library
# this will let us zero in on parts of our webpage based on their class name
# and/or tag type
from bs4 import BeautifulSoup

# open the saved copy of our MTA turnstiles webpage, original here:
# http://web.mta.info/developers/turnstile.html
mta_webpage = open("MTA_turnstiles_index.html", "r")

# if we click one of the data links on the live copy of the webpage, we
# see that the first part of the URL is "http://web.mta.info/developers/"
# each link only contains "data/nyct/turnstile/turnstile_YYMMDD.txt",
# so we'll need to combine those links with this base URL for them to work later
base_url = "http://web.mta.info/developers/"

# the BeautifulSoup recipe takes the contents of our webpage and another
# "ingredient", which tells it what kind of code it is working with. In this
# case, it's HTML
soup = BeautifulSoup(mta_webpage, "html.parser")

# using the "find" recipe, we can pass a tag type and class name as
# "ingredients" to zero in on the content we want. Thanks to our work with the
# inspection tools, we can go straight to a `div` with the class `span-84 last`
# note that because the word "class" has a special meaning in Python, the
# ingredient name adds an underscore to the end: `class_`
data_files_section = soup.find("div", class_="span-84 last")

# within that div, we can now just look for all the "anchor" tags
all_data_links = data_files_section.find_all("a")

# need to open a file to write our extracted links to
mta_data_list = open("MTA_data_index.csv","w")

# the "find_all()" recipe returns a list of everything it matches, so we
# use a for...in loop to go through all the links
for a_link in all_data_links:

    # creat a variable that combines our base URL with the contents of the
    # "href" property of each link (which is where the link information lives)
    complete_link = base_url+a_link["href"]

    # write this completed link to our output file, manually adding a
    # newline `\n` character to the end, so each link will be on its own row
    mta_data_list.write(complete_link+"\n")


# once we've written all the links to our file, close it!
mta_data_list.close()
