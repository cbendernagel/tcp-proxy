import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 2345))
    s.listen()
    conn, addr = s.accept()
    print(f"Connection received: {addr}")
    while True:
        data = conn.recv(1024)
        print(f"Received \"{data}\" from {addr}")
        conn.sendall(data)