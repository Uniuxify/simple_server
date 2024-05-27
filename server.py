import socket
import threading


class Server:
    def __init__(self, address, port):
        self.port = port
        self.address = address

        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.address, self.port))
        self.server_socket.listen()
        print('Сервер запущен')

        listen_thread = threading.Thread(target=self.listen_loop)
        listen_thread.start()

    def listen_loop(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Принято соединение от {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        """Обрабатывает соединение с клиентом в отдельном потоке."""
        try:
            while True:
                message = client_socket.recv(1024)
                if not message:
                    break
                client_socket.sendall(message)
        finally:
            client_socket.close()


