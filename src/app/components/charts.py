"""Reusable chart components."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st


def render_time_series(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "",
) -> None:
    """Render a Plotly time-series line chart."""
    fig = px.line(df, x=x, y=y, title=title)
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)


def render_kpi_row(metrics: list[dict]) -> None:
    """Render a row of KPI metric cards.

    Each metric dict: {"label": str, "value": str|int|float, "delta": str|None}
    """
    cols = st.columns(len(metrics))
    for col, m in zip(cols, metrics):
        col.metric(
            label=m["label"],
            value=m["value"],
            delta=m.get("delta"),
        )
