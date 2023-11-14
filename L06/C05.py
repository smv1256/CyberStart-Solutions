#
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))

sock.send("GET_KEY".encode()) # send get key
sock.send(bytes(sock.recv(1024).decode()[::-1], "utf-8")) # reverse key, send back

print(sock.recv(1024).decode()) # print resp
