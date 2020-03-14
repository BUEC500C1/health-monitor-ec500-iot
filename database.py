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
    db.execute('CREATE TABLE Data (ID TEXT, Timestamp TEXT, Type TEXT, Value REAL)')
    db.execute('CREATE TABLE Alerts (ID TEXT, Timestamp TEXT, Type TEXT, Threshold REAL, Value REAL)')
    print("Tables 'Data' and 'Alerts' created successfully")

def add_data_item(db, id, timestamp, entrytype, value):
    db.execute("INSERT INTO Data (ID, Timestamp, Type, Value) \
               VALUES (?,?,?,?)",(id, timestamp, entrytype, value) )
    db.commit()
    print("Data item added successfully")

def add_alerts_item(db, id, timestamp, entrytype, threshold, value):
    db.execute("INSERT INTO Alerts (ID, Timestamp, Type, Threshold, Value) \
               VALUES (?,?,?,?,?)",(id, timestamp, entrytype, threshold, value) )
    db.commit()
    print("Alerts item added successfully")

def view_entire_table(db, table):
    cur = db.cursor()
    cur.execute(f"select * from {table}")
    rows = cur.fetchall(); 
    return rows

def close_database(db):
    db.close()
    print("Database closed successfully")

if __name__ == '__main__':
    print("Initializing Main Function . . .")
    db = connect_database()
    # create_tables(db)
    # add_data_item(db, '1', '2020-03-14 14:09:10.131', 'O', '0.97')
    # add_alerts_item(db, '1', '2020-03-14 14:09:10.131', 'O', '0.96', '0.97')
    
    # List all entries in the tables 'Data' and 'Alerts'
    data_all = view_entire_table(db, 'Data')
    alerts_all = view_entire_table(db, 'Alerts')
    print("\n[~~~] TABLE DATA [~~~]\n", data_all)
    print("\n[~~~] TABLE ALERTS [~~~]\n", alerts_all)

    close_database(db)