# SQLite3 Database

## Finished ground work for sqlite3 database CRUD functions
### You can:

- Create a local database called 'database.db'.
- Create required data and alert tables; does not recreate if pre-existing.
- Add (update table) with an item for a specific data type (Oxygen, Pulse, Blood Pressure).
- Add (update table) with up to all three data types at once.
- Get table information, patient information, or one data type from one patient.
- Delete a patient from both tables.

In the main function, there is some testing implementation to review how the functions work



## Usage
### Alerts
```
# set up an alarm with a lower and upper threshold of 80 and 130
pulse_alarm = Alarm(80, 130, name="pulse")

# this will cause an alarm because the 2nd parameter (which represents pulse) is too high
pulse_alarm.check_threshold('my_patient_id', 150)

# if you want check the threshold on all pre-set alarms
# this calls check_threshold on all the default alarms
update("some_id", oxygen=50, pulse=100, bps=120, bpd=80)
```


### Data Collector / Vendor
```
# set up a new data vendor
vendor = DataVendor()

# start the thread that keeps values updated
vendor.start_receive()

# get the most recent values from the vendor
values = vendor.get_values()

# values will be a tuple with the following structure
# (patient_id, bps, bpd, pulse, oxygen)
# to unpack the values into individual variables
patient_id, bps, bpd, pulse, oxygen = vendor.get_values()
```

### Scheduler
```python
scheduler = Scheduler()

# or minuets=1 or hours=1 ... etc. check documentation for other input args
id = scheduler.create_job(myfunc, seconds=1)

print(scheduler.list_jobs())

scheduler.remove_job(id)
```

Note that all job creations and deletions are logged in `/scheduler/scheduler.log`

Refer to `/scheduler/example.py` for full example

All input args for `Scheduler.create_job(myfunc, args)` can be found [here](https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html) 