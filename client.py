import socket

# AF_INET = IpV4
# SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s.connect((socket.gethostbyname(socket.gethostname()), 1234))

# define buffer size
msg = s.recv(1024)
print(msg.decode("utf-8"))
