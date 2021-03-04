from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    discriminator: str
    avatar: str
    bot: Optional[bool] = None
    system: Optional[bool] = None
    mfa_emabled: Optional[bool] = None
    locale: Optional[str] = None
    verified: Optional[bool] = None
    email: Optional[str] = None
    flags: Optional[int] = None
    premium_types: Optional[int] = None
    public_flags: Optional[int] = None


class Member(BaseModel):
    user: Optional[User] = {}
    nick: Optional[str] = None
    roles: list[str] = None
    joined_at: str
    premium_since: Optional[str] = None
    deaf: bool
    mute: bool
    pending: Optional[bool] = None
    permissions: Optional[str] = None
