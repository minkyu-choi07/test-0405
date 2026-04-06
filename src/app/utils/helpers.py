"""General-purpose helper functions."""

from __future__ import annotations

import pandas as pd


def format_currency(value: float, symbol: str = "$") -> str:
    """Format a number as currency string."""
    return f"{symbol}{value:,.2f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a float as percentage string."""
    return f"{value:.{decimals}%}"


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Divide without ZeroDivisionError."""
    return numerator / denominator if denominator != 0 else default


def df_to_csv_bytes(df: pd.DataFrame) -> bytes:
    """Convert DataFrame to CSV bytes for st.download_button."""
    return df.to_csv(index=False).encode("utf-8")
