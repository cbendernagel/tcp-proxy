import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234))
    message = input("forward to dest: ")
    s.sendall(message.encode())
    while True:
        message = input("<- ")
        if message == "exit":
            s.close()
            break
        else:
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"-> {data}")