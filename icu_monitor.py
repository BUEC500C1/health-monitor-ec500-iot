import sys
from time import sleep

sys.path.extend(['./alarm', './data_collector', './data_generation', './database', './scheduler'])

import database  # noqa: E402
import scheduler  # noqa: E402
import alarm  # noqa: E402
import data_vendor  # noqa: E402


def main():
    vendor = data_vendor.DataVendor()
    vendor.start_receive()

    database.create_tables()
    sched = scheduler.Scheduler(vendor)

    sched.create_job(database.add_all_into_data, seconds=10)
    sched.create_job(alarm.update, seconds=1)

    while True:
        sleep(1)


if __name__ == '__main__':
    main()
