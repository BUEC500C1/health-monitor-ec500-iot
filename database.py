import sqlite3

def connect_database():
    conn = sqlite3.connect('database.db')
    print("Database opened successfully")
    return conn

# TODO: Decide what to store ID, Timestamp, and Value as
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
    db.execute('create table if not exists Alerts (PatientID TEXT, Timestamp TEXT, Type TEXT, Threshold TEXT, Value TEXT)')


def add_data_item(db, patientID, timestamp, entrytype, value):
    db.execute("INSERT INTO Data (PatientID, Timestamp, Type, Value) \
               VALUES (?,?,?,?)",(patientID, timestamp, entrytype, value) )
    db.commit()
    print("Data item added successfully")

def add_alerts_item(db, patientID, timestamp, entrytype, threshold, value):
    db.execute("INSERT INTO Alerts (PatientID, Timestamp, Type, Threshold, Value) \
               VALUES (?,?,?,?,?)",(patientID, timestamp, entrytype, threshold, value) )
    db.commit()
    print("Alerts item added successfully")

def get_entire_table(db, table):
    cur = db.cursor()
    cur.execute(f"select * from {table}")
    rows = cur.fetchall(); 
    return rows

def get_all_info_for_patientid(db, tablename, patientid):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tablename} WHERE PatientID=?", (patientid,))
    rows = cur.fetchall()
    print(rows)
    return rows

def get_entrytype_info_for_patientid(db, tablename, patientid, entrytype):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tablename} WHERE PatientID=? AND Type=?", (patientid,entrytype,))
    rows = cur.fetchall()
    print(rows)
    return rows

def print_all_tables(db):
    # List all entries in the tables 'Data' and 'Alerts'
    data_all = get_entire_table(db, 'Data')
    alerts_all = get_entire_table(db, 'Alerts')
    print("\n[~~~] TABLE DATA [~~~]\n", data_all)
    print("\n[~~~] TABLE ALERTS [~~~]\n", alerts_all)

def close_database(db):
    db.close()
    print("Database closed successfully")

if __name__ == '__main__':
    print("Initializing Main Function . . .")
    db = connect_database()
    create_tables(db)
    # add_data_item(db, '1141', '2020-03-14 14:09:10.131', 'O', '0.97')
    # add_data_item(db, '1141', '2020-03-14 14:10:10.131', 'BP', '120/80')
    # add_data_item(db, '1141', '2020-03-14 14:11:10.131', 'P', '90')

    # add_alerts_item(db, '1141', '2020-03-14 14:09:10.131', 'O', '0.96', '0.97')
    
    # print_all_tables(db)

    get_all_info_for_patientid(db, 'Data', '1141')
    get_entrytype_info_for_patientid(db, 'Data', '1141', 'O')
    
    close_database(db)