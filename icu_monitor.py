import sys
from time import sleep
from config import config

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

    sched.create_job(database.add_all_into_data, seconds=config['scheduler']['database']['interval'])
    sched.create_job(alarm.update, seconds=config['scheduler']['alarm']['interval'])

    while True:
        sleep(1)


if __name__ == '__main__':
    main()
