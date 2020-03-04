from apscheduler.schedulers.background import BackgroundScheduler
import uuid
import logging

class Scheduler():
    def __init__(self):
        self.sched = BackgroundScheduler(timezone='EST')
        self.jobSet = []
        self.sched.start()
        logging.basicConfig(filename='scheduler.log',level=logging.DEBUG)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sched.shutdown()

    def create_job(self, func, **kwargs):
        jobId = str(uuid.uuid4())
        self.sched.add_job(func, 'interval', id=jobId, **kwargs)
        self.jobSet.append(jobId)
        logging.info('Created job with UUID: {}'.format(jobId))


        return jobId

    def remove_job(self, jobId):
        self.sched.remove_job(jobId)
        logging.info('Removed job with UUID: {}'.format(jobId))


    def list_jobs(self):
        return self.jobSet
