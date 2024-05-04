import os
import socket
from route_management.route_manager import RouteManager

class ProxyServer():
    
    def __init__(self, listen_port, route_manager: RouteManager):
        self.listen_port = listen_port
        self.route_manager = route_manager
        
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", self.listen_port))
            s.listen()
            conn, addr = s.accept()
            while True:
                print(f"Connection received: {addr}")
                data = conn.recv(1024).decode()
                dest = self.route_manager.routes.get(str(data))
                print(f"forwarding connection to: {dest}")
                pid = os.fork()
                if pid <= 0:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
                        c.connect((dest.get("remoteIp"), dest.get("remotePort")))
                        forwarder = Forwarder(conn, addr, c, dest.get("remoteIp"))
                        forwarder.run()
                else:
                    s.close()
                    break
                
                
class Forwarder():
    
    def __init__(self, inbound: socket.socket, in_addr, outbound: socket.socket, out_addr):
        self.inbound = inbound
        self.in_addr = in_addr
        self.outbound = outbound
        self.out_addr = out_addr
        
    def run(self):
        while True:
            # wait for client to send something
            message = self.inbound.recv(1024)
            print(f"forwarding {message} to {self.out_addr}")
            self.outbound.sendall(message)
            # Send response back to client
            message = self.outbound.recv(1024)
            print(f"forwarding {message} to {self.in_addr}")
            self.inbound.sendall(message)
            
        
                
                
                
