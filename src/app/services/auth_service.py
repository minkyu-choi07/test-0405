"""Authentication service."""

from __future__ import annotations

from loguru import logger


def authenticate(email: str, password: str) -> bool:
    """Authenticate a user. Replace with real auth logic."""
    # TODO: Integrate with your auth provider (e.g., Supabase, Auth0, etc.)
    logger.info(f"Auth attempt for: {email}")
    return bool(email and password)


def get_user_roles(user_id: str) -> list[str]:
    """Fetch roles for a user. Replace with real lookup."""
    # TODO: Fetch from database or auth provider
    return ["viewer"]
