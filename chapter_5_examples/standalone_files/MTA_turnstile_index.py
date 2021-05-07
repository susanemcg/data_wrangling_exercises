# include the requests library in order to get data from the web
import requests

# specify the url of the webpage we're downloading
# this one contains a linked list of all the NYC MTA turnstile data files
# going back to 2010
mta_turnstiles_index_url = "http://web.mta.info/developers/turnstile.html"

# since we're *not* using an API, the website owner will have no way to identify
# us unless we provide some additional information. In this case, we're
# describing the browser it should treat our traffic as being from. We're also
# providing our name and contact information. This is data that the website
# owner will be able to see in their server logs.
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36',
    'From': 'YOUR NAME HERE - youremailaddress@emailprovider.som'
}

# because we're just loading a regular webpage, we send a `get` request to the
# URL, along with our informational headers
mta_webpage = requests.get(mta_turnstiles_index_url, headers=headers)

# opening up a local file to save the contents of the webpage to
mta_turnstiles_output_file = open("MTA_turnstiles_index.html","w")

# the webpage's code is in the `text` property of the website's response
# so write that to our file
mta_turnstiles_output_file.write(mta_webpage.text)

# close our output file!
mta_turnstiles_output_file.close()
