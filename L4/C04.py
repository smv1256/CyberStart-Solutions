#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout. If this occurs try narrowing
# down your search
#

import urllib.request

for x in range(5500, 5601):	
	print(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8082", headers = { "x-api-key" : x })).read())

# this one took me so long I'm actually so dumb lol
# the number the flag is on changes btw
