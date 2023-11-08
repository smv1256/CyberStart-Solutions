#
# Connect to alien server ('localhost', 10000)
#
# Then send each of these values...
# USER
# aliensignal
# PASS
# unlockserver
# SEND
# moonbase
# END
# ...and receive the response from each.
#
# Note: You must receive data back from the server after you send each value
#

import socket

vals = ["USER", "aliensignal", "PASS", "unlockserver", "SEND", "moonbase", "END"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))

for x in vals:
  sock.send(x.encode())
  print(sock.recv(1024))

# halfway done, lessgooo
# been super duper ez thus far...
