"""A module for configuring and using a logger with loguru."""
from __future__ import annotations

import dataclasses
import enum
import sys
from typing import TYPE_CHECKING

from loguru._logger import Core as _Core
from loguru._logger import Logger as _Logger

if TYPE_CHECKING:
    from src.files.files import FileProperties


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


@dataclasses.dataclass
class Logger:
    """A class for configuring and using a logger with loguru.

    Attributes:
        file (FileProperties): The properties of the logger file.
        sys_level (LoggerLevel): The logger level for the console stream.
        file_level (LoggerLevel): The logger level for the logger file.
        stream (logger): The loguru logger object.
    """

    file: FileProperties
    sys_level: LoggerLevel = LoggerLevel.INFO
    file_level: LoggerLevel = LoggerLevel.TRACE
    backtrace: bool = True
    diagnose: bool = True
    logger: _Logger = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        """Initializes the Logger object after its attributes have been set."""
        logger = _Logger(
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
        logger.add(sys.stdout, level=self.sys_level.value, backtrace=self.backtrace, diagnose=self.diagnose)
        logger.add(str(self.file.file_path), level=self.file_level.value)
        self.logger = logger
