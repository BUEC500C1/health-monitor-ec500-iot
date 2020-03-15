from gmail_handler import send_email

EMAIL_TO_NOTIFY = "rjewing@bu.edu"  # Set to the email you want to notify


class Alarm():
    def __init__(self, threshold_low, threshold_high, name="default_alarm"):
        self.threshold_low = threshold_low
        self.threshold_high = threshold_high
        self.name = name

    def check_threshold(self, value):
        if value is None:
            return
        if not self.threshold_low < value < self.threshold_high:
            print(
                f"Alarm {self.name} went out of range ({self.threshold_low}, {self.threshold_high}) with value {value}!")
            send_email(EMAIL_TO_NOTIFY, self.name, value,
                       (self.threshold_low, self.threshold_high))


alarms = {
    "pulse": Alarm(80, 130, name="pulse"),
    "oxygen": Alarm(90, 100, name="oxygen"),
    "bps": Alarm(90, 160, name="blood_pressure_systolic"),
    "bpd": Alarm(50, 120, name="blood_pressure_diastolic")
}


def update(patiend_id, oxygen=None, pulse=None, bps=None, bpd=None):
    alarms["oxygen"].check_threshold(oxygen)
    alarms["pulse"].check_threshold(pulse)
    alarms["bps"].check_threshold(bps)
    alarms["bpd"].check_threshold(bpd)


if __name__ == '__main__':
    update("some_id", oxygen=50, pulse=100, bps=120, bpd=80)
