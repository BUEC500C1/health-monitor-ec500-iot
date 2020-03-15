from data_receiver import DataReceiver
from threading import Thread
from time import sleep


class DataVendor():
    def __init__(self):
        self.bp_sock = DataReceiver('bp.socket')
        self.pulse_sock = DataReceiver('pulse.socket')
        self.oxygen_sock = DataReceiver('oxygen.socket')

        self.bp = None
        self.pulse = None
        self.oxygen = None

    def get_values(self):
        return (self.bp, self.pulse, self.oxygen)

    def start_receive(self):
        t = Thread(target=self.receiver, daemon=True)
        t.start()

    def receiver(self):
        while True:
            self.bp = self.bp_sock.get_value()
            self.pulse = self.pulse_sock.get_value()
            self.oxygen = self.oxygen_sock.get_value()
            sleep(0.1)


if __name__ == '__main__':
    vendor = DataVendor()
    vendor.start_receive()
    while True:
        print(vendor.get_values())
        sleep(0.5)
