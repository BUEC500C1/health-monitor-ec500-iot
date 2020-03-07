import socket
import sys
import os
import threading
from smooth_random import SmoothRandom


class FakeDataSender():
    def __init__(self, socket_name: str, lower_limit: int, upper_limit: int, variance: int):
        self.sock_name = socket_name
        self.data_gen = SmoothRandom(lower_limit, upper_limit, variance)
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            os.unlink(self.sock_name)
        except OSError:
            if os.path.exists(self.sock_name):
                raise
        self.sock.bind(socket_name)
        self.sock.listen(1)
        self.closed = False

    def send_data(self, connection):
        try:
            val = str(next(self.data_gen)).encode('ascii')
            connection.sendall(val + b'\n')
            t = threading.Timer(0.1, self.send_data, args=(connection,))
            t.daemon = True
            t.start()
        except socket.error:
            connection.close()

    def get_connection(self):
        while not self.closed:
            # Wait for a connection
            print('waiting for a connection', file=sys.stderr)
            connection, client_address = self.sock.accept()
            print('connection from', client_address, file=sys.stderr)

            self.send_data(connection)

    def close(self):
        self.closed = True
        self.sock.close()
        os.unlink(self.sock_name)


if __name__ == '__main__':
    try:
        s = FakeDataSender("uds_socket", 50, 150, 1)
        s.get_connection()
    except KeyboardInterrupt:
        s.close()
