from typing import Optional
from os import environ

from fastapi import Header, Request, HTTPException
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError


PUBLIC_KEY = environ["PUBLIC_KEY"]


async def verify(
    request: Request,
    x_signature_ed25519: Optional[str] = Header(None),
    x_signature_timestamp: Optional[str] = Header(None)
):
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    try:
        verify_key.verify(
            x_signature_timestamp.encode() + await request.body(),
            bytes.fromhex(x_signature_ed25519)
        )
    except BadSignatureError:
        raise HTTPException(status_code=401)
