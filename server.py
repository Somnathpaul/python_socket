import socket
import threading

HEADER = 64
PORT = 6060
HOST = '127.0.0.1'
ADDR = (HOST, PORT)
DISCONNECT = "!close"

# AF_INET = IpV4
# SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s.bind(ADDR)

def handel_client(conn, addr):
    print(f"[New connection] {addr} connected")
    connection  = True
    while connection:
        msg_length  = conn.rcv(HEADER).decode("utf-8")
        msg_length = int(msg_length)
        msg = conn.rcv(msg_length).decode("utf-8")

        if msg == DISCONNECT:
            connection = False

        print(f"[{addr} {msg}]")
        conn.close()

def start_server():
    s.listen()
    print(f"[LISTENING] Listenning on ip : {HOST}")
    while True:
        conn , addr = s.accept()
        thread = threading.Thread(target=handel_client, args=(conn, addr))
        thread.start()
        print(f"[Active connection] {threading.activeCount() -1}")

print("[STARTING] Server starting at port ...")
start_server()