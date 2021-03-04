from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from model.interaction import InteractionRequestData
from verify import verify


router = APIRouter(
	prefix="/interactions",
	dependencies=[Depends(verify)]
)


@router.post("")
async def post(data: InteractionRequestData):
    if data.type == 1:
        return {"type": 1}

    elif data.type == 2:
        if data.data.name == "help":
            return JSONResponse({
                "type": 4,
                "data": {
                    "content": "Hello."
                }
            })
