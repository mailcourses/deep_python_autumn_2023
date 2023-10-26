# David Beazley algo
import socket
from select import select


tasks = []
# sock: gen
to_read = {}
to_write = {}


def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 25000))
    server_sock.listen()

    while True:
        yield 'read', server_sock
        client_sock, addr = server_sock.accept()  # read
        print('connect from', addr)

        tasks.append(client(client_sock))


def client(client_sock):
    while True:
        yield 'read', client_sock
        data = client_sock.recv(4096)  # read

        if not data:
            break
        else:
            yield 'write', client_sock
            client_sock.send(data.decode().upper().encode())  # write

    client_sock.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            op_type, sock = next(task)

            if op_type == 'read':
                to_read[sock] = task
            elif op_type == 'write':
                to_write[sock] = task

        except StopIteration:
            pass


if __name__ == '__main__':
    tasks.append(server())
    event_loop()
