"""e-lims-utils tests timestamp."""
from __future__ import annotations

from datetime import datetime, timezone

import pytest

from e_lims_utils.files.timestamp import Timestamp


@pytest.fixture()
def fixture_datetime() -> tuple[datetime, Timestamp]:
    """Fixture that creates a tuple with the current datetime and a Timestamp object.

    Returns:
        tuple[datetime, list[Timestamp]]: A tuple containing the current datetime and a Timestamp object.
    """
    now = datetime.now(tz=timezone.utc)
    return now, Timestamp(now=now)


def test_timestamp_year(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the year property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.year == now.year  # nosec B101


def test_timestamp_month(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the month property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.month == now.month  # nosec B101


def test_timestamp_day(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the day property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.day == now.day  # nosec B101


def test_timestamp_date(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the date property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.date == f"{now.year}-{now.month}-{now.day}"  # nosec B101


def test_timestamp_hour(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the hour property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.hour == now.hour  # nosec B101


def test_timestamp_minute(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the minute property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.minute == now.minute  # nosec B101


def test_timestamp_second(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the second property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.second == now.second  # nosec B101


def test_timestamp_microsecond(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the microsecond property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.microsecond == now.microsecond  # nosec B101


def test_timestamp_time(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the time property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.time == f"{now.hour}-{now.minute}-{now.second}"  # nosec B101


def test_timestamp_stamp(fixture_datetime: tuple[datetime, Timestamp]) -> None:
    """Test that the stamp property of the Timestamp object is correct.

    Args:
        fixture_datetime (tuple[datetime, list[Timestamp]]): A tuple containing the current datetime and a Timestamp object.
    """
    now, timestamp = fixture_datetime
    assert timestamp.stamp == f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}"  # nosec B101
