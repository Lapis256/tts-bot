from fastapi import APIRouter, Depends

from util.verify import api_verify


router = APIRouter(
    prefix="/api",
    dependencies=[Depends(api_verify)]
)
