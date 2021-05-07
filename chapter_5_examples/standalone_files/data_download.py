# A basic example of downloading data from the web with Python,
# using the requests library
#
# The source data we are downloading will come from the following URLs:
# http://feeds.bbci.co.uk/news/science_and_environment/rss.xml
# https://gbfs.citibikenyc.com/gbfs/en/station_status.json


# import the requests library, which let's us write Python that acts like
# a web browser through code
import requests

# our chosen filename for our XML file
XMLfilename = "BBC_RSS.xml"

# open a new, writable file with the filename we stored in our `XMLfilename`
# variable
xml_output_file = open(XMLfilename,"w")

# use the requests library's "get" recipe to access the contents of our
# target URL and store it in a our `xml_data` variable
xml_data = requests.get('http://feeds.bbci.co.uk/news/science_and_environment/rss.xml')

# the requests library's "get" function has put the contents of the webpage
# in a property "text", which we'll write directly to our xml_output_file
# using the built-in "write" method
xml_output_file.write(xml_data.text)

# close our xml_output_file
xml_output_file.close()

# our chosen filename for our XML file
JSONfilename = "citibikenyc_station_status.json"

# open a new, writable file with the filename we stored in our `JSONfilename`
# variable
json_output_file = open(JSONfilename,"w")

# use the requests library's "get" recipe to access the contents of our
# target URL and store it in a our `json_data` variable
json_data = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')

# the requests library's "get" function has put the contents of the webpage
# in a property "text", which we'll write directly to our json_output_file
# using the built-in "write" method
json_output_file.write(json_data.text)

# close our json_output_file
json_output_file.close()
