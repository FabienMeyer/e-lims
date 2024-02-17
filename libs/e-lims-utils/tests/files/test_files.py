"""e-lims-utils tests files."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from e_lims_utils.files.files import FileProperties, FileSuffix
from e_lims_utils.files.timestamp import Timestamp


@pytest.fixture()
def fx_file_properties_with_timestamp() -> tuple[datetime, FileProperties]:
    """Pytest fixture for the FileProperties class.

    Returns:
        tuple[datetime, FileProperties]: A tuple containing the current datetime and a FileProperties object.
    """
    timestamp = Timestamp(datetime.now(tz=timezone.utc))
    return timestamp, FileProperties(
        name="test",
        suffix=FileSuffix.LOG,
        path=Path.cwd(),
        timestamp=timestamp,
    )


@pytest.fixture()
def fx_file_properties_without_timestamp() -> FileProperties:
    """Pytest fixture for the FileProperties class.

    Returns:
        FileProperties: A FileProperties object.
    """
    return FileProperties(
        name="test",
        suffix=FileSuffix.LOG,
        path=Path.cwd(),
        timestamp=None,
    )


def test_file_name_with_timestamp(fx_file_properties_with_timestamp: tuple[datetime, FileProperties]) -> None:
    """Test the file_name method with a timestamp.

    Args:
        fx_file_properties_with_timestamp (tuple[datetime, FileProperties]): A tuple containing the current datetime and a FileProperties object.
    """
    timestamp, file_properties = fx_file_properties_with_timestamp
    assert file_properties.file_name == f"test_{timestamp.stamp}.log"  # nosec B101


def test_file_name_without_timestamp(fx_file_properties_without_timestamp: FileProperties) -> None:
    """Test the file_name method without a timestamp.

    Args:
        fx_file_properties_without_timestamp (FileProperties): A tuple containing the current datetime and a FileProperties object.
    """
    file_properties = fx_file_properties_without_timestamp
    assert file_properties.file_name == "test.log"  # nosec B101


def test_create_file(fx_file_properties_with_timestamp: tuple[datetime, FileProperties]) -> None:
    """Test the file_path method.

    Args:
        fx_file_properties_with_timestamp (tuple[datetime, FileProperties]): A tuple containing the current datetime and a FileProperties object.
    """
    timestamp, file_properties = fx_file_properties_with_timestamp
    assert file_properties.file_path == Path.cwd() / f"test_{timestamp.stamp}.log"  # nosec B101
