from __future__ import annotations
from typing import Optional

from pydantic import BaseModel

from .discord import User, Member


class InteractionDataOption(BaseModel):
    name: str
    value: Optional[int] = None
    options: Optional[list[InteractionDataOption]] = []
InteractionDataOption.update_forward_refs()


class InteractionData(BaseModel):
    id: str
    name: str
    options: Optional[list[InteractionDataOption]] = []


class InteractionRequestData(BaseModel):
    id: str
    type: int
    data: Optional[InteractionData] = None
    guild_id: Optional[str] = None
    channel_id: Optional[str] = None
    member: Optional[Member] = None
    user: Optional[User] = None
    token: Optional[str] = None
    version: int
