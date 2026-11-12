# Day 16: Python Datetime - Interactive Walkthrough

"""
Demonstrates the core mechanics of Python's standard library `datetime` module:
- Getting current date, time, components, and Unix timestamps
- Formatting datetime objects to custom strings using `strftime`
- Parsing raw strings into datetime objects using `strptime`
- Working with `date`, `time`, and `timedelta` duration math
- Timezone awareness (UTC) for backend systems
"""

from datetime import datetime, date, time, timedelta, timezone

def walkthrough():
    print("=" * 70)
    print("1. CURRENT DATETIME & ATTRIBUTES")
    print("=" * 70)
    now = datetime.now()
    print("Full datetime object:", now)
    print("Year:        ", now.year)
    print("Month:       ", now.month)
    print("Day:         ", now.day)
    print("Hour:        ", now.hour)
    print("Minute:      ", now.minute)
    print("Second:      ", now.second)
    print("Microsecond: ", now.microsecond)
    print("POSIX / Unix Timestamp (seconds since 1970-01-01):", now.timestamp())

    print("\n" + "=" * 70)
    print("2. FORMATTING DATES (strftime: String From Time)")
    print("=" * 70)
    # Target format: "%m/%d/%Y, %H:%M:%S"
    formatted_standard = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("Standard US Format:    ", formatted_standard)
    print("Human Readable Format: ", now.strftime("%B %d, %Y - %I:%M %p"))
    print("ISO 8601 Database:     ", now.isoformat())

    print("\n" + "=" * 70)
    print("3. PARSING DATE STRINGS (strptime: String Parse Time)")
    print("=" * 70)
    date_str = "Today is 5 December, 2019"
    # To parse, the format string must match every literal character:
    parsed_date = datetime.strptime(date_str, "Today is %d %B, %Y")
    print("Raw string:   ", repr(date_str))
    print("Parsed object:", repr(parsed_date))
    print("Parsed Year:  ", parsed_date.year)
    print("Parsed Month: ", parsed_date.month)
    print("Parsed Day:   ", parsed_date.day)

    print("\n" + "=" * 70)
    print("4. TIME DIFFERENCES (timedelta)")
    print("=" * 70)
    # Calculate difference to next New Year:
    next_year = now.year + 1
    new_year = datetime(next_year, 1, 1)
    time_to_new_year = new_year - now
    print(f"Time remaining until New Year ({next_year}-01-01):", time_to_new_year)
    print(f"Days: {time_to_new_year.days}, Total Seconds: {time_to_new_year.total_seconds():,.2f}")

    # Calculate time elapsed since the Unix epoch (1 January 1970):
    epoch = datetime(1970, 1, 1)
    time_since_epoch = now - epoch
    print(f"Time elapsed since Unix Epoch (1970-01-01): {time_since_epoch.days:,} days")

    print("\n" + "=" * 70)
    print("5. TIMEZONE AWARENESS (The Backend Standard: UTC)")
    print("=" * 70)
    # Always use timezone.utc in modern Python backend services
    utc_now = datetime.now(timezone.utc)
    print("Aware UTC datetime:", utc_now)
    print("ISO 8601 with UTC offset:", utc_now.isoformat())

    # Simulated Token Expiration Check (e.g. JWT / Session)
    token_lifetime = timedelta(minutes=15)
    token_expires_at = utc_now + token_lifetime
    print("Token created at:   ", utc_now.strftime("%H:%M:%S UTC"))
    print("Token expires at:   ", token_expires_at.strftime("%H:%M:%S UTC"))
    is_expired = datetime.now(timezone.utc) > token_expires_at
    print("Is token expired now?", is_expired)

if __name__ == "__main__":
    walkthrough()

