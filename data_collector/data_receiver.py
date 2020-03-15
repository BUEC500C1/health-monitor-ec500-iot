import socket
import struct
import os
from time import sleep


class DataReceiver():
    def __init__(self, socket_name):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(socket_name)

    def get_value(self):
        recvd = self.sock.recv(1)
        val, = struct.unpack('<B', recvd)
        return val


if __name__ == '__main__':
    pulse_receiver = DataReceiver('pulse.socket')
    while True:
        print(pulse_receiver.get_value())