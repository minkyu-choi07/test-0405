"""Data fetching and caching service."""

from __future__ import annotations

import httpx
import pandas as pd
import streamlit as st

from app.config import settings


@st.cache_data(ttl=settings.cache_ttl_seconds)
def fetch_dashboard_data(filters: dict | None = None) -> pd.DataFrame:
    """Fetch dashboard data from API with Streamlit caching.

    Args:
        filters: Query parameters to pass to the API.

    Returns:
        DataFrame with the dashboard data.
    """
    params = filters or {}
    with httpx.Client(base_url=settings.api_base_url, timeout=30) as client:
        response = client.get("/dashboard", params=params)
        response.raise_for_status()
    return pd.DataFrame(response.json().get("data", []))


@st.cache_data(ttl=settings.cache_ttl_seconds)
def fetch_analytics_data(metric: str, filters: dict | None = None) -> pd.DataFrame:
    """Fetch analytics data for a specific metric."""
    params = {"metric": metric, **(filters or {})}
    with httpx.Client(base_url=settings.api_base_url, timeout=30) as client:
        response = client.get("/analytics", params=params)
        response.raise_for_status()
    return pd.DataFrame(response.json().get("data", []))
