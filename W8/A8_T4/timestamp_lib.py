# timestamp_lib.py
from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

# Lisää ISO 8601 -formaatti
_PATTERNS = (
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
    "%Y-%m-%dT%H:%M",  # <-- tämä rivi korjaa ongelman
    "%d.%m.%Y %H:%M",
    "%d.%m.%Y",
)


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    with open(PFilename, "r", encoding="utf-8") as f:
        for raw in f:
            s = raw.strip()
            if not s or s.startswith("#"):
                continue
            dt = None
            for p in _PATTERNS:
                try:
                    dt = datetime.strptime(s, p)
                    break
                except ValueError:
                    pass
            if dt is None:
                raise ValueError(f"Unsupported timestamp format: {s!r}")
            PTimestamps.append(dt)


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    return sum(ts.year == PYear for ts in PTimestamps)


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    name = PMonth.strip().lower()
    for i, m in enumerate(MONTHS, start=1):
        if name == m.lower() or name == m[:3].lower():
            return sum(ts.month == i for ts in PTimestamps)
    raise ValueError(f"Unrecognized month: {PMonth!r}")


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    name = PWeekday.strip().lower()
    for i, w in enumerate(WEEKDAYS):
        if name == w.lower() or name == w[:3].lower():
            return sum(ts.weekday() == i for ts in PTimestamps)
    raise ValueError(f"Unrecognized weekday: {PWeekday!r}")
