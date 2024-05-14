import logging
import json
import random
import time

# Configuration for logging
LOGGING_CONFIG = {
    'log1.log': logging.INFO,
    'log2.log': logging.INFO,
    'log3.log': logging.ERROR,
    # Add more log file paths and their corresponding log levels as needed
}

# Initialize logger for each log file
loggers = {}
for log_file, log_level in LOGGING_CONFIG.items():
    logger = logging.getLogger(log_file)
    logger.setLevel(log_level)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    loggers[log_file] = logger

# Sample API Integration and logging
def api_call():
    log_file = random.choice(list(loggers.keys()))
    logger = loggers[log_file]
    level = random.choice(['info', 'error', 'success'])
    log_string = "Inside the Search API"
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    log_data = {
        "level": level,
        "log_string": log_string,
        "timestamp": timestamp,
        "metadata": {
            "source": log_file
        }
    }
    logger.log(LOGGING_CONFIG[log_file], json.dumps(log_data))

# Simulate API calls for logging
while True:
    api_call()
    time.sleep(1)  # Simulate API call every second
