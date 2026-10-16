from fastapi import FastAPI

from dibs_python.core.settings import settings

from dibs_python.api.v1.router import router as api_v1_router

app = FastAPI(title="Dibs", description="Dibs API", version=settings.app_version, debug=settings.app_debug)

app.include_router(api_v1_router)

@app.get('/health', tags=["Health"])
def health() -> dict:
    """
    Health check endpoint
    """
    return {"status": "ok"}

@app.get('/version', tags=["Version"])
def version() -> dict:
    """
    Version endpoint
    """
    return {"version": settings.app_version,
            "status": "ok"}