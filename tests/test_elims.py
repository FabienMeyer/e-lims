# -*- coding: utf-8 -*-
"""e-lims tests."""

import pytest

from e-lims import e-lims


@pytest.fixture
def name() -> str:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 'World'


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert 'Hello World' in e-lims.hello(name)
