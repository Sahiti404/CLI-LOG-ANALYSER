class LogAnalyzerError(Exception):
    """Base exception for all Log Analyzer errors."""
    pass


class InvalidLogLevelError(LogAnalyzerError):
    """Raised when an invalid log level is provided."""
    pass


class InvalidDateFormatError(LogAnalyzerError):
    """Raised when the date format is invalid."""
    pass


class MalformedLineError(LogAnalyzerError):
    """Raised when a log line cannot be parsed."""
    pass