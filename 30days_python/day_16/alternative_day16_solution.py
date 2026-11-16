# Day 16: Python Datetime & Temporal Engineering - Alternative Solutions (Pass 2)
from warnings import catch_warnings
import re
from datetime import datetime, date, time, timedelta, timezone
# ==============================================================================
# BATCH 1: CORE DATETIME EXTRACTION & FORMATTING (Exercises 1, 2, and 3)
# ==============================================================================

# ==============================================================================
# Exercise 1: Extract Date Attributes (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Using dt.timetuple() / struct_time):
#      Instead of reading `.year`, `.month`, `.day` individually, explore Python's
#      `dt.timetuple()`. It returns a 9-element `time.struct_time` named tuple:
#      `tm = dt.timetuple()` -> `tm.tm_year`, `tm.tm_mon`, `tm.tm_mday`, `tm.tm_hour`, etc.
#    - Option B (Dictionary Comprehension with getattr):
#      Use a list of attribute names `attrs = ["year", "month", "day", "hour", "minute", "second"]`
#      and construct the dictionary dynamically using a dictionary comprehension and `getattr(dt, attr)`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `dt.timetuple()`: Bridges Python's high-level `datetime` objects with C-level
#      time functions (`time.mktime()`). Useful when interacting with low-level OS APIs.
#    - Dynamic `getattr`: Keeps code DRY if extracting many attributes, but incurs small
#      dynamic lookup overhead compared to direct C-level attribute access (`dt.year`).
#
# Target Output:
#   get_datetime_components(datetime(2026, 11, 12, 16, 30, 45)) ->
#     {"year": 2026, "month": 11, "day": 12, "hour": 16, "minute": 30, "second": 45, "timestamp": 1794472245.0}
# ==============================================================================
'''
# Write your Exercise 1 (Pass 2) solution below:
def get_datetime_components(dt=None):
    if dt is None:
        dt = datetime.now()
    tm = dt.timetuple()
    return {"year": tm.tm_year, "month": tm.tm_mon, "day" : tm.tm_mday, "hour": tm.tm_hour, "minute": tm.tm_min, "second" : tm.tm_sec, "timestamp" : float(dt.timestamp())}
print(get_datetime_components())
'''
# ==============================================================================
# Exercise 2: Format Datetime (Pass 2: Inline f-string Formatting)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Inline f-string Format Specifiers):
#      In Python 3.6+, f-strings directly support `strftime` format directives
#      inside the replacement field without calling `.strftime()`!
#      Syntax: `f"{dt:%m/%d/%Y, %H:%M:%S}"`
#    - Option B (Manual Pad Formatting via format() / str.zfill()):
#      Explore zero-padding manually using integer formatting:
#      `f"{dt.month:02d}/{dt.day:02d}/{dt.year:04d}, {dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"`
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Inline f-string specifiers (`f"{dt:%m/%d/%Y}"`):
#      - Evaluated at bytecode compile-time; calls C-level `__format__` method directly.
#      - Cleaner and more readable when embedding dates inside larger strings or log statements.
#    - Manual `:02d` formatting:
#      - Shows how Python pads integers with leading zeroes (`:02d` means 2 digits, zero-padded).
#
# Target Output:
#   format_datetime_custom(datetime(2026, 11, 12, 16, 5, 30)) -> "11/12/2026, 16:05:30"
#   format_datetime_custom(datetime(2025, 3, 5, 4, 7, 9))      -> "03/05/2025, 04:07:09"
# ==============================================================================
'''
# Write your Exercise 2 (Pass 2) solution below:
def format_datetime_custom(dt=None):
    if dt is None:
        dt = datetime.now()
    return f"{dt:%m/%d/%Y, %H:%M:%S}"
print(format_datetime_custom(datetime(2026, 11, 12, 16, 5, 30)))
'''
'''
def format_datetime_custom(dt=None):
    if dt is None:
        dt = datetime.now()
    return f"{dt.month:02d}/{dt.day:02d}/{dt.year:04d}, {dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
print(format_datetime_custom())
'''
# ==============================================================================
# Exercise 3: Parse Date String (Pass 2: Regex Extraction & Resilience)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Regular Expression Extraction + Direct Constructor):
#      Instead of rigid `strptime`, use `re.search` with named groups to extract
#      the day, month, and year from human text:
#      `r"Today is (?P<day>\d{1,2}) (?P<month>[A-Za-z]+), (?P<year>\d{4})"`
#      Convert month name to month number (via a dict or `datetime.strptime(month, "%B").month`),
#      then directly instantiate `datetime(int(year), int(month_num), int(day))`.
#    - Option B (Handling Leading/Trailing Whitespace & Case Insensitivity):
#      Clean the string with `.strip()` before parsing to make `strptime` resilient
#      to dirty user input.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `strptime` vs Regular Expressions:
#      - `strptime`: Strict, validates calendar logic automatically (e.g. rejects "31 February"),
#        but breaks on any minor format difference (extra space, different word order).
#      - Regex: Flexible for scraping or extracting dates embedded within unstructured sentences,
#        but requires manual calendar validation.
#
# Target Output:
#   parse_human_date("Today is 5 December, 2019")  -> datetime(2019, 12, 5, 0, 0)
#   parse_human_date("Today is 25 December, 2024") -> datetime(2024, 12, 25, 0, 0)
#   parse_human_date("Invalid string")             -> raises ValueError("Invalid date format")
# ==============================================================================

# Write your Exercise 3 (Pass 2) solution below:

def parse_human_date(date_str):
    try:
        pattern = r"Today is (?P<day>\d{1,2}) (?P<month>[A-Za-z]+), (?P<year>\d{4})"
        match = re.search(pattern, date_str)
        if not match:
            raise ValueError("Invalid date format")
        day = int(match.group("day"))
        year = int(match.group("year"))
        month_str = match.group("month")
        month_num = datetime.strptime(month_str, "%B").month
        return datetime(year, month_num, day)
    except ValueError:
        raise ValueError("Invalid date format")
print(parse_human_date("Invalid date format"))