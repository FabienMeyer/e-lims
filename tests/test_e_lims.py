"""elims tests."""

import pytest

from src import e_lims


@pytest.fixture()
def name() -> str:
    """Sample pytest fixture."""
    return "e-lims"


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert "Hello e-lims!" in e_lims.hello(name)
