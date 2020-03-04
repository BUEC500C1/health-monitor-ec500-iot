from scheduler import Scheduler
import time

#demo of the code
def myfunc():
    print("in job...")

scheduler = Scheduler()
id = scheduler.create_job(myfunc, seconds=1)

print(">>> created job", id)

scheduler.sched.start()
time.sleep(3)

print(scheduler.list_jobs())
time.sleep(5)

scheduler.remove_job(id)
print(">>> removed job", id)