"""Streamlit app entrypoint."""

from __future__ import annotations

import streamlit as st
from loguru import logger

from app.components.sidebar import render_sidebar
from app.config import settings
from app.state import get_state, reset_state


def main() -> None:
    # ── Page config (must be first Streamlit call) ──
    st.set_page_config(
        page_title=settings.app_name,
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # ── Initialize state ──
    state = get_state()
    logger.info(f"Session active | user={state.user_id}")

    # ── Sidebar (shared across all pages) ──
    render_sidebar(state)

    # ── Auth gate ──
    if not state.user_id:
        _show_login_form()
        st.stop()

    # ── Landing page ──
    st.title(settings.app_name)
    st.markdown("Welcome! Use the sidebar to navigate between pages.")


def _show_login_form() -> None:
    """Simple login form."""
    state = get_state()

    st.title("Log in")
    with st.form("login"):
        email = st.text_input("Email")
        submitted = st.form_submit_button("Log in")
        if submitted and email:
            state.user_id = email
            logger.info(f"User logged in: {email}")
            st.rerun()


def cli() -> None:
    """CLI entrypoint so `uv run app` works."""
    import subprocess
    import sys
    from pathlib import Path

    main_file = Path(__file__).resolve()
    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(main_file),
            "--server.port=8501",
            "--server.headless=true",
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
