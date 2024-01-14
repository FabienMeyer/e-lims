"""elims-utils tests."""

import pytest

from src import e_lims_utils


@pytest.fixture()
def name() -> str:
    """Sample pytest fixture."""
    return "e-lims-utils!"


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert "Hello e-lims-utils!" in e_lims_utils.hello(name)
