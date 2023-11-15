#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#

# ngl I feel mildly guilty
# ty SO

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))
sock.send("ls /tmp".encode())
print(sock.recv(1024).decode())
