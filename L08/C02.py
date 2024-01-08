#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send 'GET_KEY' to download a string.
# The string is compressed with a common algorithm found in many
# websites. Decompress the string and print it to get the flag.
#

import socket, gzip

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))
sock.send("GET_KEY".encode())
print(gzip.decompress(sock.recv(1024)))
