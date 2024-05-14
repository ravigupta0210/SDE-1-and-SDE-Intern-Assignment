from flask import Flask, render_template, request
import os
import glob
import json
import re

app = Flask(__name__)

import datetime

# Function to search logs
def search_logs(level=None, log_string=None, timestamp=None, source=None):
    logs = []
    log_files = glob.glob("*.log")
    for log_file in log_files:
        with open(log_file, 'r') as f:
            for line in f:
                log = json.loads(line)
                log_timestamp = datetime.datetime.strptime(log['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
                if (not level or log['level'] == level) and \
                   (not log_string or re.search(log_string, log['log_string'])) and \
                   (not timestamp or log_timestamp == timestamp) and \
                   (not source or log['metadata']['source'] == source):
                    logs.append(log)
    return logs


# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')


# Route for handling search queries
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        level = request.form['level']
        log_string = request.form['log_string']
        timestamp = request.form['timestamp']
        source = request.form['source']
        logs = search_logs(level, log_string, timestamp, source)
        return render_template('results.html', logs=logs)
    return render_template('search.html')




if __name__ == '__main__':
    app.run(debug=True)

