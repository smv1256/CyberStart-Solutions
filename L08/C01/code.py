#
# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

# notes:
# The phrases we get from the server differ each run.
# This means I can't send them back to the server by hand because
# when I recieve the decrypted messages, I'll have to run the code again to send it,
# but when I run it again, the messages change along with the key used to decrypt them, rendering what I sent invalid.
# So, I need to find the valid outputs with words and then send them back [sock.send(<stuff>.encode())]
# but how do I find out if they're valid words or not?
# For example, if you look at the output file, I gotta send the output I got in:
# line 1, try 6; line 2, try 9; and line 3, try 7.
# What Sprout suggested with the dictionary API could work, gotta test that out, 
# but modules like enchant aren't allowed so there's a high chance you can't send API reqs either, so I wonder if there's another way...

import socket

# server stuff
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 10000))
sock.send("GET".encode()) # send GET to recieve encrypted version
s = sock.recv(1024).decode().split("\n") # what it returns --> 3 phrases split by a new line; each phrase has a different cipher key [like the first message could be shifted by one, the second by 23, and the third by 13 or smthn like that]
print(s, "\n") # print it out

# function to decrypt (and encrypt b'cuz why not)
def caesar(key, message, mode):
  m = message.upper()
  a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  output = ""
  
  for l in m: # characters in message
    if l in a: # if character is a letter
      # (originally used match case [https://github.com/SMVthe1st/Ciphers/blob/main/caesar.py] but it's unsupported here rip lol)
      if mode == "encrypt": # yeah this is irrelevant but why not
        ind = (a.find(l) + key) % len(a) # shift + for ciphertext letter
      elif mode == "decrypt":
        ind = (a.find(l) - key) % len(a) # shift - for original letter
      else:
        print("invalid mode")
      output = output + a[ind] # output string
    else:
      output = output + l # if it's a symbol, keep it
    
  return output

for x in range(1, 27): # loop through all possible key shifts [26 for all letters in the alphabet]
  for y in range(1, 4): # [there were 3 messages with different cipher keys]
    print("line %s, try %s: " % (str(y), str(x)) + caesar(x, s[y], "decrypt") + "\n") # printing it all out
    
