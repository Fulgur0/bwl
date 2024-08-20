import socket
import threading

with open('index.html', 'r') as file:
    index_html = file.read()

class Client:
    def __init__(self, client_socket, addr):
        self.client_socket = client_socket
        self.addr = addr

    def recv(self):
        try:
            return self.client_socket.recv(1024).decode('utf-8')
        except Exception as e:
            print(e)

    def send(self, data):
        print("Sending data to " + str(self.addr))
        try:
            self.client_socket.send(data.encode('utf-8'))
        except Exception as e:
            print(e)

def handle_client(client_socket, addr):
    try:
        client = Client(client_socket, addr)
        while True:
            try:
                data = client.recv()
                if not data:
                    client_socket.close()
                    break
                if data == 'BWL /':
                    client.send(index_html)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

def run_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 3030))
        server.listen()
        print("Server is running on port 3030")

        while True:
            client_socket, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_socket, addr)).start()
    except Exception as e:
        print(e)

run_server()