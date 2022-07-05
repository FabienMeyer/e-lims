# -*- coding: utf-8 -*-
"""`e_lims` tests."""

import pytest

from e_lims import e_lims


@pytest.fixture
def name():
    # type: () -> str
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return "World"


def test_content(name):
    # type: (str) -> None
    """Sample pytest test function with the pytest fixture as an argument."""
    assert "Hello World" in e_lims.hello(name)
