"""Timestamp class."""
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Timestamp:
    """A class used to represent a Timestamp.

    Attributes:
        * now (datetime): current datetime
        * separator (str): separator used in the timestamp (default is "-")
        * year (int): year extracted from the current datetime
        * month (int): month extracted from the current datetime
        * day (int): day extracted from the current datetime
        * hour (int): hour extracted from the current datetime
        * minute (int): minute extracted from the current datetime
        * second (int): second extracted from the current datetime
        * microsecond (int): microsecond extracted from the current datetime
    """

    now: datetime
    separator: str = "-"
    year: int = dataclasses.field(init=False)
    month: int = dataclasses.field(init=False)
    day: int = dataclasses.field(init=False)
    hour: int = dataclasses.field(init=False)
    minute: int = dataclasses.field(init=False)
    second: int = dataclasses.field(init=False)
    microsecond: int = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        """The method to initialize the Timestamp object."""
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        self.microsecond = self.now.microsecond

    @property
    def date(self) -> str:
        """Returns the date in the format: year-month-day.

        Returns:
            str: a string representing the date
        """
        return f"{self.year}{self.separator}{self.month}{self.separator}{self.day}"

    @property
    def time(self) -> str:
        """Returns the time in the format: hour-minute-second.

        Returns:
            str: a string representing the time
        """
        return f"{self.hour}{self.separator}{self.minute}{self.separator}{self.second}"

    @property
    def stamp(self) -> str:
        """Returns the timestamp in the format: date_time.

        Returns:
            str: a string representing the timestamp
        """
        return f"{self.date}_{self.time}"
