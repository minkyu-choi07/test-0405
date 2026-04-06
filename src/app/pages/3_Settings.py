"""Settings page."""

from __future__ import annotations

import streamlit as st

from app.config import settings
from app.state import get_state

state = get_state()

st.header("Settings")

st.subheader("App Configuration")
st.json(
    {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "api_base_url": settings.api_base_url,
        "cache_ttl_seconds": settings.cache_ttl_seconds,
    }
)

st.subheader("Session State")
st.json(
    {
        "user_id": state.user_id,
        "current_page": state.current_page,
        "filters": state.filters,
    }
)

if st.button("Clear cache"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("Cache cleared.")
