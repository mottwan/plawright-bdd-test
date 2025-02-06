from datetime import datetime, timedelta, date

from dateutil.relativedelta import relativedelta


def time_unit_mapping(unit: str) -> str:
    unit_mapping = {
        "seconds": "seconds",
        "minutes": "minutes",
        "hours": "hours",
        "days": "days",
        "weeks": "weeks",
        "months": "days",  # Approximate a month as 30 days
        "years": "days"  # Approximate a year as 365 days
    }
    # Validate the time unit
    plural_unit = unit + 's' if not unit.endswith('s') else unit
    if plural_unit not in unit_mapping:
        raise ValueError(f"Invalid time unit: {unit}")
    return unit_mapping[plural_unit]


def calculate_time_delta(unit: str, quantity: float):
    quantity = float(quantity)

    if unit.startswith("month"):
        future_date = datetime.today() + timedelta(days=quantity * 30)  # Approximate months
    elif unit.startswith("year"):
        future_date = datetime.today() + timedelta(days=quantity * 365)  # Approximate years
    elif unit.startswith("week"):
        future_date = datetime.today() + timedelta(weeks=quantity)
    elif unit.startswith("day"):
        future_date = datetime.today() + timedelta(days=quantity)
    elif unit.startswith("hour"):
        future_date = datetime.today() + timedelta(hours=quantity)
    elif unit.startswith("minute"):
        future_date = datetime.today() + timedelta(minutes=quantity)
    elif unit.startswith("second"):
        future_date = datetime.today() + timedelta(seconds=quantity)
    else:
        future_date = datetime.today() + timedelta(milliseconds=quantity)

    return {"target_day": future_date.day, "target_month": future_date.strftime("%B"), "target_year": future_date.year,
            "future_date": future_date}


def get_next_month_date(date_string: date):
    return date_string + relativedelta(months=1)


def get_current_year(date_string: date):
    return date_string.year


def get_current_month_name(date_string: date):
    return date_string.strftime("%B")


def to_abbreviated_date_format(date_string: datetime):
    return date_string.strftime("%a, %-d %b")


def to_iso_date_format(date_string: datetime):
    return date_string.strftime("%Y-%m-%d")
