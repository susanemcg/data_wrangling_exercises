# include the requests library in order to get data from the web
import requests

# the built-in `operating system` or `os` Python library will let us create
# a new folder in which to store our downloaded data files
import os

# the built-in `time` Python library will let us `pause` our script for 2
# seconds between data requests, so that we don't overload the MTA server with
# too many requests in too short a time period
import time

# open the file where we stored our list of links
mta_data_links = open("MTA_data_index.csv","r")

# create a folder name so that we can keep the data organized
folder_name = "turnstile_data"

# since we're *not* using an API, the website owner will have no way to identify
# us unless we provide some additional information.
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36',
    'From': 'YOUR NAME HERE - youremailaddress@emailprovider.som'
}


# the built-in `readlines()` function reads one line of data from our file
# at a time, and makes them into a list
mta_links_list = mta_data_links.readlines()

# as we did when working with PDFs, we want to confirm that no folder with
# our chosen name exists before creating it; otherwise we'll get an error
if os.path.isdir(folder_name) == False:
    # create a new folder with that name
    target_folder = os.mkdir(folder_name)

# we only need four files, so we should only download that many
for i in range(0,4):
    # we use the built-in `strip()` recipe to remove the newline `\n` character
    # at the end of each row
    data_url = (mta_links_list[i]).strip()

    # we split the url on slashes, and take the item from the resulting list
    # which is the `.txt` filename. This is the filename we'll use to save
    # our local copy of the data
    data_filename = data_url.split("/")[-1]

    # make our request for the data
    turnstile_data_file = requests.get(data_url, headers=headers)

    # open a new, writable file inside our target folder, using the appropriate
    # filename
    local_data_file = open(os.path.join(folder_name,data_filename), "w")

    # save the contents of the downloaded file to that new file
    local_data_file.write(turnstile_data_file.text)

    # close the local file
    local_data_file.close()

    # "sleep" for two seconds before moving on to the next item in the loop
    time.sleep(2)
