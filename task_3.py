"""
✔️CSV.py File Creation and use it as Parent Class for task_one and task_two.
"""

from flask import Flask
import csv

app = Flask(__name__)

filename = "F:\python\employees.csv"

@app.route("/read1")
def read_entire_csv(cls):
    with open(cls.filename, "r") as foo:
        return foo.readlines()

@app.route("/read2")
def read_csv_line_by_line(cls):
    with open(cls.filename) as bar:
        yield bar.readline()