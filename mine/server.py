import os
from mine.database import CSVDataset,Database
from flask import Flask
app = Flask(__name__)

@app.route("/")
def init():
    return "Hello World!"

@app.route("/datasets")
def datasets():
    db = Database(os.environ['OPENMINED_DB_LOC'])
    return db.to_json()
