# Day 16: Python Datetime & Temporal Engineering Exercises (Pass 1)

# ==============================================================================
# LEVEL 1: CORE DATETIME EXTRACTION & FORMATTING
# ==============================================================================

# ==============================================================================
# Exercise 1: Extract Date Attributes & Unix Timestamp
# ==============================================================================
# Challenge:
#   Write a function `get_datetime_components(dt=None)` that takes an optional
#   `datetime` object (defaulting to `datetime.now()` if None) and returns a
#   dictionary containing its fundamental temporal attributes:
#     {
#       "year": int,
#       "month": int,
#       "day": int,
#       "hour": int,
#       "minute": int,
#       "second": int,
#       "timestamp": float
#     }
#
# Function signature:
#   def get_datetime_components(dt=None):
#
# Adversarial Test Matrix:
#   1. Standard Case:
#      test_dt = datetime(2026, 11, 12, 16, 30, 45)
#      get_datetime_components(test_dt) ->
#        {"year": 2026, "month": 11, "day": 12, "hour": 16, "minute": 30, "second": 45, "timestamp": test_dt.timestamp()}
#   2. Boundary Case (dt is None):
#      get_datetime_components() -> returns current local datetime components with all 7 keys present.
#   3. Trap Case (Epoch baseline):
#      get_datetime_components(datetime(1970, 1, 1, 0, 0, 0)) ->
#        {"year": 1970, "month": 1, "day": 1, "hour": 0, "minute": 0, "second": 0, "timestamp": ...}
# ==============================================================================

# Write your Exercise 1 solution below:



# ==============================================================================
# Exercise 2: Format Datetime with strftime
# ==============================================================================
# Challenge:
#   Write a formatting function `format_datetime_custom(dt=None)` that accepts an
#   optional `datetime` object (defaulting to `datetime.now()`) and returns a
#   formatted string strictly matching the pattern:
#     "MM/DD/YYYY, HH:MM:SS" (e.g. "11/12/2026, 16:05:30")
#   - Month, day, hour, minute, second must be zero-padded to 2 digits.
#   - Year must be 4 digits.
#   - Hours must be 24-hour format (00-23).
#
# Function signature:
#   def format_datetime_custom(dt=None):
#
# Adversarial Test Matrix:
#   1. Standard Case:
#      format_datetime_custom(datetime(2026, 11, 12, 16, 5, 30)) -> "11/12/2026, 16:05:30"
#   2. Boundary Case (Single digit day, month, hour, second - zero-padding check):
#      format_datetime_custom(datetime(2025, 3, 5, 4, 7, 9)) -> "03/05/2025, 04:07:09"
#   3. Trap Case (Midnight boundary):
#      format_datetime_custom(datetime(2026, 1, 1, 0, 0, 0)) -> "01/01/2026, 00:00:00"
# ==============================================================================

# Write your Exercise 2 solution below:



# ==============================================================================
# Exercise 3: Parse Date String with strptime
# ==============================================================================
# Challenge:
#   Write a parser function `parse_human_date(date_str)` that converts the human
#   date string `"Today is 5 December, 2019"` into a `datetime` object.
#   - The function must parse strings adhering to `"Today is <day> <Full Month>, <Year>"`.
#   - If the string does not match the format or is invalid, raise a `ValueError`
#     with the message `"Invalid date format"`.
#
# Function signature:
#   def parse_human_date(date_str):
#
# Adversarial Test Matrix:
#   1. Standard Case:
#      parse_human_date("Today is 5 December, 2019") -> datetime(2019, 12, 5, 0, 0)
#   2. Boundary Case (Double-digit day):
#      parse_human_date("Today is 25 December, 2024") -> datetime(2024, 12, 25, 0, 0)
#   3. Trap Case (Malformed prefix or date):
#      parse_human_date("Date: 5 December, 2019") -> raises ValueError("Invalid date format")
# ==============================================================================

# Write your Exercise 3 solution below:



# ==============================================================================
# LEVEL 2: TEMPORAL ARITHMETIC & DURATION MATH
# ==============================================================================

# ==============================================================================
# Exercise 4: Duration Calculations (Time Deltas)
# ==============================================================================
# Challenge:
#   Implement two time-delta calculation functions:
#   1. `time_until_new_year(from_dt=None)`:
#      Calculates the duration between `from_dt` (defaulting to `datetime.now()`) and
#      the next upcoming New Year (`January 1, 00:00:00` of `from_dt.year + 1`).
#      Returns a `timedelta` object.
#   2. `time_since_epoch(from_dt=None)`:
#      Calculates the duration between the Unix epoch (`January 1, 1970, 00:00:00`)
#      and `from_dt` (defaulting to `datetime.now()`).
#      Returns total days as an integer.
#
# Function signatures:
#   def time_until_new_year(from_dt=None):
#   def time_since_epoch(from_dt=None):
#
# Adversarial Test Matrix:
#   1. Standard Case (New Year calculation):
#      test_dt = datetime(2026, 12, 31, 23, 0, 0)
#      time_until_new_year(test_dt) -> timedelta(hours=1) (or total_seconds() == 3600.0)
#   2. Boundary Case (New Year's Eve midnight edge):
#      test_dt = datetime(2026, 1, 1, 0, 0, 0)
#      time_until_new_year(test_dt).days -> 365 (since 2026 is not a leap year)
#   3. Epoch Case:
#      time_since_epoch(datetime(1970, 1, 11, 0, 0, 0)) -> 10
# ==============================================================================

# Write your Exercise 4 solution below:



# ==============================================================================
# LEVEL 3: BACKEND PRODUCTION PATTERNS
# ==============================================================================

# ==============================================================================
# Exercise 5: Token Expiration Checker (UTC & Timezone Awareness)
# ==============================================================================
# Challenge:
#   In web APIs (e.g. JWT authentication / password reset links), tokens carry
#   an issue timestamp and a Time-To-Live (TTL).
#
#   Write a validator function `is_token_expired(issued_at_iso, ttl_seconds, current_time=None)`:
#   - `issued_at_iso`: An ISO 8601 formatted timestamp string (e.g. `"2026-11-12T10:00:00Z"` or `"2026-11-12T10:00:00+00:00"`).
#   - `ttl_seconds`: Duration in seconds the token remains valid.
#   - `current_time`: Optional timezone-aware `datetime` representing current time
#     (defaults to `datetime.now(timezone.utc)`).
#   - Returns `True` if `current_time >= issued_at + timedelta(seconds=ttl_seconds)`.
#   - Returns `False` if token is still within validity window.
#   - If `issued_at_iso` is malformed or invalid ISO format, gracefully return `True`
#     (treat bad tokens as expired).
#
# Function signature:
#   def is_token_expired(issued_at_iso, ttl_seconds, current_time=None):
#
# Adversarial Test Matrix:
#   1. Standard Case (Valid active token):
#      now = datetime(2026, 11, 12, 10, 5, 0, tzinfo=timezone.utc)
#      is_token_expired("2026-11-12T10:00:00Z", ttl_seconds=900, current_time=now) -> False (issued 5m ago, TTL 15m)
#   2. Boundary Case (Expired token):
#      now = datetime(2026, 11, 12, 10, 20, 0, tzinfo=timezone.utc)
#      is_token_expired("2026-11-12T10:00:00Z", ttl_seconds=900, current_time=now) -> True (issued 20m ago, TTL 15m)
#   3. Trap Case (Exact expiration boundary):
#      now = datetime(2026, 11, 12, 10, 15, 0, tzinfo=timezone.utc)
#      is_token_expired("2026-11-12T10:00:00Z", ttl_seconds=900, current_time=now) -> True
#   4. Trap Case (Malformed timestamp string):
#      is_token_expired("invalid-date-string", ttl_seconds=900) -> True
# ==============================================================================

# Write your Exercise 5 solution below:



# ==============================================================================
# Exercise 6: Age & Next Birthday Countdown
# ==============================================================================
# Challenge:
#   Implement a user profile helper `calculate_birthday_stats(birth_date_str, reference_date=None)`:
#   - `birth_date_str`: String formatted as `"YYYY-MM-DD"`.
#   - `reference_date`: Optional `date` object (defaults to `date.today()`).
#   - Returns a dictionary:
#     {
#       "age": int,                    # Completed full years lived as of reference_date
#       "days_until_birthday": int     # Number of days until next birthday (0 if today is birthday!)
#     }
#   - If `birth_date_str` is invalid date format or represents a future date,
#     raise `ValueError("Invalid birth date")`.
#
# Function signature:
#   def calculate_birthday_stats(birth_date_str, reference_date=None):
#
# Adversarial Test Matrix:
#   1. Standard Case (Birthday has not occurred yet this year):
#      calculate_birthday_stats("2000-12-25", reference_date=date(2026, 11, 12)) ->
#        {"age": 25, "days_until_birthday": 43}
#   2. Boundary Case (Birthday has already passed this year):
#      calculate_birthday_stats("2000-01-15", reference_date=date(2026, 11, 12)) ->
#        {"age": 26, "days_until_birthday": 64}  # next birthday is Jan 15, 2027
#   3. Trap Case (Today IS birthday!):
#      calculate_birthday_stats("2000-11-12", reference_date=date(2026, 11, 12)) ->
#        {"age": 26, "days_until_birthday": 0}
#   4. Trap Case (Future date):
#      calculate_birthday_stats("2030-01-01", reference_date=date(2026, 11, 12)) ->
#        raises ValueError("Invalid birth date")
# ==============================================================================

# Write your Exercise 6 solution below:

