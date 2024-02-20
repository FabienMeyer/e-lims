"""elims-utils tests."""

import pytest

from e_lims_instruments import e_lims_instruments


@pytest.fixture()
def name() -> str:
    """Sample pytest fixture."""
    return "e-lims-instruments!"


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert "Hello e-lims-instruments!" in e_lims_instruments.hello(name)  # nosec B101
