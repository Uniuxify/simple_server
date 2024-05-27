import time

import server
import client


def main():
    # mode = 'you'
    mode = 'client'

    local_server = server.Server('localhost', 8080)
    local_server.start()

    if mode == 'client':
        time.sleep(1)
        cl1 = client.Client()
        cl1.connect('localhost', 8080)
        cl1.send_message(b'Message from client1')
        time.sleep(1)
        cl1.send_message(b'Another message from client1')
        cl2 = client.Client()
        cl2.connect('localhost', 8080)
        cl2.send_message(b'Message from client2')

        cl2.send_message_timer(b'Ping message from client2', 2)
        cl1.send_message_timer(b'Ping message from client1', 1)

    if mode == 'you':
        your_client = client.Client()
        your_client.connect('localhost', 8080)
        time.sleep(1)
        while True:
            your_client.send_message(bytes(input('Введите сообщение для сервера: '), 'utf-8'))



if __name__ == '__main__':
    main()