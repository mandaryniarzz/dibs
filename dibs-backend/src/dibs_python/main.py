from fastapi import FastAPI

from dibs_python.api.v1.router import router as api_v1_router
from dibs_python.core.dependencies import SettingsDep
from dibs_python.core.settings import get_settings

cfg = get_settings()

app = FastAPI(title="Dibs", description="Dibs API", version=cfg.app_version, debug=cfg.app_debug)

app.include_router(api_v1_router)

@app.get('/health', tags=["Health"])
def health() -> dict:
    """
    Health check endpoint
    """
    return {"status": "ok"}

@app.get('/version', tags=["Version"])
def version(settings: SettingsDep) -> dict:
    """
    Version endpoint
    """
    return {"version": settings.app_version,
            "status": "ok"}