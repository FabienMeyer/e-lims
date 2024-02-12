"""File properties and suffixes."""
from __future__ import annotations

import dataclasses
from enum import StrEnum
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .timestamp import Timestamp


class FileSuffix(StrEnum):
    """An enumeration class used to represent suppoted file suffixes.

    Attributes:
        * LOG (str): log file suffix
        * NONE (str): no file suffix
    """

    LOG = "log"
    NONE = ""


@dataclasses.dataclass
class FileProperties:
    """A class used to represent the properties of a file.

    This class encapsulates the name, suffix, path, and timestamp of a file.
    It provides utility methods to get the file name with the suffix and the full file path.

    Attributes:
    name (str): The name of the file without the suffix.
    suffix (FileSuffix): The suffix or extension of the file, represented as a member of the FileSuffix enum.
    path (Path): The directory path where the file is located or will be created.
    timestamp (Optional[Timestamp]) :The timestamp associated with the file. This is optional and defaults to None. If provided, it will be included in the file name.

    Methods:
        * __post_init__(): Initializes the FileProperties object. If the path does not exist, it creates the directory.
        * file_name(): Returns the file name with the suffix and optionally the timestamp. The format is 'name_timestamp.suffix' if timestamp is provided, otherwise 'name.suffix'.
        * file_path(): Returns the full file path, which is the concatenation of the path and the file name.
    """

    name: str
    suffix: FileSuffix
    path: Path
    timestamp: Timestamp | None = None

    def __post_init__(self) -> None:
        """The method to initialize the FileProperties object.

        If the path does not exist, it creates the directory with read, write and execute permissions for all users.
        """
        if not self.path.exists():
            self.path.mkdir(mode=0o777, parents=True, exist_ok=True)

    @property
    def file_name(self) -> str:
        """Returns the file name with the suffix and optionally the timestamp.

        The format is 'name_timestamp.suffix' if timestamp is provided, otherwise 'name.suffix'.

        Returns:
            str: a string representing the file name with the suffix and optionally the timestamp
        """
        if self.timestamp is None:
            return f"{self.name}.{self.suffix.value}"
        return f"{self.name}_{self.timestamp.stamp}.{self.suffix.value}"

    @property
    def file_path(self) -> Path:
        """Returns the full file path, which is the concatenation of the path and the file name.

        Returns:
            Path: a Path object representing the full file path
        """
        return self.path / self.file_name

    def create_file(self) -> None:
        """Creates a file with the file path.

        Returns:
            Path: a Path object representing the full file path
        """
        Path.open(self.file_path, "w").close()
