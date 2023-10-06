# -*- coding: utf-8 -*-
"""elims tests."""

import pytest

from src import e_lims_logger


@pytest.fixture
def name() -> str:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return "e-lims-logger"


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert "Hello e-lims-logger!" in e_lims_logger.hello(name)
