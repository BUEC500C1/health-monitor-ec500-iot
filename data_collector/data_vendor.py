from data_receiver import DataReceiver
from threading import Thread
from time import sleep
import uuid
import data_vendor


class DataVendor():
    def __init__(self):
        self.patient_id = str(uuid.uuid4())
        self.bp_sock = DataReceiver('bp.socket')
        self.pulse_sock = DataReceiver('pulse.socket')
        self.oxygen_sock = DataReceiver('oxygen.socket')

        self.bps = None
        self.bpd = None
        self.pulse = None
        self.oxygen = None

    def get_values(self):
        return (self.patient_id, self.bps, self.bpd, self.pulse, self.oxygen)

    def start_receive(self):
        t = Thread(target=self.receiver, daemon=True)
        t.start()

    def receiver(self):
        while True:
            self.bps = self.bp_sock.get_value()
            self.bpd = self.bps - 40  # Fake a normal offset for diastolic
            self.pulse = self.pulse_sock.get_value()
            self.oxygen = self.oxygen_sock.get_value()
            sleep(0.05)


if __name__ == '__main__':
    vendor = DataVendor()
    vendor.start_receive()
    while True:
        print(vendor.get_values())
        sleep(0.5)
