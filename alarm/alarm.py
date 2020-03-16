from gmail_handler import send_email
from config import config
import database


class Alarm():
    def __init__(self, threshold_low, threshold_high, name="default_alarm"):
        self.threshold_low = threshold_low
        self.threshold_high = threshold_high
        self.name = name

    def check_threshold(self, patient_id, value):
        if value is None:
            return
        if not self.threshold_low <= value <= self.threshold_high:
            print(
                f"Alarm {self.name} went out of range ({self.threshold_low}, {self.threshold_high}) with value {value}!")
            send_email(config['email']['notify'], patient_id, self.name, value,
                       (self.threshold_low, self.threshold_high))
            database.add_alerts_item(patient_id, self.name, self.threshold_low, self.threshold_high, value)


alarms = {
    "pulse": Alarm(65, 130, name="pulse"),
    "oxygen": Alarm(82, 100, name="oxygen"),
    "bps": Alarm(90, 160, name="bps"),
    "bpd": Alarm(50, 120, name="bpd")
}


def update(patient_id, oxygen=None, pulse=None, bps=None, bpd=None):
    alarms["oxygen"].check_threshold(patient_id, oxygen)
    alarms["pulse"].check_threshold(patient_id, pulse)
    alarms["bps"].check_threshold(patient_id, bps)
    alarms["bpd"].check_threshold(patient_id, bpd)


if __name__ == '__main__':
    update("some_id", oxygen=50, pulse=100, bps=120, bpd=80)
