# Log-Analyzer CLI 🚀

A modular, memory-efficient Python command-line interface (CLI) tool designed to parse, filter, and summarize server log files.

---

## 📌 Features

- **Memory-Efficient Streaming**: Uses **Python Generators** (`parser.py`) to stream large log files line-by-line without loading entire datasets into memory.
- **Dynamic Log Filtering**: Filter log entries dynamically by severity level (`INFO`, `WARNING`, `ERROR`) or custom date criteria (`filters.py`).
- **Defensive Error Handling**: Uses custom exceptions (`exceptions.py`) to handle malformed lines and missing files gracefully without crashing.
- **Summary Reporting**: Formats and outputs structured, readable analytical reports (`report.py`).
- **Clean Modular Architecture**: Organized as a standard Python package (`log_analyzer/`) with a simple entry point (`main.py`).

---

## 📂 Project Structure

```text
.
├── log_analyzer/          # Core Python package
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # CLI argument parsing logic
│   ├── exceptions.py      # Custom exception definitions
│   ├── filters.py         # Log filtering logic
│   ├── parser.py          # Generator-based log parsing & timing logic
│   └── report.py          # Summary report generation & formatting
├── main.py                # Main application entry point
├── sample.log             # Sample log file for testing
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

🛠️ Setup & Installation
Prerequisites: Ensure Python 3.8+ is installed on your system.

Clone the Repository:
git clone [https://github.com/your-username/log-analyzer-cli.git](https://github.com/your-username/log-analyzer-cli.git)
cd log-analyzer-cli

Install Dependencies (Optional):
pip install -r requirements.txt

🚀 Usage Guide
Execute commands from the project root folder using main.py:

1. Basic Analysis
Summarize all entries in a log file:
python main.py --file sample.log

2. Filter by Severity Level
Isolate logs by log level (INFO, WARNING, or ERROR):
python main.py --file sample.log --level ERROR

3. Using Short Flags
python main.py -f sample.log -l WARNING


📄 Expected Log Format
The parser processes log entries structured in the standard format:

Plaintext
YYYY-MM-DD HH:MM:SS [LEVEL] Log message content
Example (sample.log):

Plaintext
2026-08-01 10:15:30 [INFO] System booted successfully.
2026-08-01 10:16:05 [WARNING] High memory usage detected.
2026-08-01 10:17:12 [ERROR] Failed to connect to database model.
2026-08-01 10:18:00 [ERROR] Network connection dropped.
2026-08-01 10:19:45 [INFO] User session ended.


⚙️ Package Architecture Overview
main.py: Root entry point that initializes and executes the CLI pipeline.

log_analyzer/cli.py: Handles command-line arguments using Python's standard argparse library.

log_analyzer/parser.py: Implements line-by-line streaming using Python generators for optimal memory usage.

log_analyzer/filters.py: Contains filtering logic to select entries by severity level or other conditions.

log_analyzer/report.py: Formats aggregated data and displays output summaries.

log_analyzer/exceptions.py: Defines custom exception classes like MalformedLogLineError and LogFileNotFoundError.