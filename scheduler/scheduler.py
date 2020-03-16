from apscheduler.schedulers.background import BackgroundScheduler
import uuid
import logging
from data_collector import data_vendor


class Scheduler():
    def __init__(self, vendor):
        self.data_vendor = vendor
        self.sched = BackgroundScheduler(timezone='EST')
        self.jobSet = []
        self.sched.start()
        # removed temporarily to see output in stdout
        # logging.basicConfig(filename='scheduler.log', level=logging.DEBUG)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sched.shutdown()

    def create_job(self, func, **kwargs):
        jobId = str(uuid.uuid4())
        self.sched.add_job(lambda: self.task_wrapper(func),
                           'interval', id=jobId, **kwargs)
        self.jobSet.append(jobId)
        logging.info('Created job with UUID: {}'.format(jobId))
        return jobId

    def remove_job(self, jobId):
        self.sched.remove_job(jobId)
        logging.info('Removed job with UUID: {}'.format(jobId))

    def list_jobs(self):
        return self.jobSet

    def task_wrapper(self, actual_func):
        # TODO: import data_vendor when project is properly structured
        print("Running func", actual_func)
        patient_id, bps, bpd, pulse, oxygen = self.data_vendor.get_values()
        actual_func(patient_id, bps=bps, bpd=bpd, pulse=pulse, oxygen=oxygen)
