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
    logger = Logger(file=file, level=LoggerLevel.TRACE, backtrace=True, diagnose=True)
    yield logger
    logger._logger.remove(list(logger._logger._core.handlers.keys())[-1])  # noqa: SLF001
    file.file_path.unlink()


def test_logger_message(fx_logger: Logger) -> None:
    """Test the file_name method with a timestamp.

    Args:
        fx_logger (Logger): A Logger object.
    """
    write_lines = [
        "test trace message.",
        "test debug message.",
        "test info message.",
        "test success message.",
        "test warning message.",
        "test error message.",
        "test critical message.",
    ]
    fx_logger.trace(write_lines[0])
    fx_logger.debug(write_lines[1])
    fx_logger.info(write_lines[2])
    fx_logger.success(write_lines[3])
    fx_logger.warning(write_lines[4])
    fx_logger.error(write_lines[5])
    fx_logger.critical(write_lines[6])

    with fx_logger.file.file_path.open("r") as file:
        lines = file.readlines()
        assert len(lines) == len(write_lines)  # nosec B101
        assert "test trace message." in lines[0]  # nosec B101
        assert LoggerLevel.TRACE.name in lines[0]  # nosec B101
        assert "test debug message." in lines[1]  # nosec B101
        assert LoggerLevel.DEBUG.name in lines[1]  # nosec B101
        assert "test info message." in lines[2]  # nosec B101
        assert LoggerLevel.INFO.name in lines[2]  # nosec B101
        assert "test success message." in lines[3]  # nosec B101
        assert LoggerLevel.SUCCESS.name in lines[3]  # nosec B101
        assert "test warning message." in lines[4]  # nosec B101
        assert LoggerLevel.WARNING.name in lines[4]  # nosec B101
        assert "test error message." in lines[5]  # nosec B101
        assert LoggerLevel.ERROR.name in lines[5]  # nosec B101
        assert "test critical message." in lines[6]  # nosec B101
        assert LoggerLevel.CRITICAL.name in lines[6]  # nosec B101


def test_set_file_level(fx_logger: Logger) -> None:
    """Test the set_file_level method.

    Args:
        fx_logger (Logger): A Logger object.
    """
    write_lines = [
        "test trace message.",
        "test debug message.",
        "test info message.",
        "test success message.",
        "test warning message.",
        "test error message.",
        "test critical message.",
    ]
    fx_logger.trace(write_lines[0])
    fx_logger.debug(write_lines[1])
    fx_logger.info(write_lines[2])
    fx_logger.success(write_lines[3])
    fx_logger.warning(write_lines[4])
    fx_logger.error(write_lines[5])
    fx_logger.critical(write_lines[6])

    fx_logger.set_file_level(level=LoggerLevel.ERROR)

    fx_logger.trace(write_lines[0])
    fx_logger.debug(write_lines[1])
    fx_logger.info(write_lines[2])
    fx_logger.success(write_lines[3])
    fx_logger.warning(write_lines[4])
    fx_logger.error(write_lines[5])
    fx_logger.critical(write_lines[6])

    with fx_logger.file.file_path.open("r") as file:
        lines = file.readlines()
        assert len(lines) == len(write_lines) + 2  # nosec B101
        assert "test trace message." in lines[0]  # nosec B101
        assert LoggerLevel.TRACE.name in lines[0]  # nosec B101
        assert "test debug message." in lines[1]  # nosec B101
        assert LoggerLevel.DEBUG.name in lines[1]  # nosec B101
        assert "test info message." in lines[2]  # nosec B101
        assert LoggerLevel.INFO.name in lines[2]  # nosec B101
        assert "test success message." in lines[3]  # nosec B101
        assert LoggerLevel.SUCCESS.name in lines[3]  # nosec B101
        assert "test warning message." in lines[4]  # nosec B101
        assert LoggerLevel.WARNING.name in lines[4]  # nosec B101
        assert "test error message." in lines[5]  # nosec B101
        assert LoggerLevel.ERROR.name in lines[5]  # nosec B101
        assert "test critical message." in lines[6]  # nosec B101
        assert LoggerLevel.CRITICAL.name in lines[6]  # nosec B101
        for level in LoggerLevel:
            if level != LoggerLevel.ERROR:
                assert "test error message." in lines[7]  # nosec B101
                assert level.name not in lines[7]  # nosec B101
            elif level != LoggerLevel.CRITICAL:
                assert "test critical message." in lines[8]  # nosec B101
                assert level.name not in lines[8]  # nosec B101
            else:
                assert level.name in lines[7]  # nosec B101
                assert level.name in lines[8]  # nosec B101
