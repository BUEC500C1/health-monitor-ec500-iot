from flask import Flask, render_template, request
import sys
from time import sleep
from config import config
sys.path.extend(['./alarm', './data_collector',
                 './data_generation', './database', './scheduler'])
import database as db



app = Flask(__name__)

# Utility Function For UI


def filterOutLastOfEach(data, idxOfName, idxOfVal):
    res = {}
    for i in range(len(data)-1, -1, -1):
        name_of_measurement = data[i][idxOfName]
        val_of_measurement = data[i][idxOfVal]
        res[name_of_measurement] = val_of_measurement
        if(len(res) == 4):
            break
    return res


# Routing Logic
@app.route("/")
def home():
    patient_ids = db.get_all_patient_ids()
    return render_template("home.html", patients=patient_ids)


@app.route('/alerts')
def show_user_alerts():
    user_id = request.args.get('id')

    # No param, null guard
    if user_id is None:
        return "Whoops, go back buddy"

    data = db.get_patient('Alerts', user_id)
    last_dat = filterOutLastOfEach(data, 2, 5)
    return render_template("user_alerts.html", data=data, latest_data=last_dat)


@app.route('/data')
def show_user_data():
    user_id = request.args.get('id')

    # No param, null guard
    if user_id is None:
        return "Whoops, go back buddy"

    data = db.get_patient('Data', user_id)
    last_dat = filterOutLastOfEach(data, 2, 3)
    return render_template("user_data.html", data=data[::-1], latest_data=last_dat)
