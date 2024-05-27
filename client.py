import socket
import threading
import time


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, server, port):
        self.client_socket.connect((server, port))

    def send_message(self, msg):
        try:
            self.client_socket.sendall(msg)
            response = self.client_socket.recv(1024)
            print(f"Ответ от сервера: {response.decode('utf-8')}")
        except Exception as e:
            print(e)

    def ping_server(self, msg, delay):
        while True:
            try:
                self.client_socket.sendall(msg)
                response = self.client_socket.recv(1024)
                print(f"Ответ от сервера: {response.decode('utf-8')}")
            except Exception as e:
                print(e)
            time.sleep(delay)

    def send_message_timer(self, msg, delay):
        ping_server_thread = threading.Thread(target=self.ping_server, args=(msg, delay))
        ping_server_thread.start()


    def __del__(self):
        self.client_socket.close()
