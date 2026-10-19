from fastapi import FastAPI

from app.routers import health

def create_app() -> FastAPI:
    app = FastAPI(title="Book API")
    app.include_router(health.router)

    return app