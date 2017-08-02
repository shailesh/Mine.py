from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from mine.database import CSVDataset,Database
from flask import Flask
import os
import time
import atexit

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

@app.route("/")
def init():
    return "Hello World!"

@app.route("/datasets")
def datasets():
    db = Database(os.environ['OPENMINED_DB_LOC'])
    return db.to_json()

def query_sonar_for_training_opportunities():
    print("Querying Sonar for Training Opportunities")

scheduler.add_job(
    func=print_date_time,
    trigger=IntervalTrigger(seconds=5),
    id='check_for_training_opportunities',
    name='Check OpenMined:Sonar for available models to train.',
    replace_existing=True)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
