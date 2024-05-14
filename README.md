# SDE-1-and-SDE-Intern-Assignment

# Log Query Interface

This project provides a web-based interface for searching through log files based on various criteria. It consists of a Flask application for the user interface and a log ingestor script to simulate log data generation.

## How to Run the Project

### Prerequisites

- Python 3.x installed on your system
- Flask library installed (`pip install Flask`)

### Steps

1. Clone the repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```
    cd log-query-interface
    ```

3. Run the log ingestor script to generate log data:

    ```
    python log.py
    ```

4. Run the Flask application to start the web-based query interface:

    ```
    python UI.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000/` to access the home page of the Log Query Interface.

## System Design

The project consists of two main components:

1. **Log Ingestor**: A Python script (`log.py`) that simulates API calls and logs data into separate log files (`log1.log`, `log2.log`, etc.). The log data is formatted in JSON format and includes fields such as level, log string, timestamp, and source.

2. **Query Interface**: A Flask application (`UI.py`) that provides a web-based interface for searching through log files. It includes routes for the home page, search page, and handling search queries. Users can enter search criteria such as log level, log string, timestamp, and source to retrieve matching log entries.

## Features Implemented

- Log Ingestor:
  - Simulates API calls and logs data into separate log files.
  - Configurable log formatting and logging levels.
  - Error handling for robust log ingestion.

- Query Interface:
  - Web-based interface for searching through logs.
  - Supports filtering based on log level, log string, timestamp, and source.
  - Provides search results in a tabular format.
  - Includes links to navigate back to the home page or perform another search.

## Identified Issues

- **Timestamp Comparison**: The timestamp comparison in the search functionality compares timestamps as strings. This may not work correctly in all cases, especially if the timestamp format varies. Ideally, timestamps should be compared after converting them to datetime objects.

---
