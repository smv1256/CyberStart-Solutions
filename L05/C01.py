#
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address.
# Record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#

import socket
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 10000))
sock.listen(10)

while True:
  connection, address = sock.accept()
  data = connection.recv(1024).decode()
  if len(data) > 0:
    with open("/tmp/aliensignallog.txt", "w") as file:
      file.write(data)
      connection.close()
  break
