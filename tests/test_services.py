"""Tests for service layer."""

from app.utils.helpers import format_currency, format_percentage, safe_divide


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"
    assert format_currency(0) == "$0.00"


def test_format_percentage():
    assert format_percentage(0.123) == "12.3%"


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == 0.0
    assert safe_divide(10, 0, default=-1.0) == -1.0
