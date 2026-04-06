"""Shared test fixtures."""

import pytest


@pytest.fixture
def sample_filters() -> dict:
    return {"categories": ["Sales"], "date_range": ("2025-01-01", "2025-01-31")}
