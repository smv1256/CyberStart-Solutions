#
# The Tweet Bot API can be found at http://127.0.0.1:8082
#
# GET method sent to that URL:
# ...returns basic info about API
#
# POST method sent to that URL, with:
# - x-api-key:{KEY} in header
# - user={USER} in querystring
# - status-update={TEXT} in querystring
# ...creates a new social media post

# ez B)
# don't bother with the GET request btw
# this challenge took literally like a minute _lol_

from urllib import parse, request

data = parse.urlencode({ "user" : "tweetbotuser", "status-update" : "alientest" }).encode()

print(request.urlopen(request.Request("http://127.0.0.1:8082", headers = { "x-api-key" : "tweetbotkeyv1" }, data = data)).read())
