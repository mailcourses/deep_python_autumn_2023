import socket
import selectors

selector = selectors.DefaultSelector()
print('selector', selector)


def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 17000))
    server_sock.listen(5)

    selector.register(server_sock, selectors.EVENT_READ, accept_conn)


def accept_conn(server_sock):
    client_sock, addr = server_sock.accept()
    print('Connect', addr)
    selector.register(client_sock, selectors.EVENT_READ, respond)


def respond(client_sock):
    data = client_sock.recv(4096)

    if data:
        client_sock.send(data.decode().upper().encode())
    else:
        print("close client")
        selector.unregister(client_sock)
        client_sock.close()


def event_loop():
    while True:
        events = selector.select()  # (key, events_mask)

        for key, _ in events:
            # key: NamedTuple(fileobj, events, data)
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
