# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.

resp = urllib.request.urlopen("http://127.0.0.1:8080/winning")
print(resp.read())
