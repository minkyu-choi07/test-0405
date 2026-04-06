"""Dashboard page."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from app.components.charts import render_kpi_row, render_time_series
from app.state import get_state
from app.utils.helpers import df_to_csv_bytes, format_currency, format_percentage

state = get_state()

st.header("Dashboard")

# ── Fetch data (replace with real service call) ──
# from app.services.data_service import fetch_dashboard_data
# df = fetch_dashboard_data(state.filters)

# Placeholder demo data
df = pd.DataFrame(
    {
        "date": pd.date_range("2025-01-01", periods=30, freq="D"),
        "users": range(100, 130),
        "revenue": [x * 42.5 for x in range(100, 130)],
        "conversion_rate": [0.03 + i * 0.001 for i in range(30)],
    }
)

# ── KPIs ──
render_kpi_row(
    [
        {"label": "Total Users", "value": int(df["users"].sum()), "delta": "+12%"},
        {"label": "Revenue", "value": format_currency(df["revenue"].sum())},
        {"label": "Avg Conversion", "value": format_percentage(df["conversion_rate"].mean())},
    ]
)

# ── Chart ──
render_time_series(df, x="date", y="revenue", title="Revenue over Time")

# ── Raw data ──
with st.expander("Raw data"):
    st.dataframe(df, use_container_width=True)
    st.download_button(
        "Download CSV",
        data=df_to_csv_bytes(df),
        file_name="dashboard.csv",
        mime="text/csv",
    )
