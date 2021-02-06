from Twitter_credentials import auth_ready_key

# include the requests library in order to get data from the web
import requests

# specify the Twitter endpoint that we can use to request an access token
# or bearer token
auth_url = 'https://api.twitter.com/oauth2/token'


# construct a dict containing the information the authorization endpoint wants
# in order to return an access token to us. This includes the "header"
# information, which gives the endpoint our encoded key and tells it about
# the data formatting
auth_headers = {
    'Authorization': 'Basic '+auth_ready_key,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

# we also need to pass along information about what we're asking for. The
# format of both the headers and the data is decided by the API provider,
# so we're just following their directions here
auth_data = {
    'grant_type': 'client_credentials'
}

# now we actually make our complete request to the authorization endpoint
# the "post" recipe sends this in a more protected way than just
# putting all of these values into the URL as we did with the FRED API
# because the data we're getting back (which contains our access/bearer token)
# also needs to be protected. The data sent back will be stored
# in this variable
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# pull the access token out of the data sent back from the authorization
# endpoint
access_token = auth_resp.json()['access_token']


# now that we have an access/bearer token, we're ready to request some data!
# we'll create a new dict that includes this token
search_headers = {
    'Authorization': 'Bearer '+access_token
}

# this is the Twitter search API endpoint
search_url  = 'https://api.twitter.com/1.1/search/tweets.json'

# we'll create a new dict that includes our search query parameters
# in this case, our query (`q`) is "Python", we're looking for recent results
# and we want a maximum of 4 Tweets back
search_params = {
    'q': 'Python',
    'result_type': 'recent',
    'count': 4
}

# now we can build and send our data request; the data sent back will be stored
# in this variable
search_resp = requests.get(search_url, headers=search_headers, params=search_params)

# let's create an output file where we can store the results
Twitter_output_file = open("Twitter_search_results.json", "w")

# write the returned Twitter data to our output file
Twitter_output_file.write(str(search_resp.json()))

# close the output file
Twitter_output_file.close()
