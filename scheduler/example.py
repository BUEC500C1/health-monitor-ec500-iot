from scheduler import Scheduler
import time

def myfunc():
    print("in job...")

scheduler = Scheduler()

# or minuets=1 or hours=1 ... etc. check documentation for other input args
id = scheduler.create_job(myfunc, seconds=1)
print(">>> created job", id)

time.sleep(3)

print(scheduler.list_jobs())

time.sleep(5)

scheduler.remove_job(id)
print(">>> removed job", id)
