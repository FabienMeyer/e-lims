"""A module for configuring and using a logger with loguru."""
from __future__ import annotations

import enum
import sys
from typing import TYPE_CHECKING

from loguru._logger import Core as _Core
from loguru._logger import Logger as _Logger

if TYPE_CHECKING:
    from e_lims_utils.files.files import FileProperties


class LoggerLevel(enum.StrEnum):
    """Enum class representing the different levels of logging.

    Attributes:
        TRACE (str): Trace level logging.
        DEBUG (str): Debug level logging.
        INFO (str): Info level logging.
        SUCCESS (str): Success level logging.
        WARNING (str): Warning level logging.
        ERROR (str): Error level logging.
        CRITICAL (str): Critical level logging.
    """

    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Logger:
    """A class for configuring and using a logger with loguru."""

    def __init__(self, file: FileProperties, level: LoggerLevel, *, backtrace: bool = True, diagnose: bool = True) -> None:
        """Initializes the Logger object after its attributes have been set."""
        self.file = file
        self.level = level
        self.backtrace = backtrace
        self.diagnose = diagnose
        self._logger = _Logger(
            core=_Core(),
            exception=None,
            depth=0,
            record=False,
            lazy=False,
            colors=False,
            raw=False,
            capture=True,
            patchers=[],
            extra={},
        )
        self._logger.add(sink=sys.stdout, level=self.level.value, backtrace=self.backtrace, diagnose=self.diagnose)
        self._logger.add(sink=str(file.file_path), level=self.level.value, backtrace=self.backtrace, diagnose=self.diagnose)

    def set_file_level(self, level: LoggerLevel) -> None:
        """Set the file handler level."""
        if self.level != level.value:
            self._logger.remove(list(self._logger._core.handlers.keys())[-1])  # noqa: SLF001
            self._logger.add(sink=str(self.file.file_path), level=level.value, backtrace=self.backtrace, diagnose=self.diagnose)

    def trace(self, message: str) -> None:
        """Log a trace message.

        Args:
            message (str): The message to log.
        """
        self._logger.trace(message)

    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): The message to log.
        """
        self._logger.debug(message)

    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): The message to log.
        """
        self._logger.info(message)

    def success(self, message: str) -> None:
        """Log a success message.

        Args:
            message (str): The message to log.
        """
        self._logger.success(message)

    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): The message to log.
        """
        self._logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): The message to log.
        """
        self._logger.error(message)

    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): The message to log.
        """
        self._logger.critical(message)
