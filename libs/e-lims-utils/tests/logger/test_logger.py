"""e-lims-utils tests files."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Generator

import pytest

from e_lims_utils.files.files import FileProperties, FileSuffix
from e_lims_utils.files.timestamp import Timestamp
from e_lims_utils.logger.logger import Logger, LoggerLevel


@pytest.fixture()
def fx_logger() -> Generator[Logger, None, None]:
    """Pytest fixture for the Logger class.

    Returns:
        Logger: A Logger object.
    """
    file = FileProperties(
            name="test",
            suffix=FileSuffix.LOG,
            path=Path.cwd(),
            timestamp=Timestamp(datetime.now(tz=timezone.utc)),
    )
    logger = Logger(file=file, sys_level=LoggerLevel.TRACE, file_level=LoggerLevel.TRACE, backtrace=True, diagnose=True)
    yield logger
    for handler_id in logger._logger._core.handlers:
        logger.remove(handler_id)
    file.file_path.unlink()


def test_logger_message(fx_logger: Logger) -> None:
    """Test the file_name method with a timestamp.

    Args:
        fx_logger (Logger): A Logger object.
    """
    fx_logger.trace("test trace message.")
    fx_logger.debug("test debug message.")
    fx_logger.info("test info message.")
    fx_logger.success("test success message.")
    fx_logger.warning("test warning message.")
    fx_logger.error("test error message.")
    fx_logger.critical("test critical message.")

    with fx_logger._file.file_path.open("r") as file:
        lines = file.readlines()
        assert "test trace message." in lines[0]
        assert "test debug message." in lines[1]
        assert "test info message." in lines[2]
        assert "test success message." in lines[3]
        assert "test warning message." in lines[4]
        assert "test error message." in lines[5]
        assert "test critical message." in lines[6]
        