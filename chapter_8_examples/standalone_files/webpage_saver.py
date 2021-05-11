""" Webpage Saver!

Downloads the contents of a webpage and it locally

Usage
-----
python webpage_saver.py target_url filename


Parameters
----------
target_url : str
    The full URL of the webpage to be downloaded
filename : str
    The desired filename of the local copy

Requirements
------------
* argparse module
* requests module


"""
# include the requests library in order to get data from the web
import requests

# include argparse library to pull arguments from the command line
import argparse

parser = argparse.ArgumentParser()
# arguments will be assigned based on the order in which they were provided
parser.add_argument("target_url", help="The full URL of the webpage to be downloaded")
parser.add_argument("filename", help="The desired filename of the local copy")
args = parser.parse_args()

# pull the url of the webpage we're downloading from the provided arguments
target_url = args.target_url

# pull the intended output filename from the provided arguments
output_filename = args.filename

# since we're *not* using an API, the website owner will have no way to identify
# us unless we provide some additional information. In this case, we're
# describing the browser it should treat our traffic as being from. We're also
# providing our name and contact information. This is data that the website
# owner will be able to see in their server logs.
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36',
    'From': 'YOUR NAME HERE - youremailaddress@emailprovider.com'
}

# because we're just loading a regular webpage, we send a `get` request to the
# URL, along with our informational headers
webpage = requests.get(target_url, headers=headers)

# opening up a local file to save the contents of the webpage to
output_file = open(output_filename,"w")

# the webpage's code is in the `text` property of the website's response
# so write that to our file
output_file.write(webpage.text)

# close our output file!
output_file.close()
