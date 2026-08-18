from datetime import datetime
from typing import Generator, Optional
from .exceptions import InvalidLogLevelError, InvalidDateFormatError

VALID_LEVELS = {'INFO', 'WARN', 'ERROR', 'ALL'}

def filter_entries(
    entries: Generator[dict, None, None],
    level: str = 'ALL',
    from_dt: Optional[datetime] = None,
    to_dt: Optional[datetime] = None
) -> Generator[dict, None, None]:
    if level not in VALID_LEVELS:
        raise InvalidLogLevelError(f'Invalid level: {level}')
    if from_dt and to_dt and from_dt > to_dt:
        raise InvalidDateFormatError('--from date must be before --to date')

    for entry in entries:
        if level != 'ALL' and entry['level'] != level:
            continue
        if from_dt and entry['timestamp'] < from_dt:
            continue
        if to_dt and entry['timestamp'] > to_dt:
            continue
        yield entry