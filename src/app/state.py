"""Typed session state manager."""

from dataclasses import dataclass, field

import streamlit as st


@dataclass
class AppState:
    """Typed wrapper around st.session_state."""

    user_id: str | None = None
    current_page: str = "dashboard"
    filters: dict = field(default_factory=dict)
    data_cache: dict = field(default_factory=dict)


def get_state() -> AppState:
    """Get or initialize the typed app state."""
    if "app_state" not in st.session_state:
        st.session_state.app_state = AppState()
    return st.session_state.app_state


def reset_state() -> None:
    """Reset app state to defaults."""
    st.session_state.app_state = AppState()
