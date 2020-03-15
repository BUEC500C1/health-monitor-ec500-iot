from .gmail_handler import send_email


class Alarm():
    def __init__(self, threshold_low, threshold_high, name="default_alarm"):
        self.threshold_low = threshold_low
        self.threshold_high = threshold_high
        self.name = name

    def check_threshold(self, value):
        if not self.threshold_low < value < self.threshold_high:
            print(
                f"Alarm {self.name} went out of range ({self.threshold_low}, {self.threshold_high}) with value {value}!")
            send_email()


alarms = {
    "pulse": Alarm(80, 130, name="pulse"),
    "oxygen": Alarm(90, 100, name="oxygen"),
    "blood_pressure": Alarm(90, 160, name="blood_pressure"),
}


def update(oxygen, pulse, blood_pressure):
    alarms["oxygen"].check_threshold(oxygen)
    alarms["pulse"].check_threshold(pulse)
    alarms["blood_pressure"].check_threshold(blood_pressure)


if __name__ == '__main__':
    update(50, 70, 40)
