"""Instruments models database."""
from __future__ import annotations

import enum
from datetime import datetime, timezone
from pathlib import Path

from e_lims_utils.crud.crud import BaseSqlModel, Crud
from e_lims_utils.files.files import FileProperties, FileSuffix
from e_lims_utils.files.timestamp import Timestamp
from e_lims_utils.logger.logger import Logger, LoggerLevel


class InstrumentType(enum.StrEnum):
    """The type of instrument."""

    BIT_ERROR_RATE_TESTER = "BERT"
    DIGITAL_MULTIMETER = "DMM"
    ELECTRICAL_SIGNAL_GENERATOR = "ESG"
    OSCILLOSCOPE = "OSC"
    POWER_SUPPLY = "PWR"
    SPECTRUM_ANALYZER = "SA"
    VECTOR_NETWORK_ANALYZER = "VNA"


class InstrumentBrand(enum.StrEnum):
    """The brand of instrument."""

    ANRITSU = "AN"
    KEYSIGHT = "KS"
    RIGOL = "RG"
    ROHDE_SCHWARZ = "RS"
    TEKTRONIX = "TK"
    TELEDYNE_LECROY = "TL"


class InstrumentModel(BaseSqlModel, table=True):
    """The SQLModel representing a model.

    Attributes:
        uid (int): The unique identifier of the instrument.
        name (str): The name of the instrument.
        type (InstrumentType): The type of the instrument.
        brand (InstrumentBrand): The brand of the instrument.
        model (str): The model of the instrument.
        serial_number (str): The serial number of the instrument.
        calibration_date (datetime): The calibration date of the instrument.
        calibration_due_date (datetime): The calibration due date of the instrument.
    """
    type: InstrumentType
    brand: InstrumentBrand
    model: str
    serial_number: str
    calibration_date: datetime
    calibration_due_date: datetime

    def get_name(self) -> str:
        """Get the name of the instrument.

        Returns:
            str: The name of the instrument.
        """
        return f"{self.brand.value}-{self.type.value}-{self.model}-{self.uid}"


class InstrumentsCrud(Crud):
    """The CRUD for the InstrumentModel."""

    def __init__(self, logger: Logger, db_url: str) -> None:
        """Initialize the InstrumentCrud.

        Args:
            logger (Logger): The logger.
            db_url (str): The database URL.
        """
        super().__init__(logger, InstrumentModel, db_url)

if __name__ == "__main__":


    file = FileProperties(
        name="test_crud",
        suffix=FileSuffix.LOG,
        path=Path.cwd(),
        timestamp=Timestamp(datetime.now(tz=timezone.utc)),
    )
    logger = Logger(file=file, level=LoggerLevel.TRACE, backtrace=True, diagnose=True)
    db_url = "sqlite:///instruments.db"

    instruments_crud = InstrumentsCrud(logger, db_url)
    instruments_crud.create_table()
    instrument = InstrumentModel(
        type=InstrumentType.BIT_ERROR_RATE_TESTER,
        brand=InstrumentBrand.ANRITSU,
        model="MP1800A",
        serial_number="123456",
        calibration_date=datetime.now(timezone.utc),
        calibration_due_date=datetime.now(timezone.utc),
    )
    instruments_crud.create(instrument)
    BERT = instruments_crud.read(instrument.uid)
    print(BERT.get_name())

