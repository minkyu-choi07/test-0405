"""Shared sidebar component."""

from __future__ import annotations

from datetime import date, timedelta

import streamlit as st

from app.state import AppState, reset_state


def render_sidebar(state: AppState) -> None:
    """Render the shared sidebar with filters and user info."""
    with st.sidebar:
        st.header("Filters")

        # ── Date range ──
        today = date.today()
        date_range = st.date_input(
            "Date range",
            value=(today - timedelta(days=30), today),
        )
        state.filters["date_range"] = date_range

        # ── Category multi-select ──
        categories = st.multiselect(
            "Categories",
            options=["Sales", "Marketing", "Engineering", "Support"],
            default=[],
        )
        state.filters["categories"] = categories

        st.divider()

        # ── User info ──
        if state.user_id:
            st.caption(f"Logged in as **{state.user_id}**")
            if st.button("Log out"):
                reset_state()
                st.rerun()
