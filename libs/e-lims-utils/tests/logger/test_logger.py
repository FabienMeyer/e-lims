"""e-lims-utils tests files."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Generator

import pytest

from src.files.files import FileProperties, FileSuffix
from src.files.timestamp import Timestamp
from src.logger.logger import Logger


@pytest.fixture()
def fx_logger() -> Generator[Logger, None, None]:
    """Pytest fixture for the Logger class.

    Returns:
        Logger: A Logger object.
    """
    logger = Logger(
        FileProperties(
            name="test",
            suffix=FileSuffix.LOG,
            path=Path.cwd(),
            timestamp=Timestamp(datetime.now(tz=timezone.utc)),
        ),
    )
    yield logger
    # TODO(Fabien Meyer): Find a way to delete temporary files created by the logger.
    logger.logger.success("test success message.")


def test_logger_message(fx_logger: Logger) -> None:
    """Test the file_name method with a timestamp.

    Args:
        fx_logger (Logger): A Logger object.
    """
    fx_logger.logger.trace("test trace message.")
    fx_logger.logger.debug("test debug message.")
    fx_logger.logger.info("test info message.")
    fx_logger.logger.success("test success message.")
    fx_logger.logger.warning("test warning message.")
    fx_logger.logger.error("test error message.")
    fx_logger.logger.critical("test critical message.")
