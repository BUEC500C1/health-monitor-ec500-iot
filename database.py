import sqlite3

def connect_database():
    conn = sqlite3.connect('database.db')
    print("Database opened successfully")
    return conn

'''
    Oxygen (Saturation): A Percentage
        e.g 97% or 0.97
    Pulse: Beats per minute
        e.g. 80 beats per minute
    Blood Pressure: systolic blood pressure / diastolic blood pressure
        e.g. 120/80

'''
def create_tables(db):
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
    entrytype: Either Oxygen 'O', Pulse 'P', or Blood Pressure 'BP'
    value:     The type's value to be stored
'''
def add_data_item(db, patientID, timestamp, entrytype, value):
    if value is None:
        return

    db.execute("INSERT INTO Data (PatientID, Timestamp, Type, Value) \
               VALUES (?,?,?,?)",(patientID, timestamp, entrytype, value) )
    db.commit()
    print("Data item added successfully")

'''
Description:
    add_all_types_items adds up to all three items to the data database;
    when calling, use parameterized function syntax

inputs:
    patientID:      The patient's identification code
    timestamp:      Time recorded
    oxygenValue:    Oxygen level, can be left out
    pulseValue:     Pulse value, can be left out
    bpValue:        Blood Pressure level, can be left out
'''
def add_all_types_items(db, patientID, timestamp, oxygenValue=None, pulseValue=None, bpValue=None):
    add_data_item(db, patientID, timestamp, 'O', oxygenValue)
    add_data_item(db, patientID, timestamp, 'P', pulseValue)
    add_data_item(db, patientID, timestamp, 'BP', bpValue)

'''
Description:
    add_alerts_item adds an alert item to the alert database

inputs:
    patientID:      The patient's identification code
    timestamp:      Time recorded
    entrytype:      Either Oxygen 'O', Pulse 'P', or Blood Pressure 'BP'
    threshold_low:  Lower threshold value for type entrytype
    threshold_high: Higher threshold value for type entrytype
    value:          actual recorded value
'''
def add_alerts_item(db, patientID, timestamp, entrytype, threshold_low, threshold_high, value):
    db.execute("INSERT INTO Alerts (PatientID, Timestamp, Type, ThresholdLow, ThresholdHigh, Value) \
               VALUES (?,?,?,?,?,?)",(patientID, timestamp, entrytype, threshold_low, threshold_high, value) )
    db.commit()
    print("Alerts item added successfully")


# get_entire_table returns all entries of the desired table
def get_entire_table(db, table):
    cur = db.cursor()
    cur.execute(f"select * from {table}")
    rows = cur.fetchall(); 
    return rows

# get_all_info_for_patientid returns all items for a specific patient
def get_all_info_for_patientid(db, tablename, patientid):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tablename} WHERE PatientID=?", (patientid,))
    rows = cur.fetchall()
    return rows

# get_entrytype_info_for_patientid returns all items of a specific type for a specific patient
def get_entrytype_info_for_patientid(db, tablename, patientid, entrytype):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tablename} WHERE PatientID=? AND Type=?", (patientid,entrytype,))
    rows = cur.fetchall()
    return rows

# delete_patient deletes all information about a patient from both tables
def delete_patient(db, patientid):
    cur = db.cursor()
    cur.execute(f"DELETE FROM Data WHERE PatientID=?", (patientid,))
    cur.execute(f"DELETE FROM Alerts WHERE PatientID=?", (patientid,))
    db.commit()
    print(f"Patient {patientid} has been deleted")

# print_all_tables prints both tables to the terminal line
def print_all_tables(db):
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

    # Connect to database.db or create if not present
    db = connect_database()

    # Create tables Data and Alerts if not present
    create_tables(db)

    # Add data and alert items for Patient ID '1141'
    add_data_item(db, '1141', '2020-03-14 14:09:10.131', 'O', '0.97')
    add_data_item(db, '1141', '2020-03-14 14:11:10.131', 'P', '90')
    add_data_item(db, '1141', '2020-03-14 14:10:10.131', 'BP', '120/80')
    add_alerts_item(db, '1141', '2020-03-14 14:09:10.131', 'O', '0.95', '0.96', '0.97')

    # Get all info from table Data on Patient '1141' and print out to terminal
    all_info = get_all_info_for_patientid(db, 'Data', '1141')
    oxygen_info = get_entrytype_info_for_patientid(db, 'Data', '1141', 'O')
    print(f"\nAll info for Patient '1141': {all_info}\n")
    print(f"Oxygen info for Patient '1141': {oxygen_info}\n")

    # Delete all information about Patient '1141'
    delete_patient(db, '1141')

    # Reprint information to confirm all info deleted for Patient '1141'
    all_info = get_all_info_for_patientid(db, 'Data', '1141')
    print(f"All info for Patient '1141': {all_info}\n")

    # Call update function to add all three datatypes at once
    add_all_types_items(db, '1141', '2020-03-15 14:11:10.131', oxygenValue='0.95', bpValue='120/80')
    add_all_types_items(db, '1141', '2020-03-16 14:11:10.131', oxygenValue='0.98', pulseValue='100')

    # Reprint information for recent addition after deletion for Patient '1141'
    all_info = get_all_info_for_patientid(db, 'Data', '1141')
    print(f"All info for Patient '1141': {all_info}\n")

    # Close the database once finished with all tasks
    close_database(db)