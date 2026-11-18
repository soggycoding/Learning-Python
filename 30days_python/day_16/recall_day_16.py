# Day 16: Python Datetime & Temporal Engineering - Pure Recall Challenges (Pass 3)

# ==============================================================================
# BATCH 1: RECALL CHALLENGES (Exercises 1, 2, and 3)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_16.py` or `alternative_day16_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 1: Component & Timestamp Extraction
#   Function:
#     get_datetime_components(dt=None)
#   Input:
#     Optional `datetime` object (defaults to current time if None).
#   Expected Output:
#     Dictionary containing 7 keys:
#       {"year": int, "month": int, "day": int, "hour": int, "minute": int, "second": int, "timestamp": float}
#   Constraints:
#     - If dt is None, must default to datetime.now().
#     - Must return all 7 keys with correct numeric types.
#   Adversarial Test Matrix:
#     1. Standard Case:
#        get_datetime_components(datetime(2026, 11, 12, 16, 30, 45)) ->
#          {"year": 2026, "month": 11, "day": 12, "hour": 16, "minute": 30, "second": 45, "timestamp": ...}
#     2. Boundary Case (dt is None):
#        get_datetime_components() -> returns all 7 keys populated with current local time.
#     3. Trap Case (Zero-value clock):
#        get_datetime_components(datetime(2025, 1, 1, 0, 0, 0)) -> hour, minute, second must be 0.
from multiprocessing.sharedctypes import Value
from datetime import datetime, date, time, timedelta, timezone
from warnings import catch_warnings
import re
'''
def get_datetime_components(dt=None):
    if dt is None:
        dt = datetime.now()
    return {"year": dt.year, "month": dt.month, "day": dt.day, "hour": dt.hour, "minute": dt.minute, "second": dt.second, "timestamp": dt.timestamp()}
print(get_datetime_components(datetime(2025, 1, 1, 0, 0, 0)))
'''
# Recall Prompt 2: Custom Datetime Formatting
#   Function:
#     format_datetime_custom(dt=None)
#   Input:
#     Optional `datetime` object (defaults to current time if None).
#   Expected Output:
#     Formatted string matching pattern: "MM/DD/YYYY, HH:MM:SS"
#   Constraints:
#     - Month, day, hour, minute, second must be zero-padded 2-digit strings.
#     - Year must be 4 digits.
#     - 24-hour clock format (00-23).
#   Adversarial Test Matrix:
#     1. Standard Case:
#        format_datetime_custom(datetime(2026, 11, 12, 16, 5, 30)) -> "11/12/2026, 16:05:30"
#     2. Boundary Case (Single digits zero-padding):
#        format_datetime_custom(datetime(2025, 3, 5, 4, 7, 9)) -> "03/05/2025, 04:07:09"
#     3. Trap Case (Midnight boundary):
#        format_datetime_custom(datetime(2026, 1, 1, 0, 0, 0)) -> "01/01/2026, 00:00:00"
'''
def format_datetime_custom(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%m/%d/%Y, %H:%M:%S")
print(format_datetime_custom(datetime(2026, 11, 12, 16, 5, 30)))
'''
# Recall Prompt 3: Human Date Sentence Parser
#   Function:
#     parse_human_date(date_str)
#   Input:
#     String formatted as "Today is <day> <Full Month>, <Year>"
#   Expected Output:
#     `datetime` object representing the parsed calendar date.
#   Constraints:
#     - Must parse full month names and dynamic days.
#     - If date_str is invalid, malformed, or doesn't match the format,
#       strictly raise ValueError("Invalid date format").
#   Adversarial Test Matrix:
#     1. Standard Case:
#        parse_human_date("Today is 5 December, 2019") -> datetime(2019, 12, 5, 0, 0)
#     2. Boundary Case (Double-digit day):
#        parse_human_date("Today is 25 December, 2024") -> datetime(2024, 12, 25, 0, 0)
#     3. Trap Case (Malformed text):
#        parse_human_date("Date: 5 December, 2019") -> raises ValueError("Invalid date format")
# ==============================================================================
'''
def parse_human_date(date_str):
    try:
        parsed = datetime.strptime(date_str, "Today is %d %B, %Y")
        return parsed
    except ValueError:
        raise ValueError("Invalid date format")
print(parse_human_date("Date: 5 December, 2019"))
'''