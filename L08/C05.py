#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

from urllib import parse, request
import re

while True:
  out = request.urlopen(request.Request("http://127.0.0.1:8082/selfdestruct")).read().decode("utf-8")
  num = re.findall("[0-9]+", out)
  print(num)
  if num[0] == num[1]:
    print(out)
    break
    
