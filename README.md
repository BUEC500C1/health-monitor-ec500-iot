# Health Monitor
## How to run
1. `$ pip3 install -r requirements.txt`
2. Run as separate processes:
   ```
    $ python3 data_generation/oxygen_collector.py &
    $ python3 data_generation/bp_collector.py &
    $ python3 data_generation/pulse_collector.py &
   ```
3. Run the main health monitor:
   ```
    $ python3 icu_monitor.py
   ```

## SQLite3 Database

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
