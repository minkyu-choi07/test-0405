"""Heavy resource caching (DB connections, ML models, etc.)."""

from __future__ import annotations

import streamlit as st

from app.config import settings


@st.cache_resource
def get_db_engine():
    """Create a SQLAlchemy engine cached for the app's lifetime.

    Returns a singleton engine per Streamlit worker.
    """
    from sqlalchemy import create_engine

    return create_engine(settings.database_url, echo=settings.debug)
