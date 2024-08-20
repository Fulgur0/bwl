import socket
import threading
from bwl.bwl import get_ip

class Client:
    def __init__(self, ip, port):
        self.active = True
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client.connect((self.ip, self.port))

        recv_thread = threading.Thread(target=self.recv)
        recv_thread.start()

    def recv(self):
        try:
            while self.active:
                try:
                    data = self.client.recv(1024).decode('utf-8')
                    if not data:
                        break
                    print(data)
                    self.active = False
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(data.encode('utf-8'))
        except Exception as e:
            print(e)

domain = input("Enter the domain: ")
ip = get_ip(domain)['ip']
print("IP: " + ip)
ipSplit = ip.split(':')
client = Client(ipSplit[0], int(ipSplit[1]))
client.connect()
client.send("BWL /")