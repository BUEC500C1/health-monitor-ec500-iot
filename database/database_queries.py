# TODO: Move this parameter to a global config file
# Filename for database
db_name = 'database.db'

# Initialize sqlite3 tables
init_data_table = 'create table if not exists Data (PatientID TEXT, Timestamp TEXT, Type TEXT, Value TEXT)'
init_alerts_table = 'create table if not exists Alerts (PatientID TEXT, Timestamp TEXT, Type TEXT, ThresholdLow TEXT, ThresholdHigh TEXT, Value TEXT)'

# Adding to database
add_data_item = "INSERT INTO Data (PatientID, Timestamp, Type, Value) VALUES (?,?,?,?)"
add_alert_item = "INSERT INTO Alerts (PatientID, Timestamp, Type, ThresholdLow, ThresholdHigh, Value) VALUES (?,?,?,?,?,?)"

# Each function below returns a string SQL command
# get_table returns command to get all entries from a specified table
def get_table(table):
    return f"select * from {table}"

# patient_info returns command to get all info about one patient for a specified table
def patient_info(tablename, patientid):
    return f"SELECT * FROM {tablename} WHERE PatientID={patientid}"

# type_patient_info returns command to get all info about a particular type for a patient
def type_patient_info(tablename, patientid, entrytype):
    return f"SELECT * FROM {tablename} WHERE PatientID={patientid} AND Type='{entrytype}'"

# delete_patient returns a command to delete a patient's data in a particular table
def delete_patient(tablename, patientid):
    return f"DELETE FROM {tablename} WHERE PatientID={patientid}"