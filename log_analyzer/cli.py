import argparse
import functools
import os
import sys
import time

from datetime import datetime

from .parser import read_log_file
from .filters import filter_entries
from .report import format_report

from .exceptions import (
    LogAnalyzerError,
    InvalidDateFormatError
)


def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"\nExecution Time : "
            f"{end-start:.4f} seconds"
        )

        return result

    return wrapper


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        required=True
    )

    parser.add_argument(
        "--level",
        default="ALL",
        choices=[
            "ALL",
            "INFO",
            "WARN",
            "ERROR"
        ]
    )

    parser.add_argument(
        "--from",
        dest="from_dt"
    )

    parser.add_argument(
        "--to",
        dest="to_dt"
    )

    parser.add_argument(
        "--format",
        dest="fmt",
        default="text",
        choices=[
            "text",
            "json"
        ]
    )

    return parser.parse_args()


def validate_args(args):

    if os.path.isdir(args.file):
        raise LogAnalyzerError(
            "Given path is a directory."
        )

    date_format = "%Y-%m-%d %H:%M:%S"

    if args.from_dt:
        try:
            args.from_dt = datetime.strptime(
                args.from_dt,
                date_format
            )
        except ValueError:
            raise InvalidDateFormatError(
                "Invalid From Date"
            )

    if args.to_dt:
        try:
            args.to_dt = datetime.strptime(
                args.to_dt,
                date_format
            )
        except ValueError:
            raise InvalidDateFormatError(
                "Invalid To Date"
            )


@timer
def run_analysis(args):

    entries = read_log_file(
        args.file
    )

    filtered = filter_entries(
        entries,
        args.level,
        args.from_dt,
        args.to_dt
    )

    report = format_report(
        filtered,
        args.fmt
    )

    print(report)


def main():

    args = parse_args()

    try:

        validate_args(args)

        run_analysis(args)

    except LogAnalyzerError as error:

        print(
            f"Error : {error}",
            file=sys.stderr
        )

        sys.exit(1)


if __name__ == "__main__":
    main()