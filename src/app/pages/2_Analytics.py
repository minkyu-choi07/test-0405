"""Analytics page."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from app.components.charts import render_time_series
from app.state import get_state

state = get_state()

st.header("Analytics")

# ── Metric selector ──
metric = st.selectbox("Metric", options=["users", "revenue", "conversion_rate"])

# ── Placeholder data (replace with service call) ──
# from app.services.data_service import fetch_analytics_data
# df = fetch_analytics_data(metric, state.filters)

df = pd.DataFrame(
    {
        "date": pd.date_range("2025-01-01", periods=60, freq="D"),
        "value": [i * 1.5 + (i % 7) * 10 for i in range(60)],
    }
)

render_time_series(df, x="date", y="value", title=f"{metric} over Time")
