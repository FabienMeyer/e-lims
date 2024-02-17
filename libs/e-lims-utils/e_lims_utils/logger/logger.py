"""A module for configuring and using a logger with loguru."""
from __future__ import annotations

import enum
import sys
from typing import TYPE_CHECKING

from loguru._logger import Core as _Core
from loguru._logger import Logger as _Logger

if TYPE_CHECKING:
    from e_lims_utils.files.files import FileProperties


class LoggerLevel(enum.Enum):
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
    """A class for configuring and using a logger with loguru.

    Attributes:
        _logger (Logger): The loguru logger object.
    """

    def __init__(self, file: FileProperties, sys_level: LoggerLevel = LoggerLevel.INFO, file_level: LoggerLevel = LoggerLevel.TRACE, backtrace: bool = True, diagnose: bool = True) -> None:
        """Initializes the Logger object after its attributes have been set."""
        self._file = file
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
        self.add(sys.stdout, level=sys_level, backtrace=backtrace, diagnose=diagnose)
        self.add(str(self._file.file_path), level=file_level, backtrace=backtrace, diagnose=diagnose)

    def add(self, sink: str, level: LoggerLevel, backtrace: bool = True, diagnose: bool = True) -> None:
        """Add a new sink to the logger.

        Args:
            sink (str): The sink to add to the logger.
            level (str): The level of the sink.
            backtrace (bool): Whether to include backtrace information.
            diagnose (bool): Whether to include diagnose information.
        """
        self._logger.add(sink, level=level.value, backtrace=backtrace, diagnose=diagnose)

    def remove(self, handler_id: int) -> None:
        """Remove a sink from the logger.

        Args:
            handler_id (int): The id of the handler to remove.
        """
        self._logger.remove(handler_id)

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