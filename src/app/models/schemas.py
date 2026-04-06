"""Pydantic schemas for API data validation."""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel


class DashboardRow(BaseModel):
    """Single row of dashboard data."""

    date: date
    users: int
    revenue: float
    conversion_rate: float


class DashboardResponse(BaseModel):
    """API response wrapper for dashboard endpoint."""

    data: list[DashboardRow]
    total_count: int = 0


class UserProfile(BaseModel):
    """User profile model."""

    id: str
    email: str
    display_name: str
    roles: list[str] = ["viewer"]
