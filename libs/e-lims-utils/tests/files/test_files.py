"""e-lims-utils tests files."""
from pathlib import Path

import pytest

from src.files.files import FileProperties, FileSuffix


@pytest.fixture()
def fixture_file_properties() -> FileProperties:
    """Pytest fixture for the FileProperties class."""
    return FileProperties(
        name="test",
        suffix=FileSuffix.NONE,
        path=Path.cwd(),
    )
