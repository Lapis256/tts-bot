from .interaction import router as interaction_router  # noqa
from .api import router as api_router
from .websocket import router as ws_router

routers = (
    interaction_router,
    api_router,
    ws_router
)
