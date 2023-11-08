# CHALLENGE 1: Write a TCP Client that will connect to 127.0.0.1 on
#              port 9990.
#              Your client must send "Knock, knock" to the server.
#              Then get the response, and print it out.

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 9990))
sock.send("Knock, knock".encode())
resp = sock.recv(1024)
print(resp)
