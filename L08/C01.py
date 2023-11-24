#
# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

import socket, re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))
sock.send("GET".encode())
s = sock.recv(1024).decode().split("\n")
print(s, "\n")

def caesar(key, message, mode):
  m = message.upper()
  a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  output = ""
  
  for l in m:
    if l in a:
      if mode == "encrypt":
        ind = (a.find(l) + key) % len(a)
      elif mode == "decrypt":
        ind = (a.find(l) - key) % len(a)
      else:
        print("invalid mode")
      output = output + a[ind]
    else:
      output = output + l
    
  return output

t = []

for x in range(1, 27):
  for y in range(1, 4):
    dec = caesar(x, s[y], "decrypt")
    if "THE" in dec:
      t.append(dec)
      
if len(t) == 3:
  sock.send("\n".join(t).encode())
  print("\n", sock.recv(1024).decode())

      
