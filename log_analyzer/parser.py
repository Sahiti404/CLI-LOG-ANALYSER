from datetime import datetime
from typing import Generator
from .exceptions import MalformedLineError, LogAnalyzerError
import os

LOG_LEVELS = {'INFO', 'WARN', 'ERROR'}

def read_log_file(
    path: str,
    max_errors: int = 10
) -> Generator[dict, None, None]:
    """
    Lazily reads and yields parsed log entries from a file.
    Raises LogAnalyzerError if the file does not exist.
    Raises MalformedLineError abort if error threshold exceeded.
    """
    if not os.path.isfile(path):
        raise LogAnalyzerError(f'File not found: {path}')

    error_count = 0

    with open(path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue  # skip blank lines
            try:
                yield parse_line(line)
            except MalformedLineError as e:
                error_count += 1
                if error_count > max_errors:
                    raise MalformedLineError(
                        f'Too many malformed lines (>{max_errors}). Aborting.'
                    ) from e

def parse_line(line: str) -> dict:
    """
    Parses a single log line into a dict with keys:
    timestamp (datetime), level (str), message (str).
    """
    parts = line.split(' ', 3)  # split on first 3 spaces
    if len(parts) < 4:
        raise MalformedLineError(f'Cannot parse line: {line!r}')

    date_str, time_str, level, message = parts
    if level not in LOG_LEVELS:
        raise MalformedLineError(f'Unknown log level: {level!r}')

    try:
        timestamp = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise MalformedLineError(f'Invalid timestamp: {date_str} {time_str}')

    return {
        'timestamp': timestamp,
        'level': level.strip(),
        'message': message.strip()
    }