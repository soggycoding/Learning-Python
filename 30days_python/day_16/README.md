# 📘 Day 16: Python Datetime & Temporal Engineering

Welcome to **Day 16**! Today focuses on the standard library `datetime` module. In backend engineering, handling dates, times, durations, and timestamps correctly is critical for data integrity—from database record auditing (`created_at`, `updated_at`) to session timeouts, token expiration (JWTs), subscription renewals, and cross-timezone scheduling.

> [!NOTE]
> - Interactive demonstrations and code walkthroughs are in [16_day_python_date_time.py](file:///c:/Users/Jeth/Desktop/Learning-Python/30days_python/day_16/16_day_python_date_time.py).
> - Your Pass 1 exercises are in [exercise_day_16.py](file:///c:/Users/Jeth/Desktop/Learning-Python/30days_python/day_16/exercise_day_16.py).

---

## 1. Core Classes in the `datetime` Module

```text
datetime module
 ├── datetime   # Full timestamp: year, month, day, hour, minute, second, microsecond, tzinfo
 ├── date       # Calendar date: year, month, day (e.g. birthdays, invoice dates)
 ├── time       # Clock time: hour, minute, second, microsecond, tzinfo (no date)
 ├── timedelta  # Duration / difference between two points in time (days, seconds, microseconds)
 ├── timezone   # Timezone offset representation (e.g. timezone.utc)
 └── tzinfo     # Abstract base class for timezones
```

---

## 2. String Formatting (`strftime`) vs Parsing (`strptime`)

A classic mnemonic to remember the difference:
- **`strftime`** = **String From Time** (turns a `datetime` object $\rightarrow$ formatted `str`).
- **`strptime`** = **String Parse Time** (parses a raw `str` $\rightarrow$ `datetime` object).

### Common Format Directives:
| Directive | Meaning | Example |
| :--- | :--- | :--- |
| `%Y` | 4-digit Year | `2026` |
| `%y` | 2-digit Year | `26` |
| `%m` | 2-digit Month (zero-padded) | `01` - `12` |
| `%B` | Full Month Name | `November`, `December` |
| `%b` | Abbreviated Month Name | `Nov`, `Dec` |
| `%d` | Day of Month (zero-padded) | `01` - `31` |
| `%H` | Hour (24-hour clock, `00`-`23`) | `14` |
| `%I` | Hour (12-hour clock, `01`-`12`) | `02` |
| `%p` | AM / PM | `PM` |
| `%M` | Minute (`00`-`59`) | `30` |
| `%S` | Second (`00`-`59`) | `45` |
| `%f` | Microsecond (6 digits) | `123456` |
| `%z` | UTC Offset (`+HHMM` or `-HHMM`) | `+0000`, `-0500` |

---

## 3. Time Arithmetic with `timedelta`

`timedelta` represents a duration, not a point in time:
```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)
two_hours_ago = now - timedelta(hours=2)
token_expiry = now + timedelta(minutes=15)
```

---

## 4. Senior Backend Golden Rule: The UTC Standard

> [!IMPORTANT]
> **Always store and compute in UTC internally; format to local time only at the presentation layer (UI / API client).**
> - In Python 3.11+: Use `datetime.now(timezone.utc)` instead of the deprecated `datetime.utcnow()` (which returned a naive datetime with no timezone awareness).
> - Storing naive local times causes catastrophic bugs during Daylight Saving Time (DST) transitions, cross-region database queries, and server migrations.

