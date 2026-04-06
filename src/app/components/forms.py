"""Reusable form components."""

from __future__ import annotations

import streamlit as st


def render_search_form(key: str = "search") -> str | None:
    """Render a simple search input and return the query string."""
    query = st.text_input("Search", placeholder="Type to search...", key=key)
    return query if query else None
