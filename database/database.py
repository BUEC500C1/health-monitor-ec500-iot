import sqlite3
import datetime

def connect_database():
    db = sqlite3.connect('database.db')
    return db

def get_time():
    return str(datetime.datetime.now())

'''
    Oxygen (Saturation): A Percentage
        e.g 97% or 0.97
    Pulse: Beats per minute
        e.g. 80 beats per minute
    Blood Pressure: systolic blood pressure / diastolic blood pressure
        e.g. 120/80

'''
def create_tables():
    db = connect_database()
    print("Creating tables . . . ")
    # Checks if table exists before creation
    db.execute('create table if not exists Data (PatientID TEXT, Timestamp TEXT, Type TEXT, Value TEXT)')
    db.execute('create table if not exists Alerts (PatientID TEXT, Timestamp TEXT, Type TEXT, ThresholdLow TEXT, ThresholdHigh TEXT, Value TEXT)')

'''
Description:
    add_data_item adds one type (bp, o, p) item to the data database

inputs:
    patientID: The patient's identification code
    timestamp: Time recorded
    entrytype: Data type to be stored
    value:     The type's value to be stored
'''
def add_data_item(patientID, entrytype, value):
    db = connect_database()
    if value is None:
        return

    db.execute("INSERT INTO Data (PatientID, Timestamp, Type, Value) \
               VALUES (?,?,?,?)",(patientID, get_time(), entrytype, value) )
    db.commit()
    print("Data item added successfully")

'''
Description:
    add_all_into_data adds up to all three items to the data database;
    when calling, use parameterized function syntax

inputs:
    patientID:  The patient's identification code
    oxygen:     Oxygen level, can be left out
    pulse:      Pulse value, can be left out
    bps:        Systolic Blood Pressure level, can be left out
    bpd:        Diastolic Blood Pressure level, can be left out
'''
def add_all_into_data(patientID, oxygen=None, pulse=None, bps=None, bpd=None):
    db = connect_database()
    add_data_item(patientID, 'oxygen', oxygen)
    add_data_item(patientID, 'pulse', pulse)
    add_data_item(patientID, 'bps', bps)
    add_data_item(patientID, 'bpd', bpd)

'''
Description:
    add_alerts_item adds an alert item to the alert database

inputs:
    patientID:      The patient's identification code
    entrytype:      Either Oxygen 'oxygen', Pulse 'pulse', or Systolic or Diastolic Blood Pressure 'bps' or 'bpd'
    threshold_low:  Lower threshold value for type entrytype
    threshold_high: Higher threshold value for type entrytype
    value:          actual recorded value
'''
def add_alerts_item(patientID, entrytype, threshold_low, threshold_high, value):
    db = connect_database()
    db.execute("INSERT INTO Alerts (PatientID, Timestamp, Type, ThresholdLow, ThresholdHigh, Value) \
               VALUES (?,?,?,?,?,?)",(patientID, get_time(), entrytype, threshold_low, threshold_high, value) )
    db.commit()
    print("Alerts item added successfully")

# get_entire_table returns all entries of the desired table
def get_entire_table(table):
    cur = connect_database().cursor()
    cur.execute(f"select * from {table}")
    rows = cur.fetchall(); 
    return rows

# get_all_info_for_patientid returns all items for a specific patient
def get_all_info_for_patientid(tablename, patientid):
    cur = connect_database().cursor()
    cur.execute(f"SELECT * FROM {tablename} WHERE PatientID=?", (patientid,))
    rows = cur.fetchall()
    return rows

# get_entrytype_info_for_patientid returns all items of a specific type for a specific patient
def get_entrytype_info_for_patientid(tablename, patientid, entrytype):
    db = connect_database()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tablename} WHERE PatientID=? AND Type=?", (patientid,entrytype,))
    rows = cur.fetchall()
    return rows

# delete_patient deletes all information about a patient from both tables
def delete_patient(patientid):
    db = connect_database()
    cur = db.cursor()
    cur.execute(f"DELETE FROM Data WHERE PatientID=?", (patientid,))
    cur.execute(f"DELETE FROM Alerts WHERE PatientID=?", (patientid,))
    db.commit()
    print(f"Patient {patientid} has been deleted")

# print_all_tables prints both tables to the terminal line
def print_all_tables():
    db = connect_database()
    # List all entries in the tables 'Data' and 'Alerts'
    data_all = get_entire_table(db, 'Data')
    alerts_all = get_entire_table(db, 'Alerts')
    print("\n[~~~] TABLE DATA [~~~]\n", data_all)
    print("\n[~~~] TABLE ALERTS [~~~]\n", alerts_all)

# close_database closes the opened database
def close_database(db):
    db.close()
    print("Database closed successfully")

if __name__ == '__main__':
    print("Initializing Main Function . . .")

    # Create tables Data and Alerts if not present
    create_tables()

    # Add data and alert items for Patient ID '1141'
    add_all_into_data('1141', oxygen='0.95', bps='120/80', pulse='100')
    add_alerts_item('1141', 'oxygen', '0.95', '0.96', '0.97')

    # Get all info from table Data on Patient '1141' and print out to terminal
    all_info = get_all_info_for_patientid('Data', '1141')
    oxygen_info = get_entrytype_info_for_patientid('Data', '1141', 'O')
    print(f"\nAll info for Patient '1141': {all_info}\n")
    print(f"Oxygen info for Patient '1141': {oxygen_info}\n")

    # Delete all information about Patient '1141'
    delete_patient('1141')

    # Reprint information to confirm all info deleted for Patient '1141'
    all_info = get_all_info_for_patientid('Data', '1141')
    print(f"All info for Patient '1141': {all_info}\n")

    # Call update function to add all three datatypes at once
    add_all_into_data('1141', oxygen='0.95', bpd='120/80')
    add_all_into_data('1141', oxygen='0.98', pulse='100')

    # Reprint information for recent addition after deletion for Patient '1141'
    all_info = get_all_info_for_patientid('Data', '1141')
    print(f"All info for Patient '1141': {all_info}\n")

    # Clean database for next iteration of testing
    delete_patient('1141')
